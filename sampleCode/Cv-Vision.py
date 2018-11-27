########### Python 3.6 #############
from aip.AiSpeechClient import AipSpeechClient

def invokeAsrService():
    """
    语音识别
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    SpeechClient = AipSpeechClient(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = SpeechClient.asr("E:\\project\\brain-lenovo-sdk\\static\\test1.wav")
    return data


if __name__ == '__main__':
    print(invokeAsrService())