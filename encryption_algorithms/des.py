from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    while len(data) % 8 != 0:
        data += b' '
    return data

def encrypt(data):
    key = get_random_bytes(8)
    cipher = DES.new(key, DES.MODE_ECB)
    ct_bytes = cipher.encrypt(pad(data))
    return base64.b64encode(key + ct_bytes)
