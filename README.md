# import bitcoin
from bitcoin import random_key, privtopub, pubtoaddr
# Create Private Key
private_key = random_key()
print("Private Key:", private_key)
# Create Public Key
public_key = privtopub(private_key)
print("Public Key:", public_key)
# Create a Bitcoin Address
address = pubtoaddr(public_key)
print("My Address is:", address)
