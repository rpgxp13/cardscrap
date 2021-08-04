
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


def get_kicc_login_form(uid, password):
    post_data = {
        "gv_ssoId": uid,
        "gv_ssoPw": password,
        "gv_ssoPathGbn": "https://www.easyshop.co.kr/taxLogn/taxLognLogin.kicc?nextURL=https://www.easyshop.co.kr/taxMain/taxMain.kicc"
    }

    return post_data


def get_login_do_xml(uid, password, wmonid):
    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<Root xmlns="http://www.nexacroplatform.com/platform/dataset">'
    xml += '    <Parameters>'
    xml += '	    <Parameter id="LoginInfo" />'
    xml += '	    <Parameter id="WMONID">' + wmonid + '</Parameter>'
    xml += '	    <Parameter id="arg_pgmId">Login</Parameter>'
    xml += '	    <Parameter id="nMbr_id">undefined</Parameter>'
    xml += '    </Parameters>'
    xml += '    <Dataset id="dsInData">'
    xml += '	    <ColumnInfo>'
    xml += '		    <Column id="SvcId" type="STRING" size="256"  />'
    xml += '		    <Column id="gubun" type="STRING" size="2"  />'
    xml += '		    <Column id="login_id" type="STRING" size="20"  />'
    xml += '		    <Column id="pswd" type="STRING" size="50"  />'
    xml += '		    <Column id="ctz_no" type="STRING" size="13"  />'
    xml += '		    <Column id="ip_addr" type="STRING" size="23"  />'
    xml += '		    <Column id="cert_dn" type="STRING" size="408"  />'
    xml += '		    <Column id="otp_login_cd" type="STRING" size="1"  />'
    xml += '		    <Column id="otpYn" type="STRING" size="256"  />'
    xml += '		    <Column id="txtID" type="STRING" size="256"  />'
    xml += '		    <Column id="txtOtp" type="STRING" size="256"  />'
    xml += '	    </ColumnInfo>'
    xml += '	    <Rows>'
    xml += '		    <Row>'
    xml += '			    <Col id="SvcId">TCMM100S01</Col>'
    xml += '			    <Col id="gubun">3</Col>'
    xml += '			    <Col id="login_id">' + uid + '</Col>'
    xml += '			    <Col id="pswd">' + password + '</Col>'
    xml += '			    <Col id="ctz_no" />'
    xml += '			    <Col id="ip_addr" />'
    xml += '			    <Col id="cert_dn" />'
    xml += '			    <Col id="otp_login_cd" />'
    xml += '		    </Row>'
    xml += '	    </Rows>'
    xml += '   </Dataset>'
    xml += '</Root>'

    xml = xml.encode('utf-8')

    return xml


