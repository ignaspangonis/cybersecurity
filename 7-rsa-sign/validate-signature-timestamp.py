from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256
import time

# Provided RSA key components
n = 5203971627599977702699893453803526816601943734900957352050408695934626640230526355547842182479670011732715372606519739120233260028068377783870721704081039
e = 65537
d = 1219900454931084081458999696824443939811948389448455190191043666869763173075656810757914259394254735517079867842674042002425423790222061314519263081010249

rsa_key = RSA.construct((n, e, d))

with open("sertifikatas.txt", "rb") as f:
    certificate_data = f.read()

cert_hash = SHA256.new(certificate_data).digest()

# Assume we have the original timestamp used during signing
ts10 = 1731238953

ts16 = ts10.to_bytes(16, byteorder='big')

combined_data = cert_hash + ts16
expected_combined_fingerprint = SHA256.new(combined_data).digest()

# Assume we have the signature (an integer) obtained from signing
signature_integer = 2651775735771644812897410277597513785230405288825608513777864522909028902649947232745493534845445807198494188059874334169973374500344715588272541290695197

decrypted_fingerprint_integer = pow(signature_integer, e, n)
decrypted_fingerprint = decrypted_fingerprint_integer.to_bytes((decrypted_fingerprint_integer.bit_length() + 7) // 8, byteorder='big')

if decrypted_fingerprint == expected_combined_fingerprint:
    print("Signature is valid.")
else:
    print("Signature is invalid.")
