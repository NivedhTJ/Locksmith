from Crypto.Hash import SHA256


def hash(data):
    h = SHA256.new()
    h.update(data)
    return h.digest()


def hash_hex(data):
    h = SHA256.new()
    h.update(data)
    return h.hexdigest()
