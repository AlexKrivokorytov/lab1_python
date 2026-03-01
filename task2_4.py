def xor_cipher(message: bytes, key: bytes) -> bytes:
    return bytes(message[i] ^ key[i % len(key)] for i in range(len(message)))


text = "Hello, XOR encryption!"
key = b"python"

b_text = text.encode("utf-8")
encrypted = xor_cipher(b_text, key)
decrypted = xor_cipher(encrypted, key)

print("Original:", text)
print("Decrypted:", decrypted.decode("utf-8"))
print("Test passed:", decrypted == b_text)


with open("xor-message.bin", "rb") as f:
    encrypted_data = f.read()

decrypted_data = xor_cipher(encrypted_data, key)

print("\nDecrypted file message:")
print(decrypted_data.decode("utf-8"))