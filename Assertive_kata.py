code = {'/': ' ', 'a':'.-', 'b':'-...', 
        'c':'-.-.', 'd':'-..', 'e':'.', 
        'f':'..-.', 'g':'--.', 'h':'....', 
        'i':'..', 'j':'.---', 'k':'-.-', 
        'l':'.-..', 'm':'--', 'n':'-.', 
        'o':'---', 'p':'.--.', 'q':'--.-', 
        'r':'.-.', 's':'...', 't':'-', 
        'u':'..-', 'v':'...-', 'w':'.--', 
        'x':'-..-', 'y':'-.--', 'z':'--..', 
        '1':'.----', '2':'..---', '3':'...--', 
        '4':'....-', '5':'.....', '6':'-....', 
        '7':'--...', '8':'---..', '9':'----.', 
        '0':'-----', ', ':'--..--', '.':'.-.-.-', 
        '?':'..--..', '|':'-..-.', '-':'-....-', 
        '(':'-.--.', ')':'-.--.-'}

def letters_to_morse_code(text):
    morse_code = ' '
    for letter in text:
        if letter != ' ':
            morse_code += code[letter] + ' '
        else:
            morse_code += ' /'

    return morse_code

def morse_code_to_letters(text):
    text += ' '
    decrypt = ''
    encrypted_text = ''
    for letter in text:
        if (letter != ' '):
            i = 0
            encrypted_text += letter
        else:
            i += 1
            if i == 2:
                decrypt += ''
            else:
                decrypt += list(code.keys())[list(code.values()).index(encrypted_text)]
                encrypted_text = ''

    return decrypt
    
def cipher_text():
    text = "hi there"
    cipher = letters_to_morse_code(text.lower())
    assert len(text) != 0, 'You cannot encode a blank space'
    print(cipher)
  
    text = ".... . .-.. .-.. ---"
    text_length =list(text.split(' '))
    cipher = morse_code_to_letters(text)
    assert len(text) != 0

    print(cipher)
    #print(len(text_length), "characters.")


cipher_text()