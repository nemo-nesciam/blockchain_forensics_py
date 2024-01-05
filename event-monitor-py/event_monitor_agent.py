from web3 import Web3
import requests
import os
import json
import time
from collections import deque
from colorama import Fore, Back, Style
from dotenv import load_dotenv

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

# Define global variables and thresholds
CENTRALIZED_EXCHANGES_THRESHOLD = 200
ANOMALOUS_TRANSACTION_THRESHOLD = 10
ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'
blacklist = set()
eoa_transactions = {}
approval_history = {}

# Function to check if an address is an EOA
def is_eoa(address):
    code = web3.eth.getCode(address)
    return code == '0x'

# Function to handle each mined transaction
def handle_transaction(transaction):
    global blacklist, eoa_transactions, approval_history

    # Initialize findings for this transaction
    findings = []

    # Check if transaction is a token approval (This is a placeholder. Actual implementation depends on the contract ABI)
    if is_token_approval(transaction):
        owner_address = transaction['from']
        spender_address = get_spender_address(transaction)

        # Check for blacklisted addresses and the ZeroAddress
        if owner_address in blacklist or spender_address in blacklist or spender_address == ZERO_ADDRESS:
            return findings

        # Check if addresses are EOAs
        if is_eoa(owner_address) and is_eoa(spender_address):
            # Update transaction count for the spender
            eoa_transactions[spender_address] = eoa_transactions.get(spender_address, 0) + 1

            # If spender is a high-frequency address, add to blacklist
            if eoa_transactions[spender_address] > CENTRALIZED_EXCHANGES_THRESHOLD:
                blacklist.add(spender_address)
            else:
                # Track approval history
                if spender_address not in approval_history:
                    approval_history[spender_address] = deque(maxlen=ANOMALOUS_TRANSACTION_THRESHOLD)
                approval_history[spender_address].append(owner_address)

                # Check for anomalous approval patterns
                if len(approval_history[spender_address]) == ANOMALOUS_TRANSACTION_THRESHOLD:
                    findings.append({
                        'spender_address': spender_address,
                        'owner_addresses': list(approval_history[spender_address]),
                        'transaction_count': eoa_transactions[spender_address]
                    })

    return findings

# Function to check if an address is an EOA
def is_eoa(address):
    code = web3.eth.getCode(address)
    return code == '0x'

# Function to identify token approval events (Placeholder - requires actual contract ABI and event signature)
def is_token_approval(transaction):
    # Implementation depends on the specific contract and event structure
    return 'tokenApprovalEventSignature' in transaction['input']

# Function to extract spender address from a token approval transaction
def get_spender_address(transaction):
    # Implementation depends on the specific contract and event structure
    # Placeholder: extract and return the spender address from transaction data
    return 'extracted_spender_address'

# Function to fetch recent transactions
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
        return []

    # Parse the response data
    block_data = response.json()
    transactions = block_data['result']['transactions']
    return transactions

# Function to identify token approval events (Placeholder - requires actual contract ABI and event signature)
def is_token_approval(transaction):
    # Implementation depends on the specific contract and event structure
    return 'tokenApprovalEventSignature' in transaction['input']


# Main loop to process transactions
while True:
    transactions = get_recent_transactions()
    for transaction in transactions:
        findings = handle_transaction(transaction)
        # Process findings as needed

    # Implement a sleep mechanism to avoid hitting rate limits
    time.sleep(1)
