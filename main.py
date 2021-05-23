import winsound
import time

MORSE_CODE = {'A': '.-', 'B': '-...',
              'C': '-.-.', 'D': '-..', 'E': '.',
              'F': '..-.', 'G': '--.', 'H': '....',
              'I': '..', 'J': '.---', 'K': '-.-',
              'L': '.-..', 'M': '--', 'N': '-.',
              'O': '---', 'P': '.--.', 'Q': '--.-',
              'R': '.-.', 'S': '...', 'T': '-',
              'U': '..-', 'V': '...-', 'W': '.--',
              'X': '-..-', 'Y': '-.--', 'Z': '--..',
              '1': '.----', '2': '..---', '3': '...--',
              '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.',
              '0': '-----', ',': '--..--', '.': '.-.-.-',
              '?': '..--..', '/': '-..-.', '-': '-....-',
              '(': '-.--.', ')': '-.--.-', ' ': '/'}


# ------------------------Encode English Text to Morse Code String--------------------------

def encode(to_encode):
    encrypted_text = ''
    for letter in to_encode:
        encrypted_text += MORSE_CODE[f"{letter}"]
        encrypted_text += ' '
    return encrypted_text


# ------------------------Translate Morse Code String to Sounds---------------------------------

def code_to_sound(code_string):
    for char in code_string:
        if char == '/':
            time.sleep(0.420)
        elif char == ' ':
            time.sleep(0.60)
        elif char == '-':
            winsound.Beep(900, 180)
            time.sleep(0.060)
        elif char == '.':
            winsound.Beep(900, 60)
            time.sleep(0.060)


def run():
    text_to_encode = input("Enter your message in English: \n")
    dot_dash_string = encode(text_to_encode.upper())
    print(f'Your message in Morse Code is: \n{dot_dash_string}')
    code_to_sound(dot_dash_string)
    run_again = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if run_again == 'yes':
        run()
    if run_again == 'no':
        print('Goodbye')
        quit()


print('Welcome to the English to Morse Code translator!')
run()
