from logging import log
import config

class __xmlReq:
    def __init__(self, reqest):
        self.reqtype = reqest.get('reqtype')
        self.login = reqest.get('login')
        self.person_inn = reqest.get('person_inn')
        self.person_first_name = reqest.get('first_name')
        self.person_last_name = reqest.get('last_name')
        self.middle_name = reqest.get('middle_name')
        self.person_birthday = reqest.get('birthday')
        self.identity_card_series = reqest.get('icard_series')
        self.identity_card_number = reqest.get('icard_number')
        self.identity_card_issue_date = reqest.get('icard_issue_date')
        self.identity_card_issuer = reqest.get('icard_issuer')
        self.identity_card_type = reqest.get('icard_type')
        self.contact_address = reqest.get('contact_address')
        self.contact_zip_code = reqest.get('contact_zip_code')
        self.contact_city = reqest.get('contact_city')
        self.contact_area = reqest.get('contact_area')
        self.contact_district = reqest.get('contact_district')
        self.contact_kladr_code = reqest.get('contact_kladr_code')
        self.contact_email = reqest.get('contact_email')
        self.contact_fax = reqest.get('contact_fax')
        self.contact_phone = reqest.get('contact_phone')
        self.contract_doc_number = reqest.get('contact_doc_number')
        self.contract_open_date = reqest.get('contact_open_date')
        self.contract_payment_activation = reqest.get('contact_payment_activation')
        self.contract_otp_phone = reqest.get('contact_otp_phone')
        self.bank_bic = reqest.get('bank_bic')
        self.bank_bic_type = reqest.get('bank_bic_type')
        self.bank_inn = reqest.get('bank_inn')
        self.bank_account_number = reqest.get('bank_account_number')
        self.bank_name = reqest.get('bank_name')
        self.document_rights_doc_type = reqest.get('docrights_doc_type')
        self.document_rights_create = reqest.get('docrights_create')
        self.document_rights_sign_level = reqest.get('docrights_sign_level')
        self.account_number = reqest.get('account_number')
        self.account_name = reqest.get('account_name')
        self.account_first_signs_count = reqest.get('account_first_signs_count')
        self.account_open_date = reqest.get('account_open_date')
        self.account_rights_account_number = reqest.get('account_rights_account_number')
        self.account_rights_statement_request = reqest.get('accrights_statement_request')
        self.account_rights_payment_create = reqest.get('accrights_payment_create')
        self.account_rights_payment_sign_level = reqest.get('accrights_payment_sign_level')
        self.account_rights_exchange_debit_create = reqest.get('accrights_exchange_debit_create')
        self.account_rights_exchange_debit_sign_level = reqest.get('accrights_exchange_debit_sign_level')
        self.account_rights_exchange_credit_create = reqest.get('accrights_exchange_credit_create')
        self.account_rights_exchange_credit_sign_level = reqest.get('accrights_exchange_credit_sign_level')
        
        

# формирование элементов xml
    def login(login):
        text = '<reg:login>{}</reg:login>'.format(login)
        return text

    def person(inn='',fname='',lname='',mname='',birthday=''):
        text = '<reg:person '
        if inn: text += 'inn="' + inn + '" '
        if fname: text += 'first-name="' + fname + '" '
        if lname: text += 'last-name="' + lname + '" '
        if mname: text += 'middle-name="' + mname + '" '
        if birthday: text += 'birthday="' + birthday + '" '
        text += '>'
        return text

    def card(series='',number='',issuedate='',issuer='',ictype=''):
        text = '<reg:identity-card '
        if series: text += 'series="' + series + '" '
        if number: text += 'number="' + number + '" '
        if issuedate: text += 'issue-date="' + issuedate + '" '
        if issuer: text += 'issuer="' + issuer + '" '
        if ictype: text += 'type="' + ictype + '" '
        text += '/>'
        return text
    
    def contact(address='',zipcode='',city='',
                 area='',district='',kladrcode='',
                 email='',fax='',phone=''):
        text = '<reg:contacts '
        if address: text += 'address="' + address + '" '
        if zipcode: text += 'zip-code="' + zipcode + '" '
        if city: text += 'city="' + city + '" '
        if area: text += 'area="' + area + '" '
        if district: text += 'district="' + district + '" '
        if kladrcode: text += 'kladr-code="' + kladrcode + '" '
        if email: text += 'email="' + email + '" '
        if fax: text += 'fax="' + fax + '" '
        if phone: text += 'phone="' + phone + '" '
        text += '/>'
        return text

    def cantract(docnum='',opendate='',payactiv='',otphone=''):
        text = '<reg:contract '
        if docnum: text += 'doc-number="' + docnum + '" '
        if opendate: text += 'open-date="' + opendate + '" '
        if payactiv: text += 'payment-activation="' + payactiv + '" '
        if otphone: text += 'otp-phone="' + otphone + '" '
        text += '>'
        return text

    def accrights(accnomber):
        text = '<reg:account-rights account-number="{0}" statement-request="false" \
                payment-create="true" payment-sign-level="1" exchange-debit-create="true" \
                exchange-debit-sign-level="1" exchange-credit-create="true" \
                exchange-credit-sign-level="1" />'.format(accnomber)
        return text

    def docrights():
        text = '<reg:document-rights doc-type="free-document" \
                create="true" sign-level="1" />'
        return text

    def bank(bic='',bictype='',inn='',accnumber='',name=''):
        text = '<reg:bank '
        if bic: text += 'bic="' + bic + '" '
        if bictype: text += 'bic-type="' + bictype + '" '
        if inn: text += 'inn="' + inn + '" '
        if accnumber: text += 'account-number="' + accnumber + '" '
        if name: text += 'name="' + name + '" '
        text += '/>'
        return text

    def account(number='',name='',firstsignscount='',opendate=''):
        text = '<reg:account '
        if number: text += 'number="' + number + '" '
        if name: text += 'name="' + name + '" '
        if firstsignscount: text += 'first-signs-count="' + firstsignscount + '" '
        if opendate: text += 'open-date="' + opendate + '" '
        text += '>'
        return text
        

    def reqest(filename,text):
        with open(filename,'w', encoding='utf-8') as file:
            file.write(text)

# Формирование запросов

    def resetPass(login):
        text = '<fxg:resetLitePassword xmlns:fxg="http://fxgate.web.cft.ru/registration"> \
                <fxg:login>{0}</fxg:login></fxg:resetLitePassword>'.format(login)
        return text

    def registerContract(data):
        text = '<reg:registerLiteContract xmlns:reg="http://fxgate.web.cft.ru/registration">'
        text += data
        text += '</reg:registerLiteContract>'
        return text



    def completeXMLtext(data):
        text = '<?xml version="1.0"?><S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/"><S:Body>'
        text += data
        text += '</S:Body></S:Envelope>'
        return text

    def createXML(filename,text):
        with open(config.outpath + filename,'w') as file:
            file.write(text)
        



class test:
    def new(add=''):
        text = 'You send «' + add + '»'
        return text
