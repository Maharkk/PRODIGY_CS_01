# Prodigy Infotech

## Caesar Cipher Implementation

This repository contains a Python implementation of the Caesar Cipher algorithm. The Caesar Cipher is a substitution cipher that shifts each letter in the plaintext by a fixed number of places down the alphabet.

### Task Overview

The project includes a Python program that can:
- **Encrypt**: Convert plaintext into ciphertext by shifting each letter by a specified value.
- **Decrypt**: Revert ciphertext back into plaintext using the same shift value.

### Features

- **Encryption**: Allows users to input a message and a shift value to produce the encrypted text.
- **Decryption**: Allows users to input the encrypted text and shift value to retrieve the original message.
- **User Interaction**: A simple menu-driven interface to choose between encryption, decryption, or exit.

### Usage

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Maharkk/PRODIGY_CS_01.git
    cd prodigy-infotech
    ```

2. **Run the program**:
    ```bash
    python caesar_cipher.py
    ```

3. **Follow the prompts** to either encrypt or decrypt a message.

### Code Explanation

- **Encrypt Function**: Shifts each letter of the input text by the given shift value, wrapping around the alphabet if necessary.
- **Decrypt Function**: Reverses the shift operation to return the original text.


