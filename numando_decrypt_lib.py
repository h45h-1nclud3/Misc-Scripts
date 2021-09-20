import sys


key = '99871818'

with open(sys.argv[1],'rb') as f:
    enc_lib = f.read()

decrypted_lib = []
print bytearray(enc_lib[:10])
for i in range(len(enc_lib)):
    decrypted_lib.append(ord(enc_lib[i]) ^ ord(key[i%len(key)]) )

with open(sys.argv[1] + '_decrypted', 'wb') as f:
    f.write(bytearray(decrypted_lib))
print bytearray(decrypted_lib[:10])

