#This code is for Python Bootcamp Class
#Only for eductional purpose 
#4.10.2021
from secrets import token_bytes

class Encrypt:
    def __init__(self):
        pass

    def secretKey(self,length):
        tb : bytes = token_bytes(length)
        return int.from_bytes(tb,"big")

    def encyrpt(self,orData):
        originalBytes :bytes = orData.encode()
        SecretKey :int =self.secretKey(len(originalBytes))
        print("Secret Key : ",SecretKey)

        originalBytesForCT :bytes =orData.encode()
        CT_Data : int =int.from_bytes(originalBytesForCT,"big")

        CypherText : int = SecretKey ^ CT_Data
        print("CypherText : ",CypherText)

        return CypherText , SecretKey

    def decrypt(self,Cypher , Key):
        originalData : int = Cypher ^ Key
        Byte_data : bytes =originalData.to_bytes((originalData.bit_length()+7)//8 , "big")
        return Byte_data.decode()

if __name__ == '__main__':
    orString = 'GreenHackers'
    encryptAndDecrypt =Encrypt()
    Cypher , Key =encryptAndDecrypt.encyrpt(orString)

    OriignalDecryptedData =encryptAndDecrypt.decrypt(Cypher,Key)
    print("OrigitnalDecryptedData",OriignalDecryptedData)

