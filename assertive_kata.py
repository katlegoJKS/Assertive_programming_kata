MORSE_CODE_DICT = {
    'A':'.-', 'B':'-...', 'C':'-.-.',
    'D':'-..', 'E':'.', 'F':'..-.',
    'G':'--.', 'H':'....', 'I':'..',
    'J':'.---', 'K':'-.-', 'L':'.-..',
    'M':'--', 'N':'-.', 'O':'---',
    'P':'.--.', 'Q':'--.-', 'R':'.-.',
    'S':'...', 'T':'-', 'U':'..-',
    'V':'...-', 'W':'.--', 'X':'-..-',
    'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----',
    ', ':'--..--', '.':'.-.-.-', '?':'..--..',
    '/':'-..-.', '-':'-....-',  '(':'-.--.',
    ')':'-.--.-'
    }

def encrypt_to_morse_code(text):
    morse_code = ' '
    for letter in text:
        if letter != ' ':
            morse_code += MORSE_CODE_DICT[letter] + ' '
        else:
            morse_code += ' /'
    return morse_code

def decrypt_to_text(text):
    text += ' '
    decrypt = ''
    encrypted_text = ''
    for letter in text:
        if (letter != ' '):
            counter = 0
            encrypted_text += letter
        else:
            counter += 1
            if counter == 2:
                decrypt += ' '
            else:
                decrypt += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(encrypted_text)]
                encrypted_text = ''
    return decrypt
    

if __name__ == "__main__":
    text = "Hi there"
    cipher = encrypt_to_morse_code(text.upper())
    assert len(text) != 0, 'You cannot encrypt a blank text'
    print("Original message: ",text)
    print("Message in Morse Code: ",cipher)
    print("Message length: ",len(text))
  
    morse_code = ".... ..  - .... . .-. ."
    text_length =list(morse_code.split(' '))
    cipher = decrypt_to_text(morse_code)
    assert len(morse_code) != 0, 'You cannot decrypt a blank text'
    print("\nMorse Code:", morse_code)
    print("Message in plain text:", cipher)
    print("Message length: {}".format(len(text_length)))