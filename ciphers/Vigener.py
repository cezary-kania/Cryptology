from math import ceil

def PrepareInput(text, key):
    text = text.upper().replace(' ', '')
    key = key.upper().replace(' ', '')
    if len(key) < len(text):
        key *= ceil((len(text) - len(key)) / len(key)) + 1
        key = key[:len(text)]
    return (text, key)

def Encryption(plainText, key):
    plainText, key = PrepareInput(plainText,key)
    return ''.join(map(lambda x: chr(x+65),(list(map(lambda a,b: (ord(a)+ord(b)-130) % 26,plainText,key)))))

def Decryption(cypherText, key):
    cypherText, key = PrepareInput(cypherText, key)
    return ''.join(map(lambda x: chr(x+65),(list(map(lambda a,b: (ord(a)-ord(b)-130) % 26,cypherText,key)))))

def Main():
    plainText = 'Your plain text'
    key = 'Your super secret key'
    print(f'Plain text: {plainText}')
    cypherText = Encryption(plainText,key)
    print(f'Cryptogram : {cypherText}')
    plainText = Decryption(cypherText,key)
    print(f'Decrypted text: {plainText}')

if __name__ == "__main__":
    Main()