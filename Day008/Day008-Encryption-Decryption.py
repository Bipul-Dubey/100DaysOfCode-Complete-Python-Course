logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)
print("caesar ciphar")

# write alphabet 2 time because when z is encode then it go out of length of alphabet
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u',
          'v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# long code -- word only encode or decode
"""def encrypt(text,shift):
    cipher_text=""
    for letter in text:
        position=alphabet.index(letter)
        new_position=position+shift
        new_letter=alphabet[new_position]
        cipher_text+=new_letter
    print(f"The Encoded text is {cipher_text} .")

def decrypt(cipher_text,shift):
    text=""
    for letter in cipher_text:
        position=alphabet.index(letter)
        new_position=position-shift
        text+=alphabet[new_position]
    print(f"The decoded text is {text} .")
"""

def caesr_code(text,shift,direction):
    end_text=""
    if direction=='decode':
        shift*=-1
    for char in text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=position+shift
            end_text+=alphabet[new_position]
        else:
            end_text+=char
    print(f"The {direction}d text is {end_text}")

    
should_continue=True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift=shift%26
    caesr_code(text,shift,direction)
    result=input("Type 'yes' if you want to continue other type 'no' ")
    if result=='no':
        should_continue=False
        print("goodbye")