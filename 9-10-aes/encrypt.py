from aes_helpers import (
    byte_string_to_blocks,
    string_to_blocks,
    blocks_to_byte_string,
    aes_encrypt_block,
    add_round_key,
    get_round_keys,
)

# Given data
key = "38e1d0fa257d1a8800865ff4fc2896dd7725f2da24fd0d66aad66e0f80c08efb2178c8945e290500102c7a69914088d75f6326292b7b11bba9ded80f61afc9b4"
plaintext = "pangonis"

# Convert key and plaintext to blocks
round_keys = get_round_keys(key)

plaintext_blocks = string_to_blocks(plaintext)
encrypted_blocks = []

for block in plaintext_blocks:
    encrypted_block = aes_encrypt_block(block, round_keys)
    encrypted_blocks.append(encrypted_block)

cipher_text = blocks_to_byte_string(encrypted_blocks)

print("Encrypted text:", cipher_text) # a99e037fa03de1c2276fcfb72c3eb912

