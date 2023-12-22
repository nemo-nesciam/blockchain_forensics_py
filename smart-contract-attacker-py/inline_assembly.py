from web3 import Web3
import os
from web3 import Web3
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


# function_hash = tx['input'][0:10]
# address = tx['input'][34:74]
# value= tx['input'][74:]

# print(f'function_hash: {function_hash}')
# print(f'address: {address}')
# print(f'value: {w3.toInit(hexstr=value)/10**decimals}')