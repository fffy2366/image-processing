from Crypto.Cipher import AES
import base64


class Aes:
    def __init__(self, key, iv):
        self.KEY = key
        self.IV = iv

    def _pad(self,s): return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
    def _cipher(self):
        # key = '7854156156611111'
        # iv = '0000000000000000'
        key = self.KEY
        iv = self.IV
        return AES.new(key=key, mode=AES.MODE_CBC, IV=iv)

    def encrypt_token(self,data):
        return self._cipher().encrypt(self._pad(data))

    def decrypt_token(self,data):
        return self._cipher().decrypt(data)



if __name__ == '__main__':
    aes = Aes('7854156156611111','0000000000000000')
    print('Python encrypt: ' + base64.b64encode(aes.encrypt_token('test')))
    # print('Python decrypt: ' + decrypt_token(base64.b64decode('FSfhJ/gk3iEJOPVLyFVc2Q==')))