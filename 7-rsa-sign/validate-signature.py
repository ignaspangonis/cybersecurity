from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256

# Provided RSA key components
n = 5203971627599977702699893453803526816601943734900957352050408695934626640230526355547842182479670011732715372606519739120233260028068377783870721704081039
e = 65537
d = 1219900454931084081458999696824443939811948389448455190191043666869763173075656810757914259394254735517079867842674042002425423790222061314519263081010249

# Construct the RSA key using PyCryptodome
rsa_key = RSA.construct((n, e, d))

# Read the contents of "certificate.txt" and compute the SHA-256 fingerprint
with open("sertifikatas.txt", "rb") as f:
    certificate_data = f.read()

# Hash the certificate data using SHA-256
hash_object = SHA256.new(certificate_data)
certificate_fingerprint = hash_object.digest()

# Print the SHA-256 fingerprint in hexadecimal format
print("Certificate fingerprint (SHA-256):", certificate_fingerprint.hex())

# Example signature obtained during signing (replace with actual signature from signing process)
signature_integer = 2152045062986991171981839626864416788210461628852199868780557585359957140543372855259358138334435664725534593088348579744995294406207947473678939590285693

# Decrypt the signature using the public exponent to retrieve the signed hash
decrypted_fingerprint_integer = pow(signature_integer, e, n)

# Convert the decrypted integer back to bytes
decrypted_fingerprint = decrypted_fingerprint_integer.to_bytes((decrypted_fingerprint_integer.bit_length() + 7) // 8, byteorder="big")

# Verify by comparing the decrypted fingerprint to the expected hash
if decrypted_fingerprint == certificate_fingerprint:
    print("Signature is valid.")
else:
    print("Signature is invalid.")
