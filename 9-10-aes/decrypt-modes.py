from aes_helpers import aes_decrypt_block, aes_encrypt_block, get_round_keys, byte_string_to_blocks, blocks_to_string, add_round_key, inverse_shift_rows, inverse_sub_bytes, inverse_mix_columns

def decrypt_ecb(ciphertext_blocks, round_keys):
    decrypted_blocks = []
    for block in ciphertext_blocks:
        decrypted_block = aes_decrypt_block(block, round_keys)
        decrypted_blocks.append(decrypted_block)
    return blocks_to_string(decrypted_blocks)

def decrypt_cbc(ciphertext_blocks, round_keys, iv_block):
    decrypted_blocks = []
    previous_block = iv_block
    for block in ciphertext_blocks:
        decrypted_block = aes_decrypt_block(block, round_keys)
        # XOR with the previous block (or IV for the first block)
        decrypted_block = [[decrypted_block[i][j] ^ previous_block[i][j] for j in range(4)] for i in range(4)]
        decrypted_blocks.append(decrypted_block)
        previous_block = block  # Update the previous block for the next iteration
    return blocks_to_string(decrypted_blocks)

def decrypt_cfb(ciphertext_blocks, round_keys, iv_block):
    decrypted_blocks = []
    feedback_block = iv_block
    for block in ciphertext_blocks:
        encrypted_iv = aes_encrypt_block(feedback_block, round_keys)
        decrypted_block = [[block[i][j] ^ encrypted_iv[i][j] for j in range(4)] for i in range(4)]
        decrypted_blocks.append(decrypted_block)
        feedback_block = block  # Update feedback block for the next iteration
    return blocks_to_string(decrypted_blocks)

def decrypt_ofb(ciphertext_blocks, round_keys, iv_block):
    decrypted_blocks = []
    output_block = iv_block
    for block in ciphertext_blocks:
        output_block = aes_encrypt_block(output_block, round_keys)
        decrypted_block = [[block[i][j] ^ output_block[i][j] for j in range(4)] for i in range(4)]
        decrypted_blocks.append(decrypted_block)
    return blocks_to_string(decrypted_blocks)

def decrypt_pcbc(ciphertext_blocks, round_keys, iv_block):
    decrypted_blocks = []
    previous_ciphertext_block = iv_block

    for block in ciphertext_blocks:
        decrypted_block = aes_decrypt_block(block, round_keys)
        decrypted_block = [[decrypted_block[i][j] ^ previous_ciphertext_block[i][j] for j in range(4)] for i in range(4)]
        decrypted_blocks.append(decrypted_block)
        previous_ciphertext_block = [[decrypted_block[i][j] ^ block[i][j] for j in range(4)] for i in range(4)]

    return blocks_to_string(decrypted_blocks)

# Prepare the key and IV
key = bytes.fromhex("b9e1bda83ece19bdbc18daa37475083ea4213a2dc20a1ea098bd976ca7358386bf598b6c14041b1821eed13053b33e7792c693c306c62b6d78f79c1e991c5abf")
iv = bytes.fromhex("fa3d7f0d39904df393d46cb368a16752")
iv_block = byte_string_to_blocks(iv.hex())[0]

# Prepare round keys
round_keys = get_round_keys(key.hex())

# Ciphertexts as provided
ciphertexts = [
    "7d6e72ccbc4c037b5475e68cf4ec6428d56a92886dd4322a9169789ccf42aaf7074f93d82006edbb54614a801b6ee74da8392c4ce23a2f8a86302a52e4523eb3",
    "f4983cd522cb1b0f5bbed132a1e915f532555e4bdb0a2a40122d82f5591e42fa621e90781dcd62fc7eff19f5ebcb57bf8b8750f5893326673c91a9c78ee37e9a",
    "f1d898facf84ae96f91e4a5ea15b3eff9d02ce54fde979a040a9ad1c2ff23c4693dcf56d14c995e4d0b74f92995f13c1",
    "62b94377173cb94f4003209af62755a6803d09fc54c803dff6421f3842916dbb489961e53aaaf9a525eb8b21cbc942764a024af1ae3b4e4fce2c3b0313244d78",
    "62bf4679bad7e05e0f158d71b13a10edce53dca0febe832dfcbbf8fdcd5f78e3c1d349dc1424ac937881bb3599866a5c329ae7c8ffb41bfc0054a90043444bbbc96c3ff3c3983fcf3d276dd5b7094a7e107f852c125ba5b41e865dc948dbe43a"
]

# Convert ciphertexts to blocks
ciphertext_blocks = [byte_string_to_blocks(ct) for ct in ciphertexts]

# Decrypt each mode
plaintext_ecb = decrypt_ecb(ciphertext_blocks[0], round_keys)
plaintext_cbc = decrypt_cbc(ciphertext_blocks[1], round_keys, iv_block)
plaintext_pcbc = decrypt_pcbc(ciphertext_blocks[2], round_keys, iv_block)
plaintext_cfb = decrypt_cfb(ciphertext_blocks[3], round_keys, iv_block)
plaintext_ofb = decrypt_ofb(ciphertext_blocks[4], round_keys, iv_block)

# Display the decrypted plaintexts
print("AES-EBC atviras tekstas:", plaintext_ecb)
print("AES-CBC atviras tekstas:", plaintext_cbc)
print("AES-PCBC atviras tekstas:", plaintext_pcbc)
print("AES-CFB atviras tekstas:", plaintext_cfb)
print("AES-OFB atviras tekstas:", plaintext_ofb)

