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

print(f'{Fore.WHITE}---------------------------------------------------------')

# Connect to a target smart contract
target_address = web3.to_checksum_address("0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f")
target_abi_json = '[{"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"token0","type":"address"},{"indexed":true,"internalType":"address","name":"token1","type":"address"},{"indexed":false,"internalType":"address","name":"pair","type":"address"},{"indexed":false,"internalType":"uint256","name":"","type":"uint256"}],"name":"PairCreated","type":"event"},{"constant":true,"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"allPairs","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"allPairsLength","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"tokenA","type":"address"},{"internalType":"address","name":"tokenB","type":"address"}],"name":"createPair","outputs":[{"internalType":"address","name":"pair","type":"address"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"feeTo","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"feeToSetter","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"getPair","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeTo","type":"address"}],"name":"setFeeTo","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_feeToSetter","type":"address"}],"name":"setFeeToSetter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
target_abi = json.loads(target_abi_json)
target_contract = web3.eth.contract(address=target_address, abi=target_abi)

# List all pairs
def list_all_pairs(contract):
    pair_count = contract.functions.allPairsLength().call()
    print(f"Total number of pairs: {pair_count}\nPairs:")

    for i in range(pair_count):
        pair_address = contract.functions.allPairs(i).call()


        print(f"{i+1}. Pair: {pair_address}")

# List all pairs
list_all_pairs(target_contract)