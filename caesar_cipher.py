# Caesar Cipher Implementation

# Function to encrypt the text
def encrypt(text_to_encrypt, shift):
    encrypted_text = ""
    
    for char in text_to_encrypt:
        # Check if the character is alphabetic
        if char.isalpha():
            base_ascii = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - base_ascii + shift) % 26 + base_ascii)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    
    # Return the final encrypted text
    return encrypted_text

# Function to decrypt the text
def decrypt(cipher_text, shift):
    decrypted_text = ""
    
    for char in cipher_text:
        if char.isalpha():
            base_ascii = 65 if char.isupper() else 97
            decrypted_char = chr((ord(char) - base_ascii - shift) % 26 + base_ascii)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    
    # Return the final decrypted text
    return decrypted_text

# Program to handle user input
if __name__ == "__main__":
    print("Caesar Cipher Program")  # Title
    
    while True:
        option = input("Choose an option: (1) Encrypt (2) Decrypt (3) Exit: ")
        
        # If the user chooses to encrypt
        if option == "1":
            text_to_encrypt = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(text_to_encrypt, shift)
            print(f"Encrypted text: {encrypted_text}\n")
        
        # If the user chooses to decrypt
        elif option == "2":
            cipher_text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(cipher_text, shift)
            print(f"Decrypted text: {decrypted_text}\n")
        
        # If the user chooses to exit the program
        elif option == "3":
            print("Exiting the program.")  
            break  
        
        # If the user enters an invalid option
        else:
            print("Invalid option. Please choose 1, 2, or 3.")  
