from web3 import Web3
import requests
import os
import json
import time

from collections import deque
from colorama import Fore, Back, Style
from dotenv import load_dotenv

from tornado_cash_addresses import (
    TORNADO_CASH_FUNDED_ACCOUNTS_QUEUE_SIZE,
    TORNADO_CASH_ADDRESSES_ETH,
    
    # Include other network addresses if needed
)
# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
infura_api_key = os.getenv('INFURA_ETH_HTTPS_API')
etherscan_api_key = os.getenv('ETHERSCAN_API')
etherscan_api_url = os.getenv('ETHERSCAN_API_URL')

# Initialize a Web3 connection using Infura
web3 = Web3(Web3.HTTPProvider(infura_api_key))

# Print a separator and check blockchain connection status
print(f'{Fore.WHITE}---------------------------------------------------------')
print()

if web3.is_connected():
    print(f'Connected to the blockchain: {Fore.GREEN}True')
else:
    print(f'Connected to the blockchain: {Fore.RED}False')

print()
print(f'{Fore.WHITE}---------------------------------------------------------')

# Initialize a deque to track addresses funded by Tornado Cash
tornado_cash_funded_accounts = deque(maxlen=TORNADO_CASH_FUNDED_ACCOUNTS_QUEUE_SIZE)

def get_recent_transactions():
    # Fetch the latest block number from the blockchain
    latest_block = web3.eth.block_number
    
    # Prepare parameters for the Etherscan API request
    params = {
        'module': 'proxy',
        'action': 'eth_getBlockByNumber',
        'tag': hex(latest_block),
        'boolean': 'true',
        'apikey': etherscan_api_key
    }
    
     # Make the API request to Etherscan
    response = requests.get(etherscan_api_url, params=params)
    
    # Error handling for the API response
    if response.status_code != 200:
        print(f"{Fore.RED}Failed to fetch transactions. HTTP Status Code: {response.status_code}")
        return latest_block, []

    try:
        data = json.loads(response.text)
        if 'result' in data and data['result'] is not None:
            transactions = data['result']['transactions']
        else:
            print(f"{Fore.RED}No 'result' found in the response or 'result' is None.")
            return latest_block, []
    except json.JSONDecodeError:
        print(f"{Fore.RED}Failed to decode JSON from response.")
        return latest_block, []
    
    # Print the latest block number and the number of transactions in it
    print(f"{Fore.BLUE}Latest block #: {Fore.WHITE}{latest_block}")
    print(f"{Fore.BLUE}Number of transactions in block: {Fore.WHITE}{len(transactions)}")
    print()
    
    return latest_block, transactions

def get_transaction_receipt(tx_hash):
     # Fetch the transaction receipt for a given transaction hash
    return web3.eth.get_transaction_receipt(tx_hash)

def is_contract_creation(receipt):
     # Check if the transaction receipt indicates contract creation
    return receipt['contractAddress'] is not None

def analyze_transaction(tx):
    # Analyze a transaction to detect Tornado Cash interaction and contract creation
    receipt = get_transaction_receipt(tx['hash'])
    contract_creation = is_contract_creation(receipt)

    funded_by_tornado = tx['from'].lower() in TORNADO_CASH_ADDRESSES_ETH
    if funded_by_tornado:
        tornado_cash_funded_accounts.append(tx['to'].lower())
        print(f"{Fore.CYAN}Transaction from Tornado Cash ETH address detected: {tx['hash']}")

    if contract_creation:
        print(f"{Fore.RED}Contract created at: {receipt['contractAddress']}")

    return funded_by_tornado, contract_creation

def main():
    # Main loop to continuously fetch and analyze transactions
    while True:
        print()
        print(f"{Fore.YELLOW}Fetching recent transactions...")
        print()
        latest_block, transactions = get_recent_transactions()
        print(f"{Fore.YELLOW}Transactions from the latest block:")
        print()
        
        tornado_cash_transactions = 0
        contract_creations = 0

        for tx in transactions:
            funded_by_tornado, contract_creation = analyze_transaction(tx)
            tornado_cash_transactions += funded_by_tornado
            contract_creations += contract_creation

        if tornado_cash_transactions == 0:
            print(f"{Fore.BLUE}No Tornado Cash funding detected in this block.")
    
        if contract_creations == 0:
            print(f"{Fore.BLUE}No Tornado Cash-related contract creations in this block.")
        
        print()
        print(f'{Fore.WHITE}---------------------------------------------------------')

        time.sleep(5)  # Wait for 5 seconds before the next iteration  
    
if __name__ == "__main__":
    main()
