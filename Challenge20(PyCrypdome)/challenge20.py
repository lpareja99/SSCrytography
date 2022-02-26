from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA



message = b'My message!'
key = RSA.importKey(open('myKey.pem').read(),passphrase='marina')
cipher = PKCS1_OAEP.new(key)
ciphertext = cipher.encrypt(message)


my_message = cipher.decrypt(ciphertext)
print(my_message)

