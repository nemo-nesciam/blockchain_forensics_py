from web3 import Web3
import os
import json
from web3_input_decoder import decode_constructor, decode_function

from dotenv import load_dotenv
from colorama import Fore, Back, Style


load_dotenv()

ganache_instance = os.getenv('GANACHE')
send_account = os.getenv('SEND_ACCOUNT_ADDRESS')
send_account_key = os.getenv('SEND_ACCOUNT_PRIVATE_KEY')
smart_contract_account = os.getenv('SMART_CONTRACT_ADDRESS')


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

# Connect to a target smart contract
target_address = web3.to_checksum_address(smart_contract_account)
target_abi_json = '[{"inputs":[],"stateMutability":"payable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"sender","type":"address"},{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"},{"indexed":false,"internalType":"string","name":"message","type":"string"}],"name":"DepositLog","type":"event"},{"inputs":[{"internalType":"string","name":"myMessage","type":"string"}],"name":"changeMessage","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"deposit","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"getBalance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isOwner","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"withdrawAmount","type":"uint256"}],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdrawAll","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
target_abi = json.loads(target_abi_json)
target = web3.eth.contract(address=target_address, abi=target_abi)
print(f'Target: {target_address}')

print()
gas_price_wei = web3.eth.gas_price
print(f"Current gas price: {gas_price_wei} wei")
print()

withdraw_eth = target.functions.withdraw(1000000000000000000).build_transaction({
    'nonce': web3.eth.get_transaction_count(send_account),
    'from': send_account,
    'gas': 3000000,
    'gasPrice': gas_price_wei,
})

signed_withdraw = web3.eth.account.sign_transaction(withdraw_eth, send_account_key)
transaction_hash = web3.eth._send_raw_transaction(signed_withdraw.rawTransaction)

# print()

# # # Custom serializer for handling HexBytes and other non-serializable types
def custom_serializer(obj):
    if hasattr(obj, 'hex'):
        return obj.hex()
    raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

# # # Fetch the transaction details
transaction_details = web3.eth.get_transaction(transaction_hash)

# # # Convert AttributeDict to a regular dictionary
transaction_details_dict = dict(transaction_details)

# # # Pretty print the transaction details
formatted_details = json.dumps(transaction_details_dict, indent=4, default=custom_serializer)
print(f'{Fore.WHITE}Transaction confirmation:\n{Fore.RED}{formatted_details}')

tx_input = web3.to_hex(transaction_details["input"])
print()
print(f'{Fore.WHITE}Tx input data: {tx_input}')

print()
print(f'{Fore.WHITE}---------------------------------------------------------')

print()
print(f'Current contract balance: {web3.eth.get_balance(target_address)}')
print()
