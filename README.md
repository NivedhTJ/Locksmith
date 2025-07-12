# Locksmith - File Encryption CLI Tool

**Locksmith** is a powerful and extensible command-line tool for encrypting files using multiple cryptographic algorithms. Built with simplicity and modularity in mind, it supports AES, RSA, DES, ChaCha20, ECC signing, and SHA-256 hashing.

> ⚠️ **Disclaimer**: This tool only performs **encryption** or **signing**/**hashing**. Decryption, verification, or file restoration is **not implemented**. You’ll need a separate decryption/verification program.

---

## 📂 Project Structure
Locksmith/
├── encryption_algorithms/
│ ├── aes.py
│ ├── chacha20.py
│ ├── des.py
│ ├── ecc.py
│ ├── rsa.py
│ ├── sha256.py
│ └── __init__.py
├── utils/
│ ├── file_handler.py
│ └── __init__.py
├── main.py
├── requirements.txt
├── .gitignore
└── README.md

## 2. (Optional) Create a virtual environment <br>
python -m venv .venv <br>
source .venv/bin/activate      # On Windows: .venv\Scripts\activate

## 3. Install dependencies <br>
> pip install -r requirements.txt

## 4. Usage <br>
> Run the CLI tool: <br>
> python main.py
