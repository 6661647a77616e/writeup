
# introduction to cryptohack

# ascii

```python
# List of ASCII values
ascii_values = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
result = ''.join(chr(value) for value in ascii_values)
print(result)
```

# hex
```python
hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"
# Convert hex to bytes
byte_string = bytes.fromhex(hex_string)
# Convert bytes to ASCII string
flag = byte_string.decode('ascii')
print(flag)
```

# base64

``` python
import base64

# The hexadecimal encoded string
hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"

# Step 1: Decode hex to bytes
byte_string = bytes.fromhex(hex_string)

# Step 2: Encode bytes to Base64
base64_string = base64.b64encode(byte_string)

# Step 3: Convert Base64 bytes to string for printing
base64_result = base64_string.decode('utf-8')

# Print the Base64 encoded result
print(base64_result)
```

# long bytes

```python
def long_to_bytes(n):
    return n.to_bytes((n.bit_length() + 7) // 8, byteorder='big')
    # The large integer to be converted
    number = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
    # Convert the number to bytes
    byte_message = long_to_bytes(number)
    # Decode the bytes to get the ASCII message
    message = byte_message.decode('ascii')
    # Print the message
    print(message)
```

# XOR Starter
```python
original = "label"
# XOR each character with 13 and convert back to a character
xored = ''.join(chr(ord(char) ^ 13) for char in original)
# Format the result as a flag
flag = f"crypto{{{xored}}}"
# Print the flag
print(flag)
```


----
# YOU EITHER KNOW XOR OR YOU DONT
```python
import binascii

from pwn import * 
str = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
encoded = binascii.unhexlify(str)
print(encoded)
format_flag = "crypto{"
key = "myXORkey"
print(xor(encoded,key))
```

# favourites bytes

```python
import binascii
str = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
encoded = binascii.unhexlify(str)
for xorkey in range(256):
    decoded = ''.join(chr(b ^ xorkey) for b in encoded)
    if decoded.startswith("crypto"):
        print(xorkey, decoded)

```

# gcd

```python
def gcd(a,b):
    if a == b:
        return b
    elif b == 0:
        return a
    quotient = a //b
    reminder = a%b
    return gcd(b,reminder)

print(gcd(66528,52920))
```

# extended GCD
```python
def gcd(a,b):
    if a == b:
        return b
    elif b == 0:
        return a
    quotient = a //b
    reminder = a%b
    return gcd(b,reminder)

def extendedGCD(p,q):
    if p == 0:
        return q, 0 , 1
    
    gcd, x1, y1 = extendedGCD(q%p, p)

    x = y1 - (q//p) * x1
    y = x1

    return gcd, x ,y

print(extendedGCD(26513,32321))

```

# modular arithmetic 1

```python
for i in range(100):
    if i % 17 == 8146798528947 % 17:
        print(i)
        break
```


# Module Arithmetic 2

```python
result = pow(273246787654, 65536, 65537)
print(result)

```


# Modular Inverse

```python

d = pow(3, -1, 13)
print(d)  # This will output 9
```:w
