
def MultiplyRowByColumn(encodedText, key_column):
    output = 0
    for i in range(len(encodedText)):
        output += encodedText[i]*key_column[i]
    return output

def TextToIntVector(text):
    return [ord(letter) - 65 for letter in text]

def IntVectorToText(vector):
    return ''.join([chr(num + 65) for num in vector])

def Hill(text, key):
    text = text.upper().replace(' ', '')
    keySize = len(key)
    if len(text) % keySize != 0:
        text += 'X'*(len(text) % keySize) 
    output, i = [], 0
    while i < len(text): # Old ver = while i + keySize < len(text) + 2:
        for j in range(keySize):
            partOfText = text[i:i+keySize]
            textAsNums = TextToIntVector(partOfText)
            output.append(MultiplyRowByColumn(textAsNums,key[j % keySize]) % 26)
        i += keySize
    return IntVectorToText(output)


def Encryption(plainText, key):
    return Hill(plainText, key)

def Decryption(cypherText, inv_key):
    return Hill(cypherText, inv_key)

def Main():
    plainText = 'Yours plain text'
    key = [[11,3],[8,7]]
    inv_key = [[7,23],[18,11]]
    print(f'Plain text: {plainText}')
    cypherText = Encryption(plainText,key)
    print(f'Cryptogram : {cypherText}')
    plainText = Decryption(cypherText,inv_key)
    print(f'Decrypted text: {plainText}')

if __name__ == "__main__":
    Main()