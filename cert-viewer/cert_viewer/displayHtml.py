import json
import os

def displayHtmlFromCertificateJson(jsoncertificate):
    fileDir = os.path.dirname(os.path.realpath('__file__'))
    filename = os.path.join(fileDir, "cert_data/"+jsoncertificate+".json")
    with open(filename) as f:
    	data = json.load(f)
    print(data['displayHtml'])
    return data['displayHtml']
