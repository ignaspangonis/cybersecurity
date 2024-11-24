import time
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# Provided RSA key components
n = 5203971627599977702699893453803526816601943734900957352050408695934626640230526355547842182479670011732715372606519739120233260028068377783870721704081039
e = 65537
d = 1219900454931084081458999696824443939811948389448455190191043666869763173075656810757914259394254735517079867842674042002425423790222061314519263081010249

rsa_key = RSA.construct((n, e, d))

with open("sertifikatas.txt", "rb") as f:
    certificate_data = f.read()

cert_hash = SHA256.new(certificate_data).digest().hex()

ts10 = int(time.time()) # For example, 1732392922
print("Timestamp (ts10):", ts10)

ts_hex = f"{ts10:x}"

combined_data = cert_hash + ts_hex
combined_fingerprint = SHA256.new(bytes.fromhex(combined_data)).digest()

print("Certificate and timestamp fingerprint (SHA-256):", combined_fingerprint.hex())

combined_fingerprint_integer = int.from_bytes(combined_fingerprint, byteorder="big")
signature_integer = pow(combined_fingerprint_integer, d, n)

print("Certificate and timestamp fingerprint signature (decimal):", signature_integer)
