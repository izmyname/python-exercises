import string

# get list of all english letters, numbers and punctuation
# punctuation string was inputted manually, because there's a lot of punctuation symbols don't have their morse-code encoding
text = string.ascii_lowercase + string.digits + ".,?'!/()&:;=+-_\"$@ "

# # A list of morse code characters
morse_code = [
    '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
    '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
    '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---',
    '...--', '....-', '.....', '-....', '--...', '---..', '----.', '.-.-.-',
    '--..--', '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-',
    '.-...', '---...', '-.-.-.', '-...-', '.-.-.', '-....-', '..--.-',
    '.-..-.', '...-..-', '.--.-.','/'
]

# create a dictionary
morse_dict = dict(zip(text,morse_code))

morse_message = ""

user_input = input("Please, enter your message. Note, that not all punctuation symbols have their morse-code equivalent. In this case, they'll be ignored: ").lower()

for symbol in user_input:
    try:
        morse_message += morse_dict[symbol]+ ' '
    except KeyError as x:
        print(f"{x} doesn't have morse-code-equivalent, so it'll be ignored")
        continue

print(morse_message)