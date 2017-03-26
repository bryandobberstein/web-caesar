import string

def alphabet_position(char):
    if not isinstance(char, str):
        return "character_position only works on alphabetical characters"
    elif len(char) != 1:
        return "character_position only works on single alphabetical characters"
    elif not char.isalpha():
        return "character_position only works on alphabetical characters"
    elif char.isupper():
        return string.ascii_uppercase.find(char)
    else:
        return string.ascii_lowercase.find(char)

def rotate_character(char, rot):
    if isinstance(rot, int):
        if not isinstance(char, str):
            return char
        elif not char.isalpha():
            return char
        else:
            charpos = alphabet_position(char)
            if char.isupper():
                return string.ascii_uppercase[(charpos + rot) % 26]
            else:
                return string.ascii_lowercase[(charpos + rot) % 26]

    elif isinstance(rot, str):
        if not isinstance(char, str):
            return char
        elif not char.isalpha():
            return char
        else:
            charpos = alphabet_position(char)
            rotnum = alphabet_position(rot)
            if char.isupper():
                return string.ascii_uppercase[(charpos + rotnum) % 26]
            else:
                return string.ascii_lowercase[(charpos + rotnum) % 26]

def encrypt(ptext, rot):
    etext = ""
    for i in ptext:
        etext += rotate_character(i, rot)

    return etext

def main():
    ptext = input("Enter text to rotate: ")
    rot = int(input("Enter rotation number: "))

    print(encrypt(ptext, rot))

if __name__ == '__main__': main()
