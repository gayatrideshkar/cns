from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_des(key, plaintext):
    """Encrypt plaintext using DES."""
    cipher = DES.new(key, DES.MODE_ECB)  # Create a DES cipher in ECB mode
    padded_text = pad(plaintext.encode(), DES.block_size)  # Pad the plaintext to match DES block size
    encrypted_text = cipher.encrypt(padded_text)  # Encrypt the plaintext
    return encrypted_text

def decrypt_des(key, encrypted_text):
    """Decrypt ciphertext using DES."""
    cipher = DES.new(key, DES.MODE_ECB)  # Create a DES cipher in ECB mode
    decrypted_text = unpad(cipher.decrypt(encrypted_text), DES.block_size)  # Decrypt and unpad the text
    return decrypted_text.decode()

def main():
    print("DES Algorithm Implementation")

    # Key must be 8 bytes long
    key = input("Enter an 8-character key: ").encode()
    if len(key) != 8:
        print("Error: Key must be exactly 8 characters long.")
        return

    plaintext = input("Enter plaintext: ")

    # Encryption
    encrypted_text = encrypt_des(key, plaintext)
    print(f"Encrypted Text (in bytes): {encrypted_text}")

    # Decryption
    decrypted_text = decrypt_des(key, encrypted_text)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
