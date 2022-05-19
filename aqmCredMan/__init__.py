import code
import logging
import azure.functions as func
from .config import *
from .otp import *

def main(req: func.HttpRequest) -> func.HttpResponse:
    code = check_otp(totpSecret,req.params.get('otp'))
    if code:
        return func.HttpResponse(f"Code: {code}")
    else:
        return func.HttpResponse(
             "No Code received",
             status_code=511
        )
