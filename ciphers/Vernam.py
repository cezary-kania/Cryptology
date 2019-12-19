def TextToBin(text):
    return ''.join(map(lambda x: format(x,'b'),bytearray(text,'utf-8')))

def BinToText(binN):
    n = int(binN,2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

def Encryption(plainText, key):
    pTasBytes = TextToBin(plainText)
    keyAsBytes = TextToBin(key)
    return BinToText(''.join(map(str,list(map(lambda a,b: (int(a) + int(b)) % 2,pTasBytes,keyAsBytes)))))

def Decryption(cipherText, key):
    cTasBytes = TextToBin(cipherText)
    keyAsBytes = TextToBin(key)
    return BinToText(''.join(map(str,list(map(lambda a,b: (int(a) + int(b)) % 2,cTasBytes,keyAsBytes)))))

def Main():
    plainText = 'abc'
    key = 'abx'
    cipherText = Encryption(plainText,key)
    print(cipherText)
    plainText = Decryption(cipherText,key)
    print(plainText)

if __name__ == "__main__":
    Main()
    print('Program end')