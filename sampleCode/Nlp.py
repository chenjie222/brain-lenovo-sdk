########### Python 3.6 #############
from aip.AiNlpClient import AipNlpClinet

def invokeChineseSentimentAnalysisService():
    """
    chinese Sentiment Analysis
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.chineseSentimentAnalysis("E:\\project\\brain-lenovo-sdk\\static\\NLP-sentiment.txt")
    return data

def invokeWordSegmentationService():
    """
    word Segmentation
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.wordSegmentation("E:\\project\\brain-lenovo-sdk\\static\\Nlp-stanadford")
    return data


def invokePartTaggingService():
    """
    part Tagging
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.partTagging("E:\\project\\brain-lenovo-sdk\\static\\Nlp-stanadford")
    return data

def invokeLemmatizationService():
    """
    lemmatization
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.lemmatization("E:\\project\\brain-lenovo-sdk\\static\\Nlp-stanadford")
    return data

def invokeNamedEntityService():
    """
    named Entity Recognition
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.namedEntityRecognition("E:\\project\\brain-lenovo-sdk\\static\\Nlp-stanadford")
    return data


def invokeParsingService():
    """
    parsing
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.parsing("E:\\project\\brain-lenovo-sdk\\static\\Nlp-stanadford")
    return data


def invokeRelationshipExtractionService():
    """
    relationship Extraction
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.relationshipExtraction("E:\\project\\brain-lenovo-sdk\\static\\Nlp-stanadford")
    return data


def invokeCoreferenceResolutionService():
    """
    coreference Resolution
    """
    YourAccessKey = "939B81BBD7805575685FDE0FBEB15D1D"
    YoursecretKey = "339B81BBD7805575685FDE0FBEB15D11"
    NlpClient = AipNlpClinet(YourAccessKey,YoursecretKey)
    # faceDetection，传入文件、文件path、json对象、dict、bytes、string、均可返回AI result
    data = NlpClient.coreferenceResolution("E:\\project\\brain-lenovo-sdk\\static\\Nlp-stanadford")
    return data

if __name__ == '__main__':
    print(invokeChineseSentimentAnalysisService())
    print(invokeWordSegmentationService())
    print(invokePartTaggingService())
    print(invokeLemmatizationService())
    print(invokeNamedEntityService())
    print(invokeParsingService())
    print(invokeRelationshipExtractionService())
    print(invokeCoreferenceResolutionService())
