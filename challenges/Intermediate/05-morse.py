# Encode Morse

# Create a function that takes a string as an argument and returns the Morse code equivalent.

# Examples
# encode_morse("EDABBIT CHALLENGE") ➞ ". -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. ."
# . -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .
# . -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. 
# . -.. .- -... -... .. -   -.-. .... .- .-.. .-.. . -. --. .

# encode_morse("HELP ME !") ➞ ".... . .-.. .--.   -- .   -.-.--"

# This dictionary can be used for coding:

# char_to_dots = {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }
# Notes:
#  - Ouput should be International Morse Code, and use the standard conventions for symbols 
#    not defined inside the ITU recommendation (see Resources).
#  - Input value can be lower or upper case.
#  - Input string can have digits.
#  - Input string can have some special characters (e.g. comma, colon, apostrophe, period, 
#                                                   question mark, exclamation mark).
#  - One space " " is expected after each character, except the last one.

char_to_dots = {
  'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
  'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
  'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
  'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
  'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
  '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
  '6': '-....', '7': '--...', '8': '---..', '9': '----.',
  '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
  ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
  '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.',
  ' ': ' ' 
}

dots_to_char = {v: k for k, v in char_to_dots.items()}

def encode_morse(message):
    morse_msg = ' '.join([char_to_dots[char] for char in message.upper()])
    return morse_msg

def decode_morse(message):
    
    message = message.split(" ")

    while message.count("")>0:
        message[message.index("")] = " "   

    message =  [dots_to_char[dots] for dots in message if dots!="" ]

    return "".join(message).replace("  "," ")

if __name__ == '__main__':

    print(">>>",encode_morse("EDABBIT CHALLENGE"))
    print(">>>",decode_morse(encode_morse("EDABBIT CHALLENGE")))
