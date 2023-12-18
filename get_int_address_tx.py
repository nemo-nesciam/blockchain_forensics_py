import requests
from dotenv import load_dotenv
import os
from colorama import Fore


load_dotenv()


api_key = os.getenv('ETHERSCAN_API')
# print(api_key)
target_address = '0x386a4a06B477BC49E8bc75618aA1219Cd82f0ba6'
attackers_list = [line.rstrip() for line in open('malicious_addresses.txt')]
total_value_received = 0

for count, target_address in enumerate (attackers_list): 
    value_in_address = 0

    # Get Internal Transaction By Address
    etherscan_params = (('module', 'account'), 
                        ('action', 'txlistinternal'),
                        ('address', target_address), 
                        ('sort', 'asc'),
                        ('apikey', api_key))

    response = requests.get("https://api.etherscan.io/api", params=etherscan_params)
    data = response.json().get("result")

    for ID, transaction in enumerate(data):
        current_value = int(transaction.get("value"))/1000000000000000000
        # print(f'Transaction: {count}')
        value_in_address += current_value
        total_value_received += current_value
 
    print(f'{Fore.WHITE}Value in: {Fore.RED}{target_address} is {Fore.GREEN}{value_in_address}')

print(f'{Fore.YELLOW} Total Contract Value Received: {Fore.GREEN}{total_value_received}')
    # print(f'BlockNumber: {transaction.get("blockNumber")}')
    # print(f'Value: {int(transaction.get("value"))/1000000000000000000}')