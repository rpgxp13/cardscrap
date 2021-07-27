import requests
from app import data_process as dp
from typing import OrderedDict


class Scrap:
    def __init__(self, uid, password, from_date, to_date):
        self.uid = uid
        self.password = password
        self.from_date = from_date
        self.to_date = to_date

        self.session = requests.session()

    def __str__(self):
        return f''

    def login(self):
        pass

    def scrap(self):
        pass


class SemPlus(Scrap):
    def login(self):
        url_login = "https://semplus.kisvan.co.kr/login/login.do"

        print (self.uid, self.password)
        res = self.session.post(url_login, json=dp.get_userinfo(self.uid, self.password))
        self.session.cookies.get_dict()
        res.raise_for_status()

    def scrap(self):
        page_index = 1

        url_selectCreditTranList = "https://semplus.kisvan.co.kr/management/TranLstMng/selectCreditTranList.do"

        result = {'status': 200, 'data': []}
        while True:
            res = self.session.post(url_selectCreditTranList,
                                    json=dp.get_search_info(self.from_date, self.to_date, page_index))
            res.raise_for_status()

            if 'rNum' in res.text:
                for data in res.json()['data']:
                    result['data'].append(data)

                page_index += 1
            else:
                break

        return result


class VanKICC(Scrap):
    def login(self):
        pass

    def scrap(self):
        pass
