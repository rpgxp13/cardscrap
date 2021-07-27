
def get_userinfo(uid, password):
    userInfo = {'userInfo': {
        "userId": uid,
        "pwd": password,
        "randomNum": "",
        "secCode": "",
        "secCardNo": "",
        "resultCode": "",
        "certNo": ""
    }}
    return userInfo


def get_search_info(from_date, to_date, page_index):
    searchInfo = {'searchInfo': {
        "qKind": "1", "excelYn": "N", "custClsf": "1", "custId": "", "userGubnCode": "MER", "custCnt": "",
        "selKind": "3", "timeGubn": "", "dayGubn": "T", "fromDate": from_date, "fromTime": "00",
        "fromMin": "00", "toDate": to_date, "toTime": "00", "toMin": "00", "crdfiGubn": "1",
        "crdfiCode": "", "custType": "", "custInfo": "", "merchtNo": "", "cardNo": "", "acNo": "",
        "trGubn": "", "cardGubn": "", "fromAmt": "", "toAmt": "", "kisRespCode": "", "ftKind": "1",
        "pageUnit": "", "pageIndex": page_index, "pageSize": "", "yyyy": from_date[:4], "trType": "", "setName": ""
    }}
    return searchInfo
