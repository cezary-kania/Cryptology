def TextToBin(text):
    #return ''.join(map(lambda x: format(x,'b'),bytearray(text,'utf-8')))
    return bin(int.from_bytes(text.encode(),'big')).replace('b','')
def BinToText(binN):
    n = int(binN,2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def Encryption(plainText, key):
    binPlainText = TextToBin(plainText)
    binKey = TextToBin(key)
    return ''.join(list(map(str,list(map(lambda a,b: (int(a) + int(b)) % 2,binPlainText,binKey)))))

def Decryption(cipherText, key):
    binKey = TextToBin(key)
    return BinToText(''.join(list(map(str,list(map(lambda a,b: (int(a) + int(b)) % 2,cipherText,binKey))))))

def Main():
    plainText = input('Input text to encode:')
    key = input('Input secret key:')
    cipherText = Encryption(plainText,key)
    print(cipherText)
    plainText = Decryption(cipherText,key)
    print(plainText)

if __name__ == "__main__":
    Main()
    print('Program end')