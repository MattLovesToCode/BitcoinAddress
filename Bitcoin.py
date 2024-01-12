This is a simple Bitcoin Wallet Address Project I used from a video I watched

# import bitcoin
from bitcoin import random_key, privtopub, pubtoaddr
# Create a Private Key
private_key = random_key()
print("Private Key:", private_key)
# Create Public Key
public_key = privtopub(private_key)
print("Public Key:", public_key)
# Create A Bitcoin Address
address = pubtoaddr(public_key)
print("My Address is:", address)
