from web3 import Web3
import os
import json 
from colorama import Fore, Back, Style
from constants import CHAINLINK_TOKEN_CONTRACT, TARGET_ADDRESS_1
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

print(f'{Fore.WHITE}---------------------------------------------------------')

# Connect to a target smart contract
target_address = web3.to_checksum_address(CHAINLINK_TOKEN_CONTRACT)
print(f'{Fore.WHITE}Type of address: {Fore.MAGENTA}{(web3.eth.get_code(target_address))}')
print(f'{Fore.WHITE}Total balance: {Fore.MAGENTA}{web3.from_wei(web3.eth.get_balance(target_address), "ether")}')

print(f'{Fore.WHITE}---------------------------------------------------------')