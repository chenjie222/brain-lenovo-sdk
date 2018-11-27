# -*- coding: utf-8 -*-

from aip.AibaseClient import AipBase
from utils.ApiUrl import AiUrl
from utils.CaRequestProcess import processRequest

class AiCaClient(AipBase):

    """
    Context Awareness
    """
    def genderDetection(self, options, bit=16, rate=8000, windowSize=2.56):
        """
        性别识别
        """
        token = self._auth()['result']['token']
        data = processRequest(options, bit, rate, windowSize)
        CAGenderDetectionUrl = AiUrl.AiCAGenderClassifier + token
        return self._request(CAGenderDetectionUrl, data)

    def sceneCliassification(self, options, bit=16, rate=8000, windowSize=2.56):
        """
        场景识别
        """
        token = self._auth()['result']['token']
        data = processRequest(options, bit, rate, windowSize)
        CASceneClassifierUrl = AiUrl.AiCASceneClassifier + token
        return self._request(CASceneClassifierUrl, data)


    def ambientDetection(self, options, bit=16, rate=8000, windowSize=2.56):
        """
        环境识别
        """
        token = self._auth()['result']['token']
        data = processRequest(options, bit, rate, windowSize)
        CAAmbientDetectionUrl = AiUrl.AiCAAmbientDetection + token
        return self._request(CAAmbientDetectionUrl, data)

    def infantCryingDetection(self, options, bit=16, rate=8000, windowSize=2.56):
        """
        环境识别
        """
        token = self._auth()['result']['token']
        data = processRequest(options, bit, rate, windowSize)
        CACryClassifierUrl = AiUrl.AiCACryClassifier + token
        return self._request(CACryClassifierUrl, data)

