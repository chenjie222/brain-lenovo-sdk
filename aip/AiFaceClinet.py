
# -*- coding: utf-8 -*-

"""
人脸识别
"""
import json

from aip.AibaseClient import AipBase
from utils.ApiUrl import AiUrl
from utils.FaceRequestProcess import processRequest

class AiFaceClient(AipBase):

    """
    人脸识别
    """

    def faceDetection(self, options):
        """
            人脸检测
            #调用人脸接口，需传一个option 即path或者image或者byte
        """
        token = self._auth()['result']['token']
        #AiVisionFaceDetection = BaseUrl + "v1/facedetect" + TOKEN
        data = processRequest(options)
        FaceDetectionUrl = AiUrl.AiVisionFaceDetection + token
        return self._request(FaceDetectionUrl, data)


    def faceAttributeRecognition(self,options):
        """
        人脸属性识别

        """
        token = self._auth()['result']['token']
        data = processRequest(options)
        faceAttributeRecognitionUrl = AiUrl.AiVisionFaceAttr + token
        return self._request(faceAttributeRecognitionUrl, data)

    def faceComparision(self,optionsOne, optionsTwo):
        """
        人脸比对

        """
        token = self._auth()['result']['token']
        dataOne = json.loads(processRequest(optionsOne))
        dataTwo = json.loads(processRequest(optionsTwo))
        data_dict = {
            "image1": {
                "base64Data": dataOne['base64Data']
            },
            "image2": {
                "base64Data": dataTwo['base64Data']
            },
        }
        data = json.dumps(data_dict)
        faceComparisionUrl = AiUrl.AiVisionFaceComparison + token
        return self._request(faceComparisionUrl, data)

