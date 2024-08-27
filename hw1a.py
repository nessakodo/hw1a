import string

def shift_char(char, shift):
    if char.isalpha():
        # Determine the ASCII offset based on whether it's uppercase or lowercase
        offset = ord('A') if char.isupper() else ord('a')
        # Apply the shift and wrap around using modulo
        return chr((ord(char) - offset + shift) % 26 + offset)
    elif char.isdigit():
        # Shift digits and wrap around 0-9
        return str((int(char) + shift) % 10)
    else:
        # Return non-alphanumeric characters as is
        return char

def create_shift_substitutions(n):
    encoding = {char: shift_char(char, n) for char in string.ascii_letters + string.digits}
    decoding = {v: k for k, v in encoding.items()}
    return encoding, decoding

def encode(message, subst):
    return ''.join(subst.get(char, char) for char in message)

def decode(message, subst):
    return encode(message, subst)

def main():
    while True:
        try:
            n = int(input("Enter a shift value (1-25): "))
            if 1 <= n <= 25:
                break
            else:
                print("Shift value must be between 1 and 25. Please enter a different number.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 25.")

    encoding, decoding = create_shift_substitutions(n)
    message = input("Enter the message to encode: ")
    encoded_message = encode(message, encoding)
    print(f"Encoded message: {encoded_message}")
    decoded_message = decode(encoded_message, decoding)
    print(f"Decoded message: {decoded_message}")

if __name__ == "__main__":
    main()