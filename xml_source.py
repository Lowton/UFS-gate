bank_xml = """<reg:bank bic="043678783" bic-type="ru" inn="6323066377"
        account-number="30101810100000000783"
        name="АО ''РТС-Банк''" />"""

contract_xml = """<?xml version="1.0"?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
  <S:Body>
    <reg:registerLiteContract xmlns:reg="http://fxgate.web.cft.ru/registration">
      <reg:login>{login}</reg:login>
      <reg:person
        inn="{inn}" first-name="{first_name}" last-name="{last_name}"
        middle-name="{middle_name}" birthday="{birthday}">
        <reg:identity-card
          series="{serial}" number="{doc_num}" issue-date="{doc_date}"
          issuer="{doc_dept}" type="{doc_type}" />
        <reg:contacts
          address="{address}" zip-code="{index}" city="{city}"
          email="{email}"phone="{phone}" />
      </reg:person>
      <reg:contract doc-number="{contract_num}" doc-date="contract_date"
                    payment-activation="true" otp-phone="{phone}">
        {bank}
        <reg:document-rights doc-type="free-document" create="true" sign-level="1" />
      </reg:contract>
    </reg:registerLiteContract>
  </S:Body>
</S:Envelope>"""

account_xml = """<?xml version="1.0"?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
  <S:Body>
    <reg:registerAccount xmlns:reg="http://fxgate.web.cft.ru/registration">
      <reg:login>{login}</reg:login>
      <reg:account number="{acc}" name="{acc}"
      open-date="{acc_data}" first-signs-count="1">
        {bank}
      </reg:account>
      <reg:account-rights
        account-number="{acc}" statement-request="false"
        payment-create="true" payment-sign-level="1"
        exchange-debit-create="true" exchange-debit-sign-level="1"
        exchange-credit-create="true" exchange-credit-sign-level="3" />
    </reg:registerAccount>
  </S:Body>
</S:Envelope>"""

card_xml = """<?xml version="1.0"?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
  <S:Body>
    <reg:registerCards xmlns:reg="http://fxgate.web.cft.ru/registration">
      <reg:account number="{acc}" first-signs-count="1">
        {bank}
      </reg:account>
      <!--1 or more repetitions:-->
      <reg:card number="{card}" name="VISA тестовая карта" type="VPS"
                expiration-date="{card_date}" card-account-number="{rbs}"
                payment-system="{ps}" card-product-code="{card_code}"/>
    </reg:registerCards>
  </S:Body>
</S:Envelope>"""
