alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caesar(user_text, shift_direction, encode_or_decode):

    output_text = "" # A variable to store the program's output

    # Reverse shift direction, depending on the user's choice
    if encode_or_decode == "decode":
        shift_direction *= (-1)

    for letter in user_text:
        if not letter in alphabet:
            output_text += letter  # if a letter is not in the list - we just add it, as it is
        else:
            encoded_letter = alphabet.index(letter) + shift_direction # We encrypt/decrypt a letter here
            encoded_letter %= len(alphabet)  # We use modulo to prevent index errors, if encoded_letter's index > alphabet.
            output_text += alphabet[encoded_letter]

    print(f"The {encode_or_decode}d result is: {output_text}")





keep_going = True

while keep_going:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    user_prompt=input("Would you like to keep going? yes/no").lower()

    if user_prompt == "no":
        keep_going = False
        print(f"Vale")
