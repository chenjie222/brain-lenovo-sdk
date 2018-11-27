########### Python 3.6 #############
from aip.AiCaClient import AiCaClient

def invokeGenderClassificationService():
    """
    性别识别
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    CaClient = AiCaClient(YourAccessKey,YoursecretKey)
    # 调用genderDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = CaClient.genderDetection("E:\\project\\brain-lenovo-sdk\\static\\female.wav")
    return data


def invokeSceneClassificationService():
    """
    场景识别
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    CaClient = AiCaClient(YourAccessKey, YoursecretKey)
    # sceneCliassification，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = CaClient.sceneCliassification("E:\\project\\brain-lenovo-sdk\\static\\car.wav")
    return data


def invokeSoundClassificationService():
    """
    环境识别
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    CaClient = AiCaClient(YourAccessKey, YoursecretKey)
    # 调用 ambientDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = CaClient.ambientDetection("E:\\project\\brain-lenovo-sdk\\static\\ambient.wav")
    return data


def invokeInfantCryingDetectionService():
    """
    crying识别
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    CaClient = AiCaClient(YourAccessKey, YoursecretKey)
    # 调用 infantCryingDetection，传入文件、文件path、json对象、dict、bytes、均可返回AI result
    data = CaClient.infantCryingDetection("E:\\project\\brain-lenovo-sdk\\static\\cry_1.wav")
    return data


if __name__ == '__main__':
    print(invokeGenderClassificationService())
    print(invokeSceneClassificationService())
    print(invokeSoundClassificationService())
    print(invokeInfantCryingDetectionService())