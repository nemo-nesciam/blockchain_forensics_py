import requests
from web3 import Web3
import json
from dotenv import load_dotenv
import os
from colorama import Fore, Back, Style


load_dotenv()


api_key = os.getenv('INFURA_ETH_HTTPS_API')
web3 = Web3(Web3.HTTPProvider(api_key))
block = web3.eth.get_block('latest')
to_from_pairs = {}
transaction_count = {}
tx_lookup = {}
possible_s_attack = {}

def pull_transactions():
    """ Pull down all transactions and create dictionaries of counts 
    related to  To/From Address Pairs and associated hashes
    Dictionaries Created: 
          transaction_count To:count, 
          to_from_pairs To:From, 
          tx_lookup Txhash[to,from,gas]"""
    
    # Parse out transactions and their transaction hashes
    if block and block.transactions: 
        for transaction in block.transactions: 
            tx_hash = transaction.hex() # Convert txhash from hexBytes format
            tx = web3.eth.get_transaction(tx_hash)

    # Check if to/from pairs exist and update count           
            if tx.to != None:
                if tx.to in to_from_pairs:
                    if to_from_pairs[tx.to] == tx["from"]:
                        transaction_count[tx.to] = transaction_count[tx.to] +1 
                        tx_lookup[tx_hash] =  [tx.to,tx["from"],tx.gasPrice]

    # Keep count on any new to addresses and create a to/from pair                
                elif tx.to not in to_from_pairs:
                    transaction_count[tx.to] = 1
                    to_from_pairs[tx.to] = tx["from"]
                    tx_lookup[tx_hash] =  [tx.to,tx["from"],tx.gasPrice]

              
def identify_bots():
    """Grab all to/from pairs with exactly 2 transactions in a single block 
       for review and create possible_s_attack dictionary txhash:[to,gas]"""
    for transaction_hash, pair in tx_lookup.items():    
        if transaction_count[pair[0]] == 2:
            possible_s_attack[transaction_hash] = [pair[0],pair[2]]   

            
def identify_sandwich_attacks(possible_s_attack): 
    """This function takes in a dictionary with a value list hash:[to,gas] 
    of possible sandwich attacks with 2 transactions and Parses for gas 
    variance to remove bots which keep sending via the same gas calculation"""
    #Dictionaries to swap and parse out duplicates and return valid attacks
    all_bots = {}
    duplicate_bots = {}
    sandwich_attacks = []

    # Checks for duplicate gas values as these cannot be sandwich attacks and can be removed
    # These are parsed into total lists of bots and duplicates
    for s_hash, s_gas in possible_s_attack.items(): 
        if s_gas[1] in all_bots.values():
            duplicate_bots[s_hash] = s_gas[1]
        
        elif s_gas[1] not in all_bots.values():    
            all_bots[s_hash] = s_gas[1]
            
    print(f'{len(all_bots)} bot transaction(s) with 2 like pairs identified:')
    print('-------------------------------------------------------------------')
    for bot in all_bots.keys():
        print(f'{Style.DIM}{bot}')
    print('-------------------------------------------------------------------')


    # Grabs all transactions gas prices which are bots but not in duplicate_bots 
    for s_hash, bot in all_bots.items():
        if duplicate_bots:
            if bot not in duplicate_bots.values():
               sandwich_attacks.append(s_hash) 

    return sandwich_attacks           
 

if __name__ == "__main__":
# Setup transactions and bot dictionaries for parsing
    pull_transactions()
    identify_bots()

# Check possible sandwich attack pairs against the sandwich attack algorithm
# Returns and prints matching
    if possible_s_attack:
        sandwich_attacks =identify_sandwich_attacks(possible_s_attack)
        for sandwich_attack in sandwich_attacks:
            print(f'{Fore.CYAN}Sandwich Attack Identified: \n {Fore.MAGENTA}{sandwich_attack}')      