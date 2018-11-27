# -*- coding: utf-8 -*-

"""
    Speech
"""


from aip.AibaseClient import AipBase
from utils.AsrRequestProcess import processRequest
from utils.ApiUrl import AiUrl

class AipSpeechClient(AipBase):
    """
        Aip Speech
    """
    def asr(self, options, rate=16000):
        """
            语音识别
        """
        token = self._auth()['result']['token']
        data = processRequest(options,rate)
        VoiceasrUrl = AiUrl.AiVoiceasr + token
        return self._request(VoiceasrUrl, data)


