import code
import logging
import azure.functions as func
from .config import *
from .otp import *
from .credentials import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info(generate_otp(totpSecret))
    code = check_otp(totpSecret,req.params.get('otp'))
    if code:
        return func.HttpResponse(get_credentials(),mimetype="application/json",)
    else:
        return func.HttpResponse(
             "No code received or wrong code",
             status_code=511
        )
