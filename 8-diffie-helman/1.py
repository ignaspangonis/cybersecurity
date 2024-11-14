# Given values
g = 3
p = 14012192895561279973
a = 8346435442711077662
b = 3521579192848010622

# Step 1: Calculate A = g^a mod p (Client's public key)
A = pow(g, a, p)

# Step 2: Calculate B = g^b mod p (Server's public key)
B = pow(g, b, p)

# Step 3: Client calculates the shared secret s = B^a mod p
client_secret = pow(B, a, p)

# Step 4: Server calculates the shared secret s = A^b mod p
server_secret = pow(A, b, p)

# Check if both secrets match
shared_secret = client_secret if client_secret == server_secret else None
print(shared_secret)
