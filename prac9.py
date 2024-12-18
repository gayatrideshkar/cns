from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import binascii

# Generate RSA key pair
def generate_keys():
    key = RSA.generate(1024)  # Reduced key size to 512 bits
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

def sign_message(message, private_key):
    rsa_private_key = RSA.import_key(private_key)
    hash_value = SHA256.new(message.encode('utf-8'))
    signature = pkcs1_15.new(rsa_private_key).sign(hash_value)
    return binascii.hexlify(signature).decode('utf-8')

# Verify the signature
def verify_signature(message, signature, public_key):
    rsa_public_key = RSA.import_key(public_key)
    hash_value = SHA256.new(message.encode('utf-8'))
    signature_bytes = binascii.unhexlify(signature)
    try:
        pkcs1_15.new(rsa_public_key).verify(hash_value, signature_bytes)
        print("Signature is valid!")
    except (ValueError, TypeError):
        print("Signature is invalid!")

if __name__ == "__main__":
    # Generate RSA keys (public and private)
    private_key, public_key = generate_keys()

    print(f"Private Key:\n{private_key.decode('utf-8')}")
    print(f"Public Key:\n{public_key.decode('utf-8')}")

    # Input message
    message = input("\nEnter the message to be signed: ")

    # Sign the message using the private key
    signature = sign_message(message, private_key)
    print(f"\nSignature: {signature}")

    # Verify the signature using the public key
    verify_signature(message, signature, public_key)
