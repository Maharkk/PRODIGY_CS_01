# Caesar Cipher Implementation

# Function to encrypt the text
def encrypt(text_to_encrypt, shift):
    # Initialize an empty string to store the encrypted text
    encrypted_text = ""
    
    # Loop through each character in the input text
    for char in text_to_encrypt:
        # Check if the character is alphabetic (i.e., a letter)
        if char.isalpha():
            # Determine if the letter is uppercase or lowercase
            base_ascii = 65 if char.isupper() else 97
            # Shift the letter by the provided value, wrapping around using modulo 26
            encrypted_char = chr((ord(char) - base_ascii + shift) % 26 + base_ascii)
            # Add the encrypted character to the result string
            encrypted_text += encrypted_char
        else:
            # If the character is not a letter, add it unchanged
            encrypted_text += char
    
    # Return the final encrypted text
    return encrypted_text

# Function to decrypt the text
def decrypt(cipher_text, shift):
    # Initialize an empty string to store the decrypted text
    decrypted_text = ""
    
    # Loop through each character in the cipher text
    for char in cipher_text:
        # Check if the character is alphabetic (i.e., a letter)
        if char.isalpha():
            # Determine if the letter is uppercase or lowercase
            base_ascii = 65 if char.isupper() else 97
            # Reverse the shift by subtracting the provided shift value
            decrypted_char = chr((ord(char) - base_ascii - shift) % 26 + base_ascii)
            # Add the decrypted character to the result string
            decrypted_text += decrypted_char
        else:
            # If the character is not a letter, add it unchanged
            decrypted_text += char
    
    # Return the final decrypted text
    return decrypted_text

# Main program to handle user input
if __name__ == "__main__":
    print("Caesar Cipher Program")  # Display program title
    
    # Loop to keep the program running until the user chooses to exit
    while True:
        # Ask the user to choose between encrypting, decrypting, or exiting
        option = input("Choose an option: (1) Encrypt (2) Decrypt (3) Exit: ")
        
        # If the user chooses to encrypt
        if option == "1":
            # Get the text and shift value from the user
            text_to_encrypt = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            # Call the encrypt function and display the result
            encrypted_text = encrypt(text_to_encrypt, shift)
            print(f"Encrypted text: {encrypted_text}\n")
        
        # If the user chooses to decrypt
        elif option == "2":
            # Get the cipher text and shift value from the user
            cipher_text = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            # Call the decrypt function and display the result
            decrypted_text = decrypt(cipher_text, shift)
            print(f"Decrypted text: {decrypted_text}\n")
        
        # If the user chooses to exit the program
        elif option == "3":
            print("Exiting the program.")  # Display exit message
            break  # Exit the loop and end the program
        
        # If the user enters an invalid option
        else:
            print("Invalid option. Please choose 1, 2, or 3.")  # Display error message
