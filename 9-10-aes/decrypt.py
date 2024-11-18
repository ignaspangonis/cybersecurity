from aes_helpers import aes_decrypt_block, get_round_keys, byte_string_to_blocks, blocks_to_string, inverse_shift_rows, inverse_sub_bytes, inverse_mix_columns, add_round_key

# Given data
key = "38e1d0fa257d1a8800865ff4fc2896dd7725f2da24fd0d66aad66e0f80c08efb2178c8945e290500102c7a69914088d75f6326292b7b11bba9ded80f61afc9b4"
cipher_text = "9ddba6bfdd242b8b7929976fda7687d3"

key_blocks = byte_string_to_blocks(key)
state = byte_string_to_blocks(cipher_text)[0]

round_keys = get_round_keys(key)

ciphertext_blocks = byte_string_to_blocks(cipher_text)
decrypted_blocks = []

for block in ciphertext_blocks:
  decrypted_block = aes_decrypt_block(block, round_keys)
  decrypted_blocks.append(decrypted_block)

decrypted_text = blocks_to_string(decrypted_blocks)

print("Decrypted text:", decrypted_text)
