from web3 import Web3
import os
import json
from dotenv import load_dotenv
from colorama import Fore, Back, Style


load_dotenv()

ganache_instance = os.getenv('GANACHE')
send_account = os.getenv('SEND_ACCOUNT_ADDRESS')
send_account_key = os.getenv('SEND_ACCOUNT_PRIVATE_KEY')
receive_account = os.getenv('RECEIVE_ACCOUNT_ADDRESS')
receive_account_key = os.getenv('RECEIVE_ACCOUNT_PRIVATE_KEY')
# etherscan_api_key = os.getenv('ETHERSCAN_API')

# Create a Web3 connection instance 
web3 = Web3(Web3.HTTPProvider(ganache_instance))
print()
# Check if connected to the blockchain
if web3.is_connected():
    print(f'Connected: {Fore.GREEN}True')
else:
    print(f'Connected: {Fore.RED}False')

print()
print(f'{Fore.WHITE}---------------------------------------------------------')
print()

# Get the current gas price in Wei

gas_price_wei = web3.eth.gas_price
print(f"Current gas price: {gas_price_wei} wei")

# # Convert the gas price from Wei to Gwei for readability

gas_price_gwei = web3.from_wei(gas_price_wei, 'gwei')
print(f"Current gas price: {Fore.GREEN}{gas_price_gwei} gwei")

print()
print(f'{Fore.WHITE}.........................................................')
print()

transaction = {
    'nonce': web3.eth.get_transaction_count(send_account),
    'to': receive_account,
    'value': web3.to_wei(1, 'ether'),
    'gas': 3000000,
    'gasPrice': gas_price_wei,
}

#--------------- Sign/send a transaction ---------------#

# Custom serializer for handling HexBytes and other non-serializable types
def custom_serializer(obj):
    if hasattr(obj, 'hex'):
        return obj.hex()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

signed_transaction = web3.eth.account.sign_transaction(transaction, send_account_key)
transaction_hash = web3.eth._send_raw_transaction(signed_transaction.rawTransaction)

# # Fetch the transaction details
transaction_details = web3.eth.get_transaction(transaction_hash)

# # Convert AttributeDict to a regular dictionary
transaction_details_dict = dict(transaction_details)

# # Pretty print the transaction details
formatted_details = json.dumps(transaction_details_dict, indent=4, default=custom_serializer)
print(f'{Fore.WHITE}Transaction confirmation:\n{Fore.YELLOW}{formatted_details}')

print()
print(f'{Fore.WHITE}---------------------------------------------------------')