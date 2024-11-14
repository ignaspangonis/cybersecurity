from sympy import isprime, randprime

def generate_safe_prime(bits):
    while True:
        # Step 1: Generate a random 99-bit prime q
        q = randprime(2**(bits - 2), 2**(bits - 1))

        # Step 2: Calculate p = 2q + 1
        p = 2 * q + 1

        # Step 3: Check if p is prime
        if isprime(p):
            return p

# Generate a 100-bit safe prime p for g = 2
print(generate_safe_prime(100))
