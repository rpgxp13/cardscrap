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
    def __init__(self, uid, password, from_date, to_date):
        super().__init__(uid, password, from_date, to_date)

    def login(self):
        url_login = "https://semplus.kisvan.co.kr/login/login.do"
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


class KICC(Scrap):
    def __init__(self, uid, password, from_date, to_date):
        super().__init__(uid, password, from_date, to_date)
        self.wmonid = ""
        self.mbr_id = ""

    def login(self):
        url = "https://smarteasyshop.kicc.co.kr/smart_kicc/index.jsp"
        res = self.session.post(url, data=dp.get_kicc_login_form(self.uid, self.password))
        res.raise_for_status()

        self.wmonid = self.session.cookies.get_dict()['WMONID']

        url = "https://smarteasyshop.kicc.co.kr/login.do"
        res = self.session.post(url, data=dp.get_login_do_xml(self.uid, self.password, self.wmonid))
        res.raise_for_status()

        self.mbr_id = dp.get_member_id(res.text)

    def scrap(self):
        url = "https://smarteasyshop.kicc.co.kr/CallService.do"
        res = self.session.post(url,
                                data=dp.get_call_service_do_xml(self.wmonid, self.mbr_id, self.from_date, self.to_date))
        res.raise_for_status()

        return res.text


class NICE(Scrap):
    def login(self):
        url = "https://newnibs.nicevan.co.kr/"
