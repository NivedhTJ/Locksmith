from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes


def encrypt(data):
    key = get_random_bytes(32)
    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(data)
    return cipher.nonce + key + ciphertext


def decrypt(enc_data):
    nonce = enc_data[:8]
    key = enc_data[8:40]
    ciphertext = enc_data[40:]
    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.decrypt(ciphertext)
