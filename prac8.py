import random

# Helper function to compute the greatest common divisor
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Helper function to compute the modular inverse
def mod_inverse(e, phi):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y

    g, x, _ = extended_gcd(e, phi)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % phi

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to generate RSA keys
def generate_keys():
    # Choose two prime numbers
    while True:
        p = random.randint(100, 300)
        if is_prime(p):
            break
    while True:
        q = random.randint(100, 300)
        if is_prime(q) and q != p:
            break

    # Compute n = p * q
    n = p * q

    # Compute Euler's totient function φ(n) = (p - 1) * (q - 1)
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
    while True:
        e = random.randint(2, phi - 1)
        if gcd(e, phi) == 1:
            break

    # Compute d such that (e * d) % φ(n) = 1
    d = mod_inverse(e, phi)

    # Public key (e, n) and private key (d, n)
    return (e, n), (d, n)

# Function to encrypt the plaintext
def encrypt(plaintext, public_key):
    e, n = public_key
    # Convert each character to its ASCII value, encrypt using c = (m^e) % n
    cipher = [(ord(char) ** e) % n for char in plaintext]
    return cipher

# Function to decrypt the ciphertext
def decrypt(ciphertext, private_key):
    d, n = private_key
    # Decrypt each character using m = (c^d) % n and convert back to a character
    plain = ''.join([chr((char ** d) % n) for char in ciphertext])
    return plain

if __name__ == "__main__":
    # Generate RSA keys
    public_key, private_key = generate_keys()
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")

    # Get plaintext input
    plaintext = input("\nEnter the plaintext: ")

    # Encrypt the plaintext using the public key
    encrypted_message = encrypt(plaintext, public_key)
    print(f"Encrypted Message: {encrypted_message}")

    # Decrypt the ciphertext using the private key
    decrypted_message = decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")
