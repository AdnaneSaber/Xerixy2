import os, binascii
webhook_endpoint = (binascii.b2a_hex(os.urandom(30))).decode("utf-8")


VERIFY_TOKEN = (binascii.b2a_hex(os.urandom(25))).decode("utf-8") 

print("webhook_endpoint",webhook_endpoint)
print("VERIFY_TOKEN",VERIFY_TOKEN)

"01e7925bc8e21a3c5b8406e52da5e414465631dd638f24c946e1fe8157f1"
"11f91fcc326dad4d2d3118fc816e0006ffca5c6005b66013f5"