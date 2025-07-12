from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    padding_length = 16 - len(data) % 16
    return data + bytes([padding_length]) * padding_length

def encrypt(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data))
    return base64.b64encode(cipher.iv + key + ct_bytes)
