import os, binascii
webhook_endpoint = (binascii.b2a_hex(os.urandom(30))).decode("utf-8")


VERIFY_TOKEN = (binascii.b2a_hex(os.urandom(25))).decode("utf-8") 

print("webhook_endpoint",webhook_endpoint)
print("VERIFY_TOKEN",VERIFY_TOKEN)

"d8db68392956fcc31d9a91579fa144707d4f8d6f2119d993fcd985509e95"
"98be30d93e2f19a7c2095f8a79b15d9c89f5404232d8076eaf"