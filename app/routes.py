from app import app
from flask import request
from app.models import SemPlus
import json


@app.route('/<company>/scrap', methods=['GET'])
def scrap(company: str):
    uid = request.args.get('uid')
    password = request.args.get('password')
    from_date = request.args.get('from-date')
    to_date = request.args.get('to-date')

    if company.lower() == 'semplus':
        card_compay = SemPlus(uid, password, from_date, to_date)
    else:
        return json.dumps({'status': 500, 'data': []})

    card_compay.login()
    result = card_compay.scrap()
    return result

    #return json.dumps({'company': company, 'uid': uid, 'password': password, 'from-date': from_date, 'to-date': to_date})
