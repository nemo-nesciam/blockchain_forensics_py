from web3 import Web3
import os
from colorama import Fore, Back, Style
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('INFURA_ETH_HTTPS_API')

#--------------- Create a Web3 connection instance ---------------#
web3 = Web3(Web3.HTTPProvider(api_key))

#--------------- Check if connected to the blockchain ------------#
if web3.is_connected():
    print(f'Connected: {Fore.GREEN}True')
else:
    print(f'Connected: {Fore.RED}False')

#--------------- Connect to a target smart contract --------------#
target_address = web3.toChecksumAddress("")
target_abi = ""
target = web3.eth.contract(address=target_address, abi=target_abi)
