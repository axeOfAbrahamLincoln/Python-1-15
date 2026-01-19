import caesar_art 

print(caesar_art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


        

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    # for org_letter in original_text:
    #     shifted_position = alphabet.index(org_letter) + shift_amount
    #     if shifted_position >= len(alphabet):
    #         encrypted_text += alphabet[shifted_position-len(alphabet)]
    #     else:
    #         encrypted_text += alphabet[shifted_position]
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position = shifted_position % len(alphabet)
            encrypted_text += alphabet[shifted_position]
    
    print(f"Encrypted word is: {encrypted_text}")


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shift_amount
        decrypted_text += alphabet[shifted_position]
    
    print(f"Decrypted word is: {decrypted_text}")

def caesar(coding):
    if coding == "encode":
        encrypt(text,shift)
    elif coding == "decode":
        decrypt(text,shift)

is_end = False
while not is_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction)
    is_continue = input("Do you wan to continue?(Y/N):").lower()
    if is_continue == "n":
        is_end = True







