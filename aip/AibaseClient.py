# -*- coding: utf-8 -*-

"""
    AipBase
"""
import json
import time
import requests
requests.packages.urllib3.disable_warnings()
from utils.ApiUrl import AiUrl
from utils import Constant
class AipBase(object):
    """
        AipBase
    """
    def __init__(self, accesskey, secretKey):
        """
            AipBase( accesskey, secretKey)
        """
        self._accessKey = accesskey.strip()
        self._secretKey = secretKey.strip()
        self._authObj = {}
        self.__client = requests
        self.__connectTimeout = 60.0
        self.__socketTimeout = 60.0
        self._proxies = {}

    def getVersion(self):
        """
            version
        """
        return AiUrl.VERSION

    def setConnectionTimeoutInMillis(self, ms):
        """
            setConnectionTimeoutInMillis
        """

        self.__connectTimeout = ms / 1000.0

    def setSocketTimeoutInMillis(self, ms):
        """
            setSocketTimeoutInMillis
        """

        self.__socketTimeout = ms / 1000.0

    def setProxies(self, proxies):
        """
            proxies
        """

        self._proxies = proxies

    def _request(self, url, data, headers=None):
        """
            self._request('', {})
        """
        try:
            result = self._validate(url, data)
            if result != True:
                return result

            authObj = self._auth()
            params = self._getParams(authObj)

            data = self._proccessRequest(data)
            headers = self._getHeaders('POST',headers)
            response = self.__client.post(url, data=data, params=params, 
                            headers=headers, verify=False, timeout=(
                                self.__connectTimeout,
                                self.__socketTimeout,
                            ), proxies=self._proxies
                        )
            obj = self._proccessResult(response.content)

        except (requests.exceptions.ReadTimeout, requests.exceptions.ConnectTimeout) as e:
            return {
                'error_msg': 'connection or read data timeout',
            }
 
        return obj

    def _validate(self, url, data):
        """
            validate
        """

        return True

    def _proccessRequest(self,data):
        """
            参数处理
        """


        return data

    def _proccessResult(self, content):
        """
            formate result
            返回结果转字典
        """


        return json.loads(content.decode()) or {}

    def _auth(self, refresh=False):
        """
            api access auth
            #获取token
        """

        #如果未过期
        if not refresh:
                ## 判断token是否过过期，如果没过期，是否还剩余大于30s时间
            tm = self._authObj.get('time', 0) + int(self._authObj.get('expires_in', 0)) - 30
            if tm > int(time.time()):
                return self._authObj
        headers = None
        headers = self._getHeaders('POST', headers)
        data_dict = {
            'accesskey': self._accessKey,
            'secretkey': self._secretKey,
        }
        data = json.dumps(data_dict)
        obj = self.__client.post(AiUrl.AiOnlineAuthurl,
                                 verify=False,
                                 headers=headers,
                                 data=data,
                                 timeout=(self.__connectTimeout,self.__socketTimeout,),
                                 proxies=self._proxies).json()
        obj['time'] = int(time.time())
        obj['expires_in'] = Constant.TOKEN_EXPIRE_TIME
        self._authObj = obj

        return obj

    def _getParams(self, authObj):
        """
            api request http url params
        """

        params = {}

        return params

    def _getHeaders(self,method, headers=None):
        """
            api request http headers
        """

        headers = headers or {}
        headers[ 'Content-Type'] ='application/json'
        headers[ 'charset'] ='utf8'
        headers[ 'Accept'] ='application/json;charset=utf-8'

        return headers


