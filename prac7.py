import random

class DiffieHellman:
    def __init__(self, p, g):
        self.p = p  # large prime number
        self.g = g  # primitive root modulo p (base)
    
    def generate_private_key(self):
        # Private key: a large random number
        return random.randint(1, self.p - 1)
    
    def generate_public_key(self, private_key):
        # Public key = g^private_key mod p
        return pow(self.g, private_key, self.p)
    
    def generate_shared_secret(self, received_public_key, private_key):
        # Shared secret = received_public_key^private_key mod p
        return pow(received_public_key, private_key, self.p)

if __name__ == "__main__":
    # Publicly shared prime (p) and base (g)
    p = 23  # A small prime number for demonstration (should be a large prime in practice)
    g = 5   # A primitive root modulo 23

    print(f"Publicly shared values: p = {p}, g = {g}")

    # Create Diffie-Hellman objects for two parties (Alice and Bob)
    alice = DiffieHellman(p, g)
    bob = DiffieHellman(p, g)

    # Generate private keys for Alice and Bob
    alice_private_key = alice.generate_private_key()
    bob_private_key = bob.generate_private_key()

    print(f"\nAlice's Private Key: {alice_private_key}")
    print(f"Bob's Private Key: {bob_private_key}")

    # Generate public keys to exchange
    alice_public_key = alice.generate_public_key(alice_private_key)
    bob_public_key = bob.generate_public_key(bob_private_key)

    print(f"\nAlice's Public Key (sent to Bob): {alice_public_key}")
    print(f"Bob's Public Key (sent to Alice): {bob_public_key}")

    # Generate shared secret keys
    alice_shared_secret = alice.generate_shared_secret(bob_public_key, alice_private_key)
    bob_shared_secret = bob.generate_shared_secret(alice_public_key, bob_private_key)

    print(f"\nAlice's Shared Secret: {alice_shared_secret}")
    print(f"Bob's Shared Secret: {bob_shared_secret}")

    # The shared secret keys should match
    if alice_shared_secret == bob_shared_secret:
        print("\nKey exchange successful! Both parties have the same shared secret.")
    else:
        print("\nKey exchange failed! The shared secrets do not match.")
