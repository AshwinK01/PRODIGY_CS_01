def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    choice = input("Do you want to (e)ncrypt or (d)ecrypt? ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice, please choose 'e' for encryption or 'd' for decryption.")
        return

    text = input("Enter the text: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        result = caesar_encrypt(text, shift)
    else:
        result = caesar_decrypt(text, shift)
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()
