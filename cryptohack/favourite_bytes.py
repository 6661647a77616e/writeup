# Given primes
p = 857504083339712752489993810777
q = 1029224947942998075080348647219

# Calculate N
N = p * q

# Calculate Euler's totient
phi = (p - 1) * (q - 1)

str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encoded = binascii.unhexlify(str)
for xorkey in range(256):
    decoded = ''.join(chr(b ^ xorkey) for b in encoded)
    if decoded.startswith("crypto"):
        print(xorkey, decoded)
