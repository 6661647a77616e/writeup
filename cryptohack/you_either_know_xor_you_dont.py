import binascii

from pwn import * 
str = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encoded = binascii.unhexlify(str)
print(encoded)
format_flag = "crypto{"
key = "myXORkey"
print(xor(encoded,key))
