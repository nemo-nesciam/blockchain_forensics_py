from web3 import Web3
import os
import json 
from colorama import Fore, Back, Style
from dotenv import load_dotenv

def split_signature(sig):
    assert len(sig) == 65, "Invalid signature length"

    r = int.from_bytes(sig[0:32], byteorder='big')
    s = int.from_bytes(sig[32:64], byteorder='big')
    v = sig[64]

    return v, r, s

# Example usage:
signature = b'your_signature_bytes_here'  # Replace this with the actual signature bytes
v, r, s = split_signature(signature)
print(f'{Fore.BLUE}"v:", v')
print(f'{Fore.YELLOW}"r:", hex(r)')
print(f'{Fore.LIGHTBLUE_EX}"s:", hex(s)')
