from sympy import isprime
from sympy.ntheory import primerange, factorint
from Crypto.Util.number import inverse

def find_small_prime_factor(n, bit_limit):
    # Adjusted to use factorint for more advanced factorization
    factorization = factorint(n)
    for factor, _ in factorization.items():
        if factor.bit_length() <= bit_limit:
            return factor
    return None

def rsa_decrypt(c, n, e):
    bit_limit = 40
    p = find_small_prime_factor(n, bit_limit)
    if not p:
        raise ValueError("No small prime factor found within the bit limit.")

    q = n // p
    if not isprime(q):
        raise ValueError("Calculated q is not prime.")

    phi_n = (p - 1) * (q - 1)
    d = inverse(e, phi_n)
    m = pow(c, d, n)

    # Convert the decrypted integer message back to bytes/string
    try:
        message = m.to_bytes((m.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
    except ValueError:
        message = m

    return message

c = 90708548149730452313300412903982774660312730771591279987660619811707542185916
e = 65537
n = 99186218111363243410101731962347422165625362610235773539276567172386926970801
message = rsa_decrypt(c, n, e)
print("Decrypted Message:", message)
