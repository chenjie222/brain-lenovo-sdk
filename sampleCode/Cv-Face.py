########### Python 3.6 #############
from aip.AiFaceClinet import AiFaceClient

def invokeFaceDetectionService():
    """
    人脸识别
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    FaceClient = AiFaceClient(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = FaceClient.faceDetection("E:\\project\\brain-lenovo-sdk\\static\\face_1.jpg")
    return data


def invokeFaceAttributeRecognitionService():
    """
    人脸属性
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    FaceClient = AiFaceClient(YourAccessKey, YoursecretKey)
    # faceAttributeRecognition，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = FaceClient.faceAttributeRecognition("E:\\project\\brain-lenovo-sdk\\static\\face_1.jpg")
    return data


def invokeFaceComparisionService():
    """
    人脸比对
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    FaceClient = AiFaceClient(YourAccessKey, YoursecretKey)
    # 调用 ambientDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = FaceClient.faceComparision("E:\\project\\brain-lenovo-sdk\\static\\face_1.jpg", "E:\\project\\brain-lenovo-sdk\\static\\face_1.jpg")
    return data



if __name__ == '__main__':
    print(invokeFaceDetectionService())
    print(invokeFaceAttributeRecognitionService())
    print(invokeFaceComparisionService())