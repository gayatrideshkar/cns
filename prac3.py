import numpy as np

def mod_inverse(matrix, modulus):
    """
    Compute the modular inverse of a matrix.
    """
    determinant = int(round(np.linalg.det(matrix)))  # Determinant of the matrix
    determinant_mod = determinant % modulus
    determinant_inv = pow(determinant_mod, -1, modulus)  # Modular inverse of determinant

    # Adjugate matrix (transpose of cofactor matrix)
    adjugate_matrix = np.round(np.linalg.inv(matrix) * determinant).astype(int) % modulus
    inverse_matrix = (determinant_inv * adjugate_matrix) % modulus

    return inverse_matrix

def text_to_numbers(text):
    """Convert text to numbers (A=0, B=1, ..., Z=25)."""
    return [ord(char) - ord('A') for char in text.upper() if char.isalpha()]

def numbers_to_text(numbers):
    """Convert numbers (0-25) back to text."""
    return ''.join(chr(num + ord('A')) for num in numbers)

def encrypt(text, key_matrix):
    """Encrypt the text using the Hill cipher and a given key matrix."""
    text_numbers = text_to_numbers(text)

    # Padding to match the size of the key matrix
    n = key_matrix.shape[0]
    if len(text_numbers) % n != 0:
        text_numbers += [0] * (n - len(text_numbers) % n)

    text_matrix = np.array(text_numbers).reshape(-1, n).T
    encrypted_matrix = np.dot(key_matrix, text_matrix) % 26

    encrypted_text = numbers_to_text(encrypted_matrix.T.flatten())
    return encrypted_text

def decrypt(encrypted_text, key_matrix):
    """Decrypt the text using the Hill cipher and a given key matrix."""
    encrypted_numbers = text_to_numbers(encrypted_text)

    n = key_matrix.shape[0]
    encrypted_matrix = np.array(encrypted_numbers).reshape(-1, n).T

    inverse_key_matrix = mod_inverse(key_matrix, 26)
    decrypted_matrix = np.dot(inverse_key_matrix, encrypted_matrix) % 26

    decrypted_text = numbers_to_text(decrypted_matrix.T.flatten())
    return decrypted_text

def main():
    print("Hill Cipher Implementation")

    # Example key matrix (3x3)
    key_matrix = np.array([
        [6, 24, 1],
        [13, 16, 10],
        [20, 17, 15]
    ])

    plaintext = input("Enter plaintext: ").replace(" ", "").upper()
    encrypted_text = encrypt(plaintext, key_matrix)
    print(f"Encrypted Text: {encrypted_text}")

    decrypted_text = decrypt(encrypted_text, key_matrix)
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
