import code
import logging
import azure.functions as func

import pyotp

def generate_otp(secret):
    return pyotp.totp.TOTP(secret,interval=600).now()

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    code = generate_otp("")
    if code:
        return func.HttpResponse(f"Code: {code}")
    else:
        return func.HttpResponse(
             "No Code received",
             status_code=200
        )
