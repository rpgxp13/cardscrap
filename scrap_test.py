import requests

session = requests.session()

uid = '197116'
password = 'tpays0507*'

userInfo = {'userInfo': {
    "userId": uid,
    "pwd": password,
    "randomNum": "",
    "secCode": "",
    "secCardNo": "",
    "resultCode": "",
    "certNo": ""
}}

url = "https://kcs.koces.com/main/welcome.do"
res = session.post(url)
res.raise_for_status()

startKey = "<input type=\"hidden\" id=\"csrf\" name=\"csrf\" value=\""
endKey = "\"/>"

startIndex = res.text.find(startKey) + len(startKey)
endIndex = res.text.find(endKey, startIndex)

csrf = res.text[startIndex:endIndex]

userInfo = {
    "id": uid,
    "password": password,
    "csrf": csrf
}

url = "https://kcs.koces.com/main/login.do"
res = session.post(url, data=userInfo)
res.raise_for_status()

scrap_data = {
    "curMenuId": "363",
    "curMenuNm": "%BD%C5%BF%EB%C7%F6%B1%DD%C6%F7%C0%CE%C6%AE_%BD%C5%BF%EB%C4%AB%B5%E5",
    "sUserId": uid,
    "sDateFlag": "day",
    "sDateType": "2",
    "sDateFrom": "20210728",
    "sDateTo": "20210730",
    "sMonthFrom": "201809",
    "sMonthTo": "201809",
    "sFlag1": "0",
    "sFlag20": "N",
    "pageSize": "10000000",
    "pageNo": "1",
    "totalCnt": "10000000",
    "tableId": "list1",
    "sMode": "ED"
}

url = "https://kcs.koces.com/html/trst/auth/saleAuth/cardAuth/getList.do"
res = session.post(url, data=scrap_data)
res.raise_for_status()

print(res.text)
