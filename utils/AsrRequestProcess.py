import re
import json
import base64
import json
def checkJsonFormat(raw_msg):
    """
    判断字符串是不是json对象
    """
    if isinstance(raw_msg, str):  # 判断是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False


def processRequest(option,rate):
    data_json = {}
    if type(option).__name__ == 'str':
        # 如果传音频文件path
        if re.findall(r'([^<>/\\\|:""\*\?]+\.\w+$)', option) :
            try:
                with open(option, "rb") as f:
                    byte_data = f.read()
            except IOError:
                print("error:The file was not found or read failed")
                return
            base64_data = base64.b64encode(byte_data).decode()

            data_dict = {
                'sampleRate': rate,
                "bit":16,
                "base64Data": base64_data
            }
            data_json = json.dumps(data_dict)

        # 如果上传jsonobject
        if checkJsonFormat(option):
            data_json = option

    # 如果传byte
    if type(option).__name__ == 'bytes':
        base64_data = base64.b64encode(option).decode()
        data_dict = {
            'sampleRate': rate,
            "bit": 16,
            "base64Data": base64_data
        }
        data_json = json.dumps(data_dict)

    #如果上传dict
    if type(option).__name__ == 'dict' :
        data_json = json.dumps(option)


    return data_json

