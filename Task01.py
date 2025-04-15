def caesar_cipher(text, shift, mode):
    result = ""
    for char in text:
        if char.isalpha():
            # Determine the ASCII offset based on uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Calculate the shifted character based on mode
            if mode == "encrypt":
                new_char = chr((ord(char) - offset + shift) % 26 + offset)
            elif mode == "decrypt":
                new_char = chr((ord(char) - offset - shift) % 26 + offset)
            result += new_char
        else:
            # Preserve non-alphabet characters as is
            result += char
    return result



"""
Task 1 Description
Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. 
Allow users to input a message and a shift value to perform encryption and decryption.
"""
# User input
print("CAESAR CIPHER PROGRAM")
mode = input("Choose mode (encrypt/decrypt): ").lower()
text = input("Enter your message: ")
shift = int(input("Enter the Caesar shift value: "))

# Perform encryption or decryption
if mode in ["encrypt", "decrypt"]:
    output = caesar_cipher(text, shift, mode)
    print(f"\nThe {mode}ed message is: {output}")
else:
    print("\nInvalid mode selected. Please choose 'encrypt' or 'decrypt'.")