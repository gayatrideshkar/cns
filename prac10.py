import hashlib

# Function to hash a message using SHA-256
def sha256_hash(message):
    # Create a new SHA-256 hash object
    sha256 = hashlib.sha256()
    
    # Update the hash object with the bytes of the message
    sha256.update(message.encode('utf-8'))
    
    # Get the hexadecimal representation of the digest
    hash_value = sha256.hexdigest()
    
    return hash_value

if __name__ == "__main__":  # Corrected if condition
    # Input message to be hashed
    message = input("Enter the message to hash using SHA-256: ")
    
    # Get the SHA-256 hash of the message
    hashed_message = sha256_hash(message)
    
    # Output the hashed message
    print(f"SHA-256 Hash: {hashed_message}")
