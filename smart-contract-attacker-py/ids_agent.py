from web3 import Web3
import os
import json 
from colorama import Fore, Back, Style
from dotenv import load_dotenv


load_dotenv()

infura_api_key = os.getenv('INFURA_ETH_HTTPS_API')
# etherscan_api_key = os.getenv('ETHERSCAN_API')

# Create a Web3 connection instance 
web3 = Web3(Web3.HTTPProvider(infura_api_key))

# Check if connected to the blockchain
if web3.is_connected():
    print(f'Connected: {Fore.GREEN}True')
else:
    print(f'Connected: {Fore.RED}False')

print()
print(f'{Fore.WHITE}---------------------------------------------------------')
print()

block = web3.eth.get_block('latest')

# List of function signatures to search for
function_signatures = ['095ea7b3', '', '']

# Monitoring for specific functions: 
for transaction in block['transactions']:
    value = web3.eth.get_transaction(transaction)
    input_data = value['input'].hex()  # Convert the bytes object to a hex string
  
    for signature in function_signatures:
        if signature in input_data:
            print(f"{Fore.WHITE}Transaction Hash: {web3.to_hex(value['hash'])}, Signature:{Fore.LIGHTBLUE_EX}{signature}")