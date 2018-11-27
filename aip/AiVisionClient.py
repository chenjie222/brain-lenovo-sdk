
# -*- coding: utf-8 -*-

import json

from aip.AibaseClient import AipBase
from utils.ApiUrl import AiUrl
from utils.VisionRequestProcess import processRequest

class AiVisionClient(AipBase):

    """
    图像识别
    """

    def objectRecognition(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = processRequest(options)
        VisionObjectRecognitionUrl = AiUrl.AiVisionObjectRecognition + token
        return self._request(VisionObjectRecognitionUrl, data)

    def moblieRecognition(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = processRequest(options)
        VisionMoblieRecognitionUrl = AiUrl.AiVisionMoblieRecognition + token
        return self._request(VisionMoblieRecognitionUrl, data)

    def sceneRecognition(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = processRequest(options)
        VisionSceneRecognitionUrl = AiUrl.AiVisionSceneRecognition + token
        return self._request(VisionSceneRecognitionUrl, data)

    def photoRecognition(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = processRequest(options)
        VisionPhotoClassificationUrl = AiUrl.AiVisionPhotoClassification + token
        return self._request(VisionPhotoClassificationUrl, data)
