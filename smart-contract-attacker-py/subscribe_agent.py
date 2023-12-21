from web3 import Web3
import os
import json
import asyncio
from events import events

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
print(f'Listening for events at: {Fore.YELLOW}{target_address}')

print()
print(f'{Fore.WHITE}---------------------------------------------------------')
print()

# Set global variable for the event name
event_name = "DepositLog"

def event_handler(event): 
    event = Web3.to_json(event)
    event = json.loads(event)
    print(f"Event: {event_name}, Sender: {event['args']['sender']}, Value: {event['args']['value']}, Message: {event['args']['message']}")


print()
print(f'{Fore.WHITE}---------------------------------------------------------')
print()



# Keep listening for "specified" events and sending them to the handler 
async def event_log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            event_handler(event)
        await asyncio.sleep(poll_interval)

# Create an event filter for "specified" subscription
# Run the EventLogLoop with asyncio every 2 seconds to poll for new events
def main():
    event_filter = target.events[event_name].create_filter(fromBlock=events[event_name]["fromBlock"])
    asyncio.run(event_log_loop(event_filter, 2,))


if __name__ == "__main__": 
    main()