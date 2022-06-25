MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}


def text_to_morse_code(message):
    morse=''
    for letter in message:
        if letter!=' ':
            morse+=MORSE_CODE_DICT[letter.capitalize()]+' '
        else:
            morse+=' '
    return morse


def morse_code_to_text(morse):
    morse+=' '
    text=''
    demorse=''
    i=0
    for letter in morse:
        if letter!=' ':
            i=0
            text+=letter
        else:
            i+=1
            if i>=2:
                demorse+=' '
            else:
                demorse+=list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(text)]
                text=''
    return demorse


morsecode=text_to_morse_code("AB XY MN     ZYX")

print(morse_code_to_text(morsecode))



