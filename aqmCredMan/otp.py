import pyotp

def generate_otp(secret):
    return pyotp.TOTP(secret,interval=600).now()
