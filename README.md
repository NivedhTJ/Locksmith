# Locksmith - File Encryption CLI Tool

**Locksmith** is a command-line tool for encrypting files using multiple cryptographic algorithms. Built with simplicity and modularity in mind, it supports AES, RSA, DES, ChaCha20, ECC signing, and SHA-256 hashing.

> ⚠️ **Disclaimer**: This tool only performs **encryption** or **signing**/**hashing**. Decryption, verification, or file restoration is **not implemented**. You’ll need a separate decryption/verification program.

---

## 📂 Project Structure

```
Locksmith/
├── encryption_algorithms/
│ ├── __init__.py
│ ├── aes.py
│ ├── chacha20.py
│ ├── des.py
│ ├── ecc.py
│ ├── rsa.py
│ └── sha256.py
├── utils/
│ ├── __init__.py
│ └── file_handler.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## 2. (Optional) Create a virtual environment <br>
```bash
python -m venv .venv

# Activate the environment
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate # windows cmd
```

## 3. Install dependencies
```bash
pip install -r requirements.txt
```

## 4. Usage <br>
``` bash
# Run the CLI tool
python main.py
```

## Output
- Encrypted/Hashed/Signed files are saved in an output/ folder created automatically.

- The original input file is never deleted or modified.
