########### Python 3.6 #############
from aip.AiVisionClient import AiVisionClient

def invokeObjectRecognitionService():
    """
    Object Recognition
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    VisionClient = AiVisionClient(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = VisionClient.objectRecognition("E:\\project\\brain-lenovo-sdk\\static\\ImgRecognition_animal.jpg")
    return data

def invokeMoblieRecognitionService():
    """
    Object Recognition
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    VisionClient = AiVisionClient(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = VisionClient.moblieRecognition("E:\\project\\brain-lenovo-sdk\\static\\ImgRecognition_animal.jpg")
    return data


def invokeSceneRecognitionService():
    """
    Scene Recognition
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    VisionClient = AiVisionClient(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = VisionClient.sceneRecognition("E:\\project\\brain-lenovo-sdk\\static\\ImgRecognition_animal.jpg")
    return data


def invokePhotoRecognitionService():
    """
    Photo Recognition
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    VisionClient = AiVisionClient(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = VisionClient.photoRecognition("E:\\project\\brain-lenovo-sdk\\static\\ImgRecognition_animal.jpg")
    return data


if __name__ == '__main__':
    print(invokeObjectRecognitionService())
    print(invokeMoblieRecognitionService())  # 不通
    print(invokeSceneRecognitionService())
    print(invokePhotoRecognitionService())