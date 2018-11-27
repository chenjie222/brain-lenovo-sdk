########### Python 3.6 #############
from aip.AiKgClient import AiKgClient

def invokeRelationshipExtractionService():
    """
    Relationship Extraction
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    KgClient = AiKgClient(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = KgClient.relationshipExtraction("E:\\project\\brain-lenovo-sdk\\static\\kg-chinese.txt")
    return data


def invokeEntityLinkingService():
    """
    Entity Linking
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    KgClient = AiKgClient(YourAccessKey, YoursecretKey)
    # faceAttributeRecognition，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = KgClient.entityLinking("E:\\project\\brain-lenovo-sdk\\static\\kg-chinese.txt")
    return data



if __name__ == '__main__':
    print(invokeRelationshipExtractionService())
    print(invokeEntityLinkingService())