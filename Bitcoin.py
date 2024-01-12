This is a simple Bitcoin Wallet Address Project

from bitcoin import random_key, privtopub, pubtoaddr
private_key = random_key()
print("Private Key:", private_key)
public_key = privtopub(private_key)
print("Public Key:", public_key)
address = pubtoaddr(public_key)
print("My Address is:", address)
