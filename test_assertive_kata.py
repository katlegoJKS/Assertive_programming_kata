from assertive_kata import *

def test_encrypt_to_morse_code():
    text = "Hi-There"
    result = encrypt_to_morse_code(text.upper())
    assert len(text) != 0

def test_decrypt_to_text():
    morse_code = ".... .. -....- - .... . .-. ." 
    result = decrypt_to_text(morse_code.upper())
    assert len(morse_code) != 0