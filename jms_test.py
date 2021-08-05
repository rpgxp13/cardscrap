import requests
import json


session = requests.session()

url = "https://jms.jtnet.co.kr"
res = session.post(url)

res.raise_for_status()

login_info = {
    "userCd": "cyw295",
    "password": "tps0707@",
    "tlsVer": "1.3",
    "useOS": "Windows 10 64bit",
    "useBrowser": "Chrome"
}

url = "https://jms.jtnet.co.kr/api/login"
res = session.post(url, json=login_info)

res.raise_for_status()

url = "https://jms.jtnet.co.kr/jsp/main.jsp"
res = session.post(url)

res.raise_for_status()

text = res.text

start_key = "' == '' ? '{}' : '"
end_key = "') );"

start_index = text.find(start_key) + len(start_key)
end_index = text.find(end_key, start_index)

user_info = json.loads(text[start_index:end_index])

businessNumber = user_info['businessNumber']

scrap_info = {
    "dateSel": "T",
    "amountStart": "",
    "amountEnd": "",
    "primaryAccount": "",
    "authority": "",
    "transactionType": "",
    "bankType": "I",
    "cardType": "",
    "ddcFlag": "",
    "dateCheck": "N",
    "orderType": "T",
    "timeStart": "000000",
    "timeEnd": "235959",
    "isEx": "N",
    "tranStart": "20210803",
    "tranEnd": "20210803",
    "bank": "",
    "businessNumber": businessNumber,
    "siteId": "",
    "authFlag": "N",
    "gmAuthFlag": "N",
    "g1": "45",
    "g2": "",
    "g3": "",
    "domainCode": "",
    "massRowsYn": "",
    "pageNumber": "1",
    "pageSize": "100",
    "totalCount": "0",
    "mode": "PAGE"
}
url = "https://jms.jtnet.co.kr/action/tr/selectTrCard"
res = session.post(url, data=scrap_info)

res.raise_for_status()

res_json = json.loads(res.text)

result = json.loads(res_json['result'])

for data in result['list']:
    print(data)
