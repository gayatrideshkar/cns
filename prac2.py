class Playfair:
    def __init__(self, key, plaintext):
        self.key = key.lower()
        self.plaintext = plaintext.lower()
        self.matrix = [['' for _ in range(5)] for _ in range(5)]

    def clean_playfair_key(self):
        # Remove duplicates while preserving order
        new_key = ""
        for char in self.key:
            if char not in new_key:
                new_key += char
        self.key = new_key

    def generate_cipher_key(self):
        # Generate the key matrix
        set_chars = set()
        for char in self.key:
            if char != 'j':
                set_chars.add(char)

        temp_key = self.key
        for i in range(26):
            ch = chr(i + 97)
            if ch != 'j' and ch not in set_chars:
                temp_key += ch

        idx = 0
        for i in range(5):
            for j in range(5):
                self.matrix[i][j] = temp_key[idx]
                idx += 1

        print("Playfair Cipher Key Matrix:")
        for row in self.matrix:
            print(row)

    def format_plaintext(self):
        # Format the plaintext
        message = ""
        for char in self.plaintext:
            if char == 'j':
                message += 'i'
            else:
                message += char

        i = 0
        while i < len(message):
            if i + 1 < len(message) and message[i] == message[i + 1]:
                message = message[:i + 1] + 'x' + message[i + 1:]
            i += 2

        if len(message) % 2 == 1:
            message += 'x'

        return message

    def form_pairs(self, message):
        # Split the message into pairs
        return [message[i:i + 2] for i in range(0, len(message), 2)]

    def get_char_pos(self, ch):
        # Get position of character in matrix
        for i in range(5):
            for j in range(5):
                if self.matrix[i][j] == ch:
                    return [i, j]
        return None

    def encrypt_message(self):
        # Encrypt the plaintext
        message = self.format_plaintext()
        msg_pairs = self.form_pairs(message)
        enc_text = ""

        for pair in msg_pairs:
            ch1, ch2 = pair
            ch1_pos = self.get_char_pos(ch1)
            ch2_pos = self.get_char_pos(ch2)

            if ch1_pos[0] == ch2_pos[0]:
                enc_text += self.matrix[ch1_pos[0]][(ch1_pos[1] + 1) % 5]
                enc_text += self.matrix[ch2_pos[0]][(ch2_pos[1] + 1) % 5]
            elif ch1_pos[1] == ch2_pos[1]:
                enc_text += self.matrix[(ch1_pos[0] + 1) % 5][ch1_pos[1]]
                enc_text += self.matrix[(ch2_pos[0] + 1) % 5][ch2_pos[1]]
            else:
                enc_text += self.matrix[ch1_pos[0]][ch2_pos[1]]
                enc_text += self.matrix[ch2_pos[0]][ch1_pos[1]]

        return enc_text

    def decrypt_message(self, cipher_text):
        # Decrypt the ciphertext
        msg_pairs = self.form_pairs(cipher_text)
        dec_text = ""

        for pair in msg_pairs:
            ch1, ch2 = pair
            ch1_pos = self.get_char_pos(ch1)
            ch2_pos = self.get_char_pos(ch2)

            if ch1_pos[0] == ch2_pos[0]:
                dec_text += self.matrix[ch1_pos[0]][(ch1_pos[1] - 1 + 5) % 5]
                dec_text += self.matrix[ch2_pos[0]][(ch2_pos[1] - 1 + 5) % 5]
            elif ch1_pos[1] == ch2_pos[1]:
                dec_text += self.matrix[(ch1_pos[0] - 1 + 5) % 5][ch1_pos[1]]
                dec_text += self.matrix[(ch2_pos[0] - 1 + 5) % 5][ch2_pos[1]]
            else:
                dec_text += self.matrix[ch1_pos[0]][ch2_pos[1]]
                dec_text += self.matrix[ch2_pos[0]][ch1_pos[1]]

        return dec_text


if __name__ == "__main__":
    key = input("Enter the key: ")
    plaintext = input("Enter the plaintext: ")
    
    pfc = Playfair(key, plaintext)
    pfc.clean_playfair_key()
    pfc.generate_cipher_key()
    
    enc_text = pfc.encrypt_message()
    print("Encrypted Text:", enc_text)

    cipher_text = input("\nEnter the cipher text to decrypt: ")
    
    decryption_pfc = Playfair(key, "")
    decryption_pfc.clean_playfair_key()
    decryption_pfc.generate_cipher_key()
    
    dec_text = decryption_pfc.decrypt_message(cipher_text)
    print("Decrypted Text:", dec_text)
