from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# Provided RSA key components
n = 5203971627599977702699893453803526816601943734900957352050408695934626640230526355547842182479670011732715372606519739120233260028068377783870721704081039
e = 65537
d = 1219900454931084081458999696824443939811948389448455190191043666869763173075656810757914259394254735517079867842674042002425423790222061314519263081010249

rsa_key = RSA.construct((n, e, d))

with open("sertifikatas.txt", "rb") as f:
    certificate_data = f.read()

hash_object = SHA256.new(certificate_data)
certificate_fingerprint = hash_object.digest()

print("Certificate fingerprint (SHA-256):", certificate_fingerprint.hex())

hash_integer = int.from_bytes(certificate_fingerprint, byteorder="big")

# signature = hash^d mod n
signature_integer = pow(hash_integer, d, n)

print("Fingerprint signature (decimal):", signature_integer)
