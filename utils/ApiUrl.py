
class AiUrl():
    # sdk在线获取token接口
    AiOnlineAuthurl = "https://dev-api.brain.lenovo.com/online-authorize"
    #Base Pre Url
    BaseUrl = "https://dev-api.brain.lenovo.com/"
    # Nothing just a extract
    TOKEN = "?token="
    #Version
    VERSION = "/1.6"

    # NLP Word Segmentation Url
    AiNlpSegmentation = BaseUrl + "apicore/nlp/word-segmentation" + VERSION + TOKEN

    # NLP Post of Speech Tagging
    AiNlpPART = BaseUrl + "apicore/nlp/part-of-speech-tagging" + VERSION + TOKEN

    # NLP Lemmatization
    AiNlpLemmatization = BaseUrl + "apicore/nlp/lemmatization" + VERSION + TOKEN

    # NLP Named-Entity-Recognition
    AiNlpNamedEntityRecognition = BaseUrl + "apicore/nlp/named-entity-recognition" + VERSION + TOKEN

    # NLP Parsing
    AiNlpParsing = BaseUrl + "apicore/nlp/parsing" + VERSION + TOKEN

    # NLP Relation Extration
    AiNlpRelationExtration = BaseUrl + "apicore/nlp/relationship-extraction" + VERSION + TOKEN

    # Nlp Conference Resolution
    AiNlpConferenceResolution = BaseUrl + "apicore/nlp/coreference-resolution" + VERSION + TOKEN

    # Nlp Chinese Sentiment Analysis
    Ai_NlpChineseAnalysis = BaseUrl + "apicore/nlp/sentiment-analysis" + VERSION + TOKEN

    # Vision Technologies
    # Object Recognition
    AiVisionObjectRecognition = BaseUrl + "apicore/cv/object-recognition" + VERSION + TOKEN

    # Moblie Recognition
    AiVisionMoblieRecognition = BaseUrl + "apicore/cv/mobile-recognition" + VERSION + TOKEN

    # Scene Recognition
    AiVisionSceneRecognition = BaseUrl + "apicore/cv/scenario-recognition" + VERSION + TOKEN

    # Photo Classification
    AiVisionPhotoClassification = BaseUrl + "apicore/cv/photo-classification" + VERSION + TOKEN

    # Face Detection
    AiVisionFaceDetection = BaseUrl + "apicore/cv/face-detection" + VERSION + TOKEN

    # Face Comparison
    AiVisionFaceComparison = BaseUrl + "apicore/cv/face-comparison" + VERSION + TOKEN

    # Face Attributes Detection
    AiVisionFaceAttr = BaseUrl + "apicore/cv/face-attributes-detection" + VERSION + TOKEN



    # Context Awareness
    # Gonder Detection
    AiCAGenderClassifier = BaseUrl + "/apicore/ca/gender-detection" + VERSION + TOKEN

    # Scene Classification
    AiCASceneClassifier = BaseUrl + "/apicore/ca/scene-classification" + VERSION + TOKEN

    # Ambient Detection
    AiCAAmbientDetection = BaseUrl + "/apicore/ca/ambient-detection" + VERSION + TOKEN

    # Crying Detection
    AiCACryClassifier = BaseUrl + "/apicore/ca/infant-crying-detection" + VERSION + TOKEN

    # Knowledge Graph
    # Relationship Extraction
    AiKGOpenIE = BaseUrl + "/apicore/kg/relationship-extraction" + VERSION + TOKEN

    # Entity Linking
    AiKGAnnotate = BaseUrl + "/apicore/kg/entity-linking" + VERSION + TOKEN


    # Voice Technology
    # automatic speech recognition
    AiVoiceasr = BaseUrl + "/apicore/voice/speech-recognition" + VERSION + TOKEN


