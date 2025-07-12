import os

def get_file_content(filepath):
    with open(filepath, "rb") as f:
        return f.read()

def save_encrypted_file(original_path, encrypted_data, extension):
    os.makedirs("output", exist_ok=True)
    filename = os.path.basename(original_path)
    new_path = os.path.join("output", filename + extension)
    with open(new_path, "wb") as f:
        f.write(encrypted_data)
    print(f"Encrypted file saved as: {new_path}")
