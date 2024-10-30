from Crypto.Util import number

p = number.getPrime(256)
q = number.getPrime(256)

n = p * q
phi_n = (p - 1) * (q - 1)
e = 65537

if number.GCD(e, phi_n) != 1:
    raise ValueError("e ir φ(n) turi būti tarpusavyje pirminiai.")

d = pow(e, -1, phi_n)

public_key = (e, n)
private_key = (d, n)

print("p:", p)
print("q:", q)
print("Viešasis raktas (e, n):", public_key)
print("Privatus raktas (d, n):", private_key)
