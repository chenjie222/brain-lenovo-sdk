
# -*- coding: utf-8 -*-

"""
自然语言处理
"""
import json

from aip.AibaseClient import AipBase
from utils.NLPRequestProcess import ProcessRequestSentiment,ProcessRequestStandford
from utils.ApiUrl import AiUrl


class AipNlpClinet(AipBase):

    """
    自然语言处理
    """
    def chineseSentimentAnalysis(self, options):
        """
            词法分析
        """
        token = self._auth()['result']['token']
        data = ProcessRequestSentiment(options)
        ChineseSentimentAnalysisUrl = AiUrl.Ai_NlpChineseAnalysis + token
        return self._request(ChineseSentimentAnalysisUrl, data)

    def wordSegmentation(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = ProcessRequestStandford(options)
        AiNlpSegmentationUrl = AiUrl.AiNlpSegmentation + token
        return self._request(AiNlpSegmentationUrl, data)


    def partTagging(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = ProcessRequestStandford(options)
        AiNlpPARTUrl = AiUrl.AiNlpPART + token
        return self._request(AiNlpPARTUrl, data)

    def lemmatization(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = ProcessRequestStandford(options)
        AiNlpLemmatizationUrl = AiUrl.AiNlpLemmatization + token
        return self._request(AiNlpLemmatizationUrl, data)

    def namedEntityRecognition(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = ProcessRequestStandford(options)
        AiNlpNamedEntityRecognitionUrl = AiUrl.AiNlpNamedEntityRecognition + token
        return self._request(AiNlpNamedEntityRecognitionUrl, data)


    def parsing(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = ProcessRequestStandford(options)
        AiNlpparsingUrl = AiUrl.AiNlpParsing + token
        return self._request(AiNlpparsingUrl, data)


    def relationshipExtraction(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = ProcessRequestStandford(options)
        AiNlpRelationExtrationUrl = AiUrl.AiNlpRelationExtration + token
        return self._request(AiNlpRelationExtrationUrl, data)

    def coreferenceResolution(self, options):
        """

        """
        token = self._auth()['result']['token']
        data = ProcessRequestStandford(options)
        AiNlpConferenceResolutionUrl = AiUrl.AiNlpConferenceResolution + token
        return self._request(AiNlpConferenceResolutionUrl, data)

