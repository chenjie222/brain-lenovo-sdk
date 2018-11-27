# -*- coding: utf-8 -*-

"""
人脸识别
"""
import json

from aip.AibaseClient import AipBase
from utils.ApiUrl import AiUrl
from utils.KgRequestProcess import processRequest

class AiKgClient(AipBase):

    """
    Knowledge Graph
    """

    def relationshipExtraction(self, options, confidence=0.5):
        """
        :param options: request data
        :param confidence: 置信度
        :return:Knowledge Graph
        """
        token = self._auth()['result']['token']
        data = processRequest(options, confidence)
        KGOpenIEUrl = AiUrl.AiKGOpenIE + token
        return self._request(KGOpenIEUrl, data)


    def entityLinking(self, options, confidence=0.5):
        """
        :param options: request data
        :param confidence: 置信度
        :return:Knowledge Graph
        """
        token = self._auth()['result']['token']
        data = processRequest(options, confidence)
        KGAnnotateUrl = AiUrl.AiKGAnnotate + token
        return self._request(KGAnnotateUrl, data)
