import requests
from web3 import Web3
import json
from dotenv import load_dotenv
import os
from colorama import Fore


load_dotenv()


api_key = os.getenv('INFURA_ETH_HTTPS_API')
web3 = Web3(Web3.HTTPProvider(api_key))
block = web3.eth.get_block('latest')
to_from_pairs = {}
transaction_count = {}


# Get block transaction data
if block and block.transactions: 
    for transaction in block.transactions: 
        tx_hash = transaction.hex() # Convert from hexBytes format
        tx = web3.eth.get_transaction(tx_hash) # Use transaction hash to get transaction details
        # print(tx)
        
# Check if to/from pairs exist and update count        
        if tx.to != None:
            if tx.to in to_from_pairs:
                if to_from_pairs[tx.to] == tx["from"]:
                    transaction_count[tx.to] = transaction_count[tx.to] +1 

# Keep count on any new to addresses and create a to/from pair               
            elif tx.to not in to_from_pairs:
                transaction_count[tx.to] = 1
                to_from_pairs[tx.to] = tx["from"]

# print(transaction_count)
# print(to_from_pairs)
                
for key, value in transaction_count.items():
    if value == 2:
        print(to_from_pairs[key])