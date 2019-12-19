def Encryption(plainText, key):
    plainText = plainText.upper().replace(' ', '')
    return ''.join(map(lambda a: chr((ord(a)-65 + key) % 26 + 65),plainText))

def Decryption(cypherText, key):
    cypherText = cypherText.upper().replace(' ', '')
    return ''.join(map(lambda a: chr((ord(a)-65 - key) % 26 + 65),cypherText))

def Main():
    plainText = 'Your plain text'
    key = 20
    print(f'Plain text: {plainText}')
    cypherText = Encryption(plainText,key)
    print(f'Cryptogram : {cypherText}')
    plainText = Decryption(cypherText,key)
    print(f'Decrypted text: {plainText}')

if __name__ == "__main__":
    Main()