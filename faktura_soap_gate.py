outputFolder = 'C:\\System\\WorkBench\\ubs-faktura-sync\\'

class __xmlReq:
    def __init__(self):
        pass

    def login(login):
        text = '<reg:login>{}</reg:login>'.format(login)
        return text
    
    def contacts(address='',zipcode='',city='',
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

    def card(series='',number='',issuedate='',issuer='',ictype=''):
        text = '<reg:identity-card '
        if series: text += 'series="' + series + '" '
        if number: text += 'number="' + number + '" '
        if issuedate: text += 'issue-date="' + issuedate + '" '
        if issuer: text += 'issuer="' + issuer + '" '
        if ictype: text += 'type="' + ictype + '" '
        text += '/>'
        return text

    def resetPass(login):
        text = '<fxg:resetLitePassword xmlns:fxg="http://fxgate.web.cft.ru/registration"> \
                <fxg:login>{0}</fxg:login></fxg:resetLitePassword>'.format(login)
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



class test:
    def new(add=''):
        text = 'You send «' + add + '»'
        return text
