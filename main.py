from utils.file_handler import get_file_content, save_encrypted_file
from encryption_algorithms import aes, rsa, des, chacha20, ecc, sha256
import os
import pyfiglet


def show_banner():
    banner = pyfiglet.figlet_format("Locksmith")
    print(banner)


def show_menu():
    print(
        """
Welcome to the File Encryption Tool 
1. AES Encryption
2. RSA Encryption
3. DES Encryption
4. ChaCha20 Encryption
5. ECC Sign
6. SHA-256 Hash
7. Exit
"""
    )
    return input("Choose an option: ")


def main():
    show_banner()

    while True:
        choice = show_menu()

        if choice == "7":
            print("Exiting...")
            break

        filepath = input("Enter the path of the file: ").strip().strip('"').strip("'")
        try:
            data = get_file_content(filepath)
        except FileNotFoundError:
            print("File not found. Please try again.")
            continue

        if choice == "1":  # AES
            encrypted = aes.encrypt(data)
            save_encrypted_file(filepath, encrypted, ".aes")

        elif choice == "2":  # RSA
            priv_key, pub_key = rsa.generate_keys()
            with open("private.pem", "wb") as f:
                f.write(priv_key)
            with open("public.pem", "wb") as f:
                f.write(pub_key)
            encrypted = rsa.encrypt(data, pub_key)
            save_encrypted_file(filepath, encrypted, ".rsa")
            print(
                "RSA keys saved as private.pem and public.pem. Keep private.pem safe!"
            )

        elif choice == "3":  # DES
            encrypted = des.encrypt(data)
            save_encrypted_file(filepath, encrypted, ".des")

        elif choice == "4":  # ChaCha20
            encrypted = chacha20.encrypt(data)
            save_encrypted_file(filepath, encrypted, ".chacha20")

        elif choice == "5":  # ECC Sign
            priv_key, pub_key = ecc.generate_ecc_keypair()
            with open("ecc_private.pem", "wb") as f:
                f.write(priv_key.encode("utf-8"))
            with open("ecc_public.pem", "wb") as f:
                f.write(pub_key.encode("utf-8"))
            signature = ecc.sign_message(priv_key, data)
            save_encrypted_file(filepath, signature, ".eccsig")
            print(
                "ECC keys saved as ecc_private.pem and ecc_public.pem. Keep private key safe!"
            )

        elif choice == "6":  # SHA-256 Hash
            digest = sha256.hash(data)
            save_encrypted_file(filepath, digest, ".sha256")
            print(f"SHA-256 hash saved.")

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
