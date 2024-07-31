def decrypt(message, key, nonce):
    cipher = ChaCha20.new(key=key, nonce=iv)
    ciphertext = cipher.decrypt(message)
    return ciphertext
