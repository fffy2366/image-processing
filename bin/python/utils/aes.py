from Crypto.Cipher import AES
import base64


def _pad(s): return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)
def _cipher():
    key = '7854156156611111'
    iv = '0000000000000000'
    return AES.new(key=key, mode=AES.MODE_CBC, IV=iv)

def encrypt_token(data):
    return _cipher().encrypt(_pad(data))

def decrypt_token(data):
    return _cipher().decrypt(data)

if __name__ == '__main__':
    print('Python encrypt: ' + base64.b64encode(encrypt_token('test')))
    # print('Python decrypt: ' + decrypt_token(base64.b64decode('FSfhJ/gk3iEJOPVLyFVc2Q==')))