import gmpy2

c = 38173844545078129948288269399042027
e = 3
n = 57978193340973369297108562701043535531241438035929130357155046000278533026851

# This decryption works only if m^e < n
if c >= n:
    raise ValueError("The assumption m^e < n is not satisfied.")

# Calculate the e-th root of c to determine m
m = gmpy2.iroot(c, e)[0]

try:
    message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
except ValueError:
    message = m

print("Decrypted Message (numeric):", m)
print("Decrypted Message (original):", message)
