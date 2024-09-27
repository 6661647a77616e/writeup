from Crypto.Hash import SHA256
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Read the private key file
with open('private_0a1880d1fffce9403686130a1f932b10.key', 'r') as key_file:
    key_data = key_file.read().strip().split('\n')

# Parse the key data
N = int(key_data[0].split('=')[1])
d = int(key_data[1].split('=')[1])

# Public exponent e (usually 65537)
e = 65537

# The flag to be signed
flag = "crypto{Immut4ble_m3ssag1ng}"

# Step 1: Hash the flag using SHA256
hash_object = SHA256.new(flag.encode())
hashed = hash_object.digest()

# Step 2: Convert the hash to a long integer
hash_as_long = bytes_to_long(hashed)

# Step 3: Sign the hash (encrypt with private key)
signature = pow(hash_as_long, d, N)

print(f"The signature is: {signature}")

# Verification (optional, but good to check)
# Step 4: "Decrypt" the signature with public key
decrypted_hash = pow(signature, e, N)

# Step 5: Convert back to bytes and compare with original hash
decrypted_hash_bytes = long_to_bytes(decrypted_hash)
assert decrypted_hash_bytes == hashed, "Signature verification failed!"

print("Signature verified successfully!")