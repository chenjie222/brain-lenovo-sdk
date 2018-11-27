import base64
import json
import re
import json


def checkJsonFormat(raw_msg):
    """
    判断字符串是不是json对象
    """
    if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False

def ProcessRequestSentiment(option):
    data_json = {}
    if type(option).__name__ == 'str':
        # 如果传text文件
        if re.findall(r'([^<>/\\\|:""\*\?]+\.\w+$)', option) :
            with open(option, "r", encoding="UTF-8") as f:
                data = f.read()
                data_dict = {
                    'data': data,
                }
                data_json = json.dumps(data_dict)

        # 如果上传jsonobject
        if checkJsonFormat(option):
            data_json = option

        # 如果传string message
        if re.findall('[\u4E00-\u9FA5]', option):
            data_dict = {
                'data': option
            }
            data_json = json.dumps(data_dict)

    #如果上传字典dict
    if type(option).__name__ == 'dict' :
        data_json = option

    return data_json

def ProcessRequestStandford (option):
    data_json = {}
    if type(option).__name__ == 'str':
        # 如果传text文件 path
        if re.findall(r'([^<>/\\\|:""\*\?]+\.\w+$)', option) :
            try:
                with open(option, "r") as f:
                    data = f.read()
            except IOError:
                print("error:The file was not found or read failed")
                return
            data_dict = {
                "language" : "en-us",
                'data': data,
            }
            data_json = json.dumps(data_dict)

        # 如果上传jsonobject
        if checkJsonFormat(option):
            data_json = option

        # 如果传string message
        if re.findall(r'([a-zA-Z]+)', option):
            data_dict = {
                'data': option
            }
            data_json = json.dumps(data_dict)

    #如果上传bytes
    if type(option).__name__ == 'bytes':
        data_str = option.decode()
        data_dict = {
            'data': data_str
        }
        data_json = json.dumps(data_dict)

    #如果上传字典
    if type(option).__name__ == 'dict' :
        data_json = option

    return data_json