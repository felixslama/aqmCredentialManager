import pyotp 
from .config import *
def generate_otp(secret):
    return pyotp.totp.TOTP(secret,interval=totpInterval).provisioning_uri(name='AQM', issuer_name='AETHER ENGINEERING')

def check_otp(secret,otp):
    return pyotp.totp.TOTP(secret,interval=totpInterval).verify(otp)