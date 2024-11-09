import time
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Provided RSA key components
n = 5203971627599977702699893453803526816601943734900957352050408695934626640230526355547842182479670011732715372606519739120233260028068377783870721704081039
e = 65537
d = 1219900454931084081458999696824443939811948389448455190191043666869763173075656810757914259394254735517079867842674042002425423790222061314519263081010249

rsa_key = RSA.construct((n, e, d))

with open("sertifikatas.txt", "rb") as f:
    certificate_data = f.read()

cert_hash = SHA256.new(certificate_data).digest()

ts10 = int(time.time()) # e.g. 1731160588
print("Timestamp (ts10):", ts10)

ts16 = ts10.to_bytes(16, byteorder='big')

combined_data = cert_hash + ts16
combined_fingerprint = SHA256.new(combined_data).digest()

print("Certificate and timestamp fingerprint (SHA-256):", combined_fingerprint.hex())

signature = pkcs1_15.new(rsa_key).sign(SHA256.new(combined_fingerprint))
signature_decimal = int.from_bytes(signature, byteorder="big")

print("Certificate and timestamp fingerprint signature (decimal):", signature_decimal)
