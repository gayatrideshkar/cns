from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad, unpad
import binascii

class BlowfishAlgorithm:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        padded_text = pad(plaintext.encode(), Blowfish.block_size)
        encrypted_text = cipher.encrypt(padded_text)
        return binascii.hexlify(encrypted_text).decode()

    def decrypt(self, ciphertext):
        cipher = Blowfish.new(self.key, Blowfish.MODE_ECB)
        encrypted_bytes = binascii.unhexlify(ciphertext)
        decrypted_padded_text = cipher.decrypt(encrypted_bytes)
        return unpad(decrypted_padded_text, Blowfish.block_size).decode()

if __name__ == "__main__":
    key = input("Enter a key (4 to 56 bytes): ").encode()

    if not (4 <= len(key) <= 56):
        print("Key must be between 4 and 56 bytes long.")
    else:
        blowfish = BlowfishAlgorithm(key)

        plaintext = input("Enter the plaintext: ")
        encrypted_text = blowfish.encrypt(plaintext)
        print("Encrypted Text:", encrypted_text)

        ciphertext = input("\nEnter the cipher text to decrypt: ")
        decrypted_text = blowfish.decrypt(ciphertext)
        print("Decrypted Text:", decrypted_text)
