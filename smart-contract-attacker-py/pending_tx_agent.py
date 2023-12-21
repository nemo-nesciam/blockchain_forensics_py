from web3 import Web3
from websockets import connect
import os
import json
import asyncio
from colorama import Fore, Back, Style
from dotenv import load_dotenv


load_dotenv()

infura_https_api_key = os.getenv('INFURA_ETH_HTTPS_API')
infura_ws_api_key = os.getenv('INFURA_ETH_WS_API')
# etherscan_api_key = os.getenv('ETHERSCAN_API')

# Create a Web3 connection instance 
web3 = Web3(Web3.HTTPProvider(infura_https_api_key))
# web3 = Web3(Web3.WebsocketProvider(infura_ws_api_key))
# Check if connected to the blockchain
if web3.is_connected():
    print()
    print(f'Connected: {Fore.GREEN}True')
else:
    print(f'Connected: {Fore.RED}False')

print()
print(f'{Fore.WHITE}---------------------------------------------------------')
print()

# Possible filters

filter_for_address = '0xEf1c6E67703c7BD7107eed8303Fbe6EC2554BF6B'

def event_handler(pending_tx):
    transaction = json.loads(pending_tx)
    tx_hash = transaction['params']['result']
    tx_details = web3.eth.get_transaction(tx_hash)
    
     # Apply filter(s) if needed: 
    if tx_details['to'] == web3.to_checksum_address(filter_for_address):
        print (web3.to_hex(tx_details['hash']))

    # # Convert AttributeDict to a regular dictionary and convert values to hex
    # tx_dict = {k: v.hex() if hasattr(v, 'hex') else v for k, v in dict(tx_details).items()}

    # # Pretty print the transaction details
    # print(json.dumps(tx_dict, indent=4, default=str))

async def subscribe_pending_tx():
    async with connect(infura_ws_api_key) as ws:
        await ws.send('{"jsonrpc": "2.0", "id": 1, "method": "eth_subscribe", "params": ["newPendingTransactions"]}')

    
        while True:
            try:
                pending_tx = await asyncio.wait_for(ws.recv(), timeout=15)
                event_handler(pending_tx)

            except KeyboardInterrupt:
                exit()
            except:
                pass

if __name__ == "__main__":
        asyncio.run(subscribe_pending_tx())