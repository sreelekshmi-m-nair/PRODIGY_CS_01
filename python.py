def caesar_cipher(text, shift, mode):
    result = ""
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char

    return result

def main():
    print("Caesar Cipher Program")
    while True:
        mode = input("Would you like to encrypt or decrypt? (type 'exit' to quit): ").strip().lower()
        if mode == 'exit':
            break
        if mode not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please choose 'encrypt' or 'decrypt'.")
            continue

        text = input("Enter your message: ").strip()
        try:
            shift = int(input("Enter the shift value (integer): ").strip())
        except ValueError:
            print("Please enter a valid integer for the shift value.")
            continue

        result = caesar_cipher(text, shift, mode)
        print(f"The {mode}ed text is: {result}\n")

if __name__ == "__main__":
    main()
