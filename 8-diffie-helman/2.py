import math

# Given values
g = 5
p = 741369009217
x = 546410079593

def baby_step_giant_step(g, x, p):
    # Step 1: Calculate m
    m = math.isqrt(p) + 1

    # Step 2: Compute baby steps and store them in a dictionary
    baby_steps = {}
    for j in range(m):
        baby_step = pow(g, j, p)
        baby_steps[baby_step] = j

    # Step 3: Compute g^(-m) mod p
    g_inv_m = pow(g, -m, p)

    # Step 4: Giant steps to find the match
    giant_step = x
    for i in range(m):
        if giant_step in baby_steps:
            # Solution found
            return i * m + baby_steps[giant_step]
        giant_step = (giant_step * g_inv_m) % p

    return None  # No solution found

print(baby_step_giant_step(g, x, p))
