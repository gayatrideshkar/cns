from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

class AESAlgorithm:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        # Create AES cipher object
        cipher = AES.new(self.key, AES.MODE_ECB)
        # Pad plaintext to make its length a multiple of the AES block size (16 bytes)
        padded_text = pad(plaintext.encode(), AES.block_size)
        # Encrypt padded plaintext
        encrypted_text = cipher.encrypt(padded_text)
        # Convert encrypted bytes to a hexadecimal string
        return binascii.hexlify(encrypted_text).decode()

    def decrypt(self, ciphertext):
        # Create AES cipher object
        cipher = AES.new(self.key, AES.MODE_ECB)
        # Convert the ciphertext (hexadecimal string) back to bytes
        encrypted_bytes = binascii.unhexlify(ciphertext)
        # Decrypt ciphertext and remove padding
        decrypted_padded_text = cipher.decrypt(encrypted_bytes)
        # Unpad decrypted text and convert it to a string
        return unpad(decrypted_padded_text, AES.block_size).decode()

if __name__ == "__main__":
    key = input("Enter a 16-byte, 24-byte, or 32-byte key: ").encode()

    if len(key) not in [16, 24, 32]:
        print("Key must be 16, 24, or 32 bytes long.")
    else:
        aes = AESAlgorithm(key)

        plaintext = input("Enter the plaintext: ")
        encrypted_text = aes.encrypt(plaintext)
        print("Encrypted Text:", encrypted_text)

        ciphertext = input("\nEnter the cipher text to decrypt: ")
        decrypted_text = aes.decrypt(ciphertext)
        print("Decrypted Text:", decrypted_text)