def get_call_service_do_xml(wmonid, mbr_id, from_date, to_date):
    xml = '<?xml version="1.0" encoding="UTF-8"?>'
    xml += '<Root xmlns="http://www.nexacroplatform.com/platform/dataset">'
    xml += '	<Parameters>'
    xml += '		<Parameter id="LoginInfo" />'
    xml += '		<Parameter id="WMONID">' + wmonid + '</Parameter>'
    xml += '		<Parameter id="arg_pgmId">div_Work</Parameter>'
    xml += '		<Parameter id="nMbr_id">' + mbr_id + '</Parameter>'
    xml += '	</Parameters>'
    xml += '	<Dataset id="dsInData">'
    xml += '		<ColumnInfo>'
    xml += '			<Column id="SvcId" type="STRING" size="256"  />'
    xml += '			<Column id="user_id" type="STRING" size="256"  />'
    xml += '			<Column id="aut_id" type="STRING" size="256"  />'
    xml += '			<Column id="func_cd" type="STRING" size="256"  />'
    xml += '			<Column id="gubun" type="STRING" size="256"  />'
    xml += '			<Column id="retrv_dt01" type="STRING" size="256"  />'
    xml += '			<Column id="retrv_dt02" type="STRING" size="256"  />'
    xml += '			<Column id="bizr_no" type="STRING" size="256"  />'
    xml += '			<Column id="tid" type="STRING" size="256"  />'
    xml += '			<Column id="aprv_no" type="STRING" size="256"  />'
    xml += '			<Column id="cardno" type="STRING" size="256"  />'
    xml += '			<Column id="iss_fm_nm" type="STRING" size="256"  />'
    xml += '			<Column id="purch_fm_nm" type="STRING" size="256"  />'
    xml += '			<Column id="fin_org_cd" type="STRING" size="256"  />'
    xml += '			<Column id="jo_shop_no" type="STRING" size="256"  />'
    xml += '			<Column id="tot_trx_amt" type="STRING" size="256"  />'
    xml += '			<Column id="tot_trx_amt2" type="STRING" size="256"  />'
    xml += '			<Column id="s_alot_months_cnt" type="STRING" size="256"  />'
    xml += '			<Column id="s_alot_months_cnt2" type="STRING" size="256"  />'
    xml += '			<Column id="trx_tm" type="STRING" size="256"  />'
    xml += '			<Column id="trx_tm2" type="STRING" size="256"  />'
    xml += '			<Column id="trx_can_cl_cd" type="STRING" size="256"  />'
    xml += '			<Column id="trx_resp_cd" type="STRING" size="256"  />'
    xml += '			<Column id="oil" type="STRING" size="256"  />'
    xml += '			<Column id="fromPageNo" type="STRING" size="256"  />'
    xml += '			<Column id="endPageNo" type="STRING" size="256"  />'
    xml += '			<Column id="remk" type="STRING" size="256"  />'
    xml += '			<Column id="remk2" type="STRING" size="256"  />'
    xml += '			<Column id="remk_1" type="STRING" size="256"  />'
    xml += '			<Column id="remk_2" type="STRING" size="256"  />'
    xml += '			<Column id="trx_typ" type="STRING" size="256"  />'
    xml += '			<Column id="cardno2" type="STRING" size="256"  />'
    xml += '			<Column id="max_no" type="STRING" size="256"  />'
    xml += '			<Column id="itm_tit2" type="STRING" size="256"  />'
    xml += '			<Column id="itm_sz" type="STRING" size="256"  />'
    xml += '			<Column id="itm_fmt" type="STRING" size="256"  />'
    xml += '			<Column id="itm_mode" type="STRING" size="256"  />'
    xml += '			<Column id="itm_align" type="STRING" size="256"  />'
    xml += '			<Column id="sql_con" type="STRING" size="256"  />'
    xml += '			<Column id="sql_alias" type="STRING" size="256"  />'
    xml += '			<Column id="gid" type="STRING" size="256"  />'
    xml += '			<Column id="card_typ_flag" type="STRING" size="256"  />'
    xml += '		</ColumnInfo>'
    xml += '		<Rows>'
    xml += '			<Row>'
    xml += '				<Col id="SvcId">TESS103S01</Col>'
    xml += '				<Col id="func_cd">3</Col>'
    xml += '				<Col id="gubun">0</Col>'
    xml += '				<Col id="retrv_dt01">' + from_date + '</Col>'
    xml += '				<Col id="retrv_dt02">' + to_date + '</Col>'
    xml += '				<Col id="bizr_no">*</Col>'
    xml += '				<Col id="tid">*</Col>'
    xml += '				<Col id="purch_fm_nm">*</Col>'
    xml += '				<Col id="trx_resp_cd">0000</Col>'
    xml += '				<Col id="fromPageNo">0</Col>'
    xml += '				<Col id="endPageNo">1000000</Col>'
    xml += '				<Col id="remk">0000</Col>'
    xml += '				<Col id="cardno2" />'
    xml += '				<Col id="sql_con">NVL(trx_natr_no,&#39;&#32;&#39;)&#32;as&#32;trx_natr_no,&#32;NVL(trx_can_cl_cd,&#39;&#32;&#39;)&#32;as&#32;trx_can_cl_cd,&#32;NVL(slip_no,&#39;&#32;&#39;)&#32;as&#32;slip_no,&#32;NVL(case&#32;when&#32;trx_resp_cd=&#39;0000&#39;&#32;and&#32;trx_can_cl_cd&#32;not&#32;in&#32;(&#39;0&#39;,&#32;&#39;7&#39;)&#32;then&#32;&#39;통신취소&#39;&#32;when&#32;ifm_typ_cd=&#39;0100&#39;&#32;and&#32;trx_resp_cd=&#39;0000&#39;&#32;and&#32;trx_can_yn=&#39;C&#39;&#32;then&#32;&#39;승인원거래&#39;&#32;when&#32;ifm_typ_cd=&#39;0200&#39;&#32;and&#32;trx_resp_cd=&#39;0000&#39;&#32;and&#32;trx_can_yn=&#39;C&#39;&#32;then&#32;&#39;취소원거래&#39;&#32;when&#32;m_gd_cd=&#39;LC&#39;&#32;then&#32;&#39;조회&#39;&#32;when&#32;trx_resp_cd!=&#39;0000&#39;&#32;then&#32;&#39;거절&#39;&#32;when&#32;ifm_typ_cd=&#39;0100&#39;&#32;then&#32;&#39;승인&#39;&#32;when&#32;ifm_typ_cd=&#39;0200&#39;&#32;and&#32;trx_resp_cd=&#39;0000&#39;&#32;and&#32;trx_cl_cd=&#39;TI&#39;&#32;then&#32;&#39;전화취소&#39;&#32;when&#32;ifm_typ_cd=&#39;0200&#39;&#32;and&#32;trx_resp_cd=&#39;0000&#39;&#32;and&#32;trx_dt&lt;&gt;orgnl_aprv_dt&#32;then&#32;&#39;전일취소&#39;&#32;when&#32;ifm_typ_cd=&#39;0200&#39;&#32;then&#32;&#39;취소&#39;&#32;when&#32;ifm_typ_cd&#32;is&#32;null&#32;then&#32;&#39;&#32;&#39;&#32;end,&#39;&#32;&#39;)&#32;as&#32;ifm_typ_cd,&#32;NVL(trx_dt||trx_tm,&#39;&#32;&#39;)&#32;as&#32;trx_dtm,&#32;NVL(nvl(tid,&#32;&#39;&#32;&#39;),&#39;&#32;&#39;)&#32;as&#32;tid,&#32;NVL(cardno,&#39;&#32;&#39;)&#32;as&#32;cardno,&#32;NVL(decode(nvl(card_typ_flag,&#39;N&#39;),&#32;&#39;Y&#39;,&#32;&#39;체크&#39;,&#39;G&#39;,&#39;기프트&#39;,&#39;신용&#39;),&#39;&#32;&#39;)&#32;as&#32;card_typ_cd,&#32;NVL(iss_fm_nm,&#39;&#32;&#39;)&#32;as&#32;iss_fm_nm,&#32;NVL(GET_FIN_ORG_NM(&#39;F01&#39;,&#32;purch_fm_cd),&#39;&#32;&#39;)&#32;as&#32;purch_fm_nm,&#32;NVL(jo_shop_no,&#39;&#32;&#39;)&#32;as&#32;jo_shop_no,&#32;case&#32;when&#32;ifm_typ_cd=&#39;0200&#39;&#32;and&#32;trx_resp_cd=&#39;0000&#39;&#32;and&#32;aut_yn&#32;=&#32;&#39;Y&#39;&#32;then&#32;nvl(-tot_trx_amt,0)&#32;else&#32;nvl(tot_trx_amt,0)&#32;end&#32;as&#32;tot_trx_amt,&#32;NVL(case&#32;when&#32;alot_months_cnt=&#39;0&#39;&#32;then&#32;&#39;일시불&#39;&#32;when&#32;to_char(alot_months_cnt)&#32;&lt;&gt;&#32;&#39;0&#39;&#32;then&#32;alot_months_cnt||&#39;개월&#39;&#32;else&#32;to_char(alot_months_cnt)&#32;end,&#39;&#32;&#39;)&#32;as&#32;alot_months_cnt,&#32;NVL(aprv_no,&#39;&#32;&#39;)&#32;as&#32;aprv_no,&#32;NVL(decode(trx_mthd_cd,&#32;&#39;2&#39;,&#32;&#39;Y&#39;,&#32;&#39;K&#39;,&#32;&#39;Y&#39;,&#32;&#39;N&#39;),&#39;&#32;&#39;)&#32;as&#32;trx_mthd_cd,&#32;NVL(decode(trim(orgnl_aprv_dt),&#32;&#39;20&#39;,&#32;&#39;&#39;,&#32;&#39;&#39;,&#32;&#39;&#39;,&#32;&#39;000000&#39;,&#32;&#39;&#39;,&#32;&#39;00000000&#39;,&#32;&#39;&#39;,&#32;&#39;20000000&#39;,&#32;&#39;&#39;,&#32;decode(substr(orgnl_aprv_dt,&#32;7,&#32;1),&#32;&#39;&#39;,&#32;&#39;20&#39;||orgnl_aprv_dt,&#32;orgnl_aprv_dt)),&#39;&#32;&#39;)&#32;as&#32;orgnl_aprv_dt,&#32;NVL(DECODE(HNDL_ST_DTL_CD,&#39;60&#39;,PAY_PLAN_DT,&#39;63&#39;,PAY_PLAN_DT,&#39;66&#39;,PAY_PLAN_DT,&#39;67&#39;,PAY_PLAN_DT,NULL),&#39;&#32;&#39;)&#32;as&#32;pay_plan_dt,&#32;NVL(get_com_cd_nm(&#39;TRN_C00002&#39;,&#32;trx_resp_cd),&#39;&#32;&#39;)&#32;as&#32;trx_resp_cd,&#32;NVL(decode(btr_sign_chk_2(mkr_cd,&#32;etc_sign_flag,&#32;purch_fm_cd,&#32;trx_resp_cd,&#32;tat_ddc_flag,&#32;tat_edc_flag,&#32;tat_dcc_rgst_cd),&#32;0,&#32;&#39;Y&#39;,&#32;DECODE&#32;(trm_typ_cd,&#32;&#39;MS&#39;,&#32;&#39;Y&#39;,&#39;N&#39;)),&#39;&#32;&#39;)&#32;as&#32;sign_yn</Col>'
    xml += '				<Col id="sql_alias">trx_natr_no||&#39;@@&#39;||trx_can_cl_cd||&#39;@@&#39;||slip_no||&#39;@@&#39;||ifm_typ_cd||&#39;@@&#39;||trx_dtm||&#39;@@&#39;||tid||&#39;@@&#39;||cardno||&#39;@@&#39;||card_typ_cd||&#39;@@&#39;||iss_fm_nm||&#39;@@&#39;||purch_fm_nm||&#39;@@&#39;||jo_shop_no||&#39;@@&#39;||tot_trx_amt||&#39;@@&#39;||alot_months_cnt||&#39;@@&#39;||aprv_no||&#39;@@&#39;||trx_mthd_cd||&#39;@@&#39;||orgnl_aprv_dt||&#39;@@&#39;||pay_plan_dt||&#39;@@&#39;||trx_resp_cd||&#39;@@&#39;||sign_yn</Col>'
    xml += '				<Col id="card_typ_flag">*</Col>'
    xml += '			</Row>'
    xml += '		</Rows>'
    xml += '	</Dataset>'
    xml += '</Root>'

    xml = xml.encode('utf-8')

    return xml


def get_member_id(text):
    startKey = "<Col id=\"mbr_id\">"
    endKey = "</Col>"

    startIndex = text.find(startKey) + len(startKey)
    endIndex = text.find(endKey, startIndex)

    return text[startIndex:endIndex]
