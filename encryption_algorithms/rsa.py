from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def encrypt(data):
    key = RSA.generate(2048)
    public_key = key.publickey()
    cipher = PKCS1_OAEP.new(public_key)
    encrypted = cipher.encrypt(data[:190])  # RSA limit for small files only
    return base64.b64encode(encrypted)