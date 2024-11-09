from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Provided RSA key components
n = 5203971627599977702699893453803526816601943734900957352050408695934626640230526355547842182479670011732715372606519739120233260028068377783870721704081039
e = 65537
d = 1219900454931084081458999696824443939811948389448455190191043666869763173075656810757914259394254735517079867842674042002425423790222061314519263081010249

# Construct the RSA key using PyCryptodome
rsa_key = RSA.construct((n, e, d))

# 1. Read the contents of "certificate.txt" and compute the SHA-256 fingerprint
with open("sertifikatas.txt", "rb") as f:
    certificate_data = f.read()

# Hash the certificate data using SHA-256
hash_object = SHA256.new(certificate_data)
certificate_fingerprint = hash_object.digest()

# bd2c5a048a9ad2a84ca642ec54d2cfa8127a77ffe6c37c40899cd52bea78e14c
print("Certificate fingerprint (SHA-256):", certificate_fingerprint.hex())

signature = pkcs1_15.new(rsa_key).sign(hash_object)
signature_decimal = int.from_bytes(signature, byteorder="big")

# 5039108308966603468380576974529542483524827733370409082009102999394319896579647226303219703527643342770274213880273830554941304391235270078848803943886190
print("Fingerprint signature (decimal):", signature_decimal)
