from flask import request
#Imported custom script to retrieve display on template the "displayHtml" field of the certificate
from cert_viewer import displayHtml

def award(certificate_uid):
    requested_format = request.args.get('format', None)
    if requested_format == 'json':
        return get_award_json(certificate_uid)
    from . import cert_store, certificate_formatter
    award, verification_info = certificate_formatter.get_formatted_award_and_verification_info(cert_store,
                                                                                               certificate_uid)
    #The added line of code
    displayHtmlData = displayHtml.displayHtmlFromCertificateJson(certificate_uid)
    return {'award': award,
            'verification_info': verification_info, 'displayHtml': displayHtmlData}


def get_award_json(certificate_uid):
    from . import cert_store
    certificate_json = cert_store.get_certificate_json(certificate_uid)
    return certificate_json
