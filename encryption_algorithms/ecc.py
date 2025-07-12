from Crypto.PublicKey import ECC
from Crypto.Signature import DSS
from Crypto.Hash import SHA256


def generate_ecc_keypair():
    """
    Generate a new ECC key pair (P-256 curve).
    Returns (private_key_pem_str, public_key_pem_str).
    """
    key = ECC.generate(curve="P-256")
    private_key = key.export_key(format="PEM")
    public_key = key.public_key().export_key(format="PEM")
    return private_key, public_key


def sign_message(private_key_pem, message_bytes):
    """
    Sign the message bytes using the provided private key (PEM string).
    Returns the signature bytes.
    """
    key = ECC.import_key(private_key_pem)
    h = SHA256.new(message_bytes)
    signer = DSS.new(key, "fips-186-3")
    signature = signer.sign(h)
    return signature


def verify_signature(public_key_pem, message_bytes, signature):
    """
    Verify the signature of the message using the public key (PEM string).
    Returns True if valid, False otherwise.
    """
    key = ECC.import_key(public_key_pem)
    h = SHA256.new(message_bytes)
    verifier = DSS.new(key, "fips-186-3")
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False
