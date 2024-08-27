# HW1a - Substitution Cypher

- Name : Nessa Benavente
- Student ID: 109524187
- Class : CSCI 3412 - Algorithms
- Hw# : 1a
- Due Date : August 27th, 2024

## Description

This program implements a substitution encoder and decoder. The uses a simple encryption technique where each letter in the plaintext is shifted a certain number of places down the alphabet. In this implementation, we use a shift of 3 places.

## Features

- Encode messages using substitution cipher
- Decode messages encrypted with substitution cipher
- Preserves non-alphabetic characters
- Case-sensitive (maintains uppercase and lowercase letters)

## How to Use

1. Run the program.
2. Enter the message you want to encode or decode when prompted.
3. The program will output:
   - The original input message
   - The encoded message
   - The decoded message (which should match the original input)

## Sample Output

```
Input Message: Hello, CSCI 3412 Students!
Encoded Message: Khoor, FVFL 6745 Vwxghqwv!
Decoded Message: Hello, CSCI 3412 Students!
```

## Implementation Details

The program uses the following logic:

- For encoding: Each letter is shifted 3 places forward in the alphabet. For example, 'A' becomes 'D', 'B' becomes 'E', and so on. 'X', 'Y', and 'Z' wrap around to 'A', 'B', and 'C' respectively.
- For decoding: Each letter is shifted 3 places backward in the alphabet. The process is reversed from encoding.
- Non-alphabetic characters (numbers, punctuation, spaces) remain unchanged.
- The program maintains the case of the original letters.

