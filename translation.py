import urllib.request
import json
import os
import sys
apiURL = "https://openapi.naver.com/v1/papago/n2mt"
client_id = "H_PGTxoOcanHVU_PmIHI"
client_secret = "7LPxEe7szR"
encText = input("번역할 문장을 입력하세요 : ")
data = "source=ko&target=en&text=" + encText

requesturl = urllib.request.Request(apiURL)
requesturl.add_header("X-Naver-Client-Id", client_id)
requesturl.add_header("X-Naver-Client-Secret", client_secret)
response = urllib.request.urlopen(requesturl, data = data.encode("utf-8"))
rescode = response.getcode()

if rescode == 200:
    response_body = response.read()
    data = json.loads((response_body.decode('utf-8')))
    print(encText," -> ",data["message"]["result"]["translatedText"])
else:
    print("Error Code :", response)

