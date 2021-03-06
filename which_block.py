#!/usr/bin/env python

import argparse
import re
import pprint
import math
from web3 import Web3, HTTPProvider

def main():

    DEBUG = False 
    parser = argparse.ArgumentParser()
    parser.add_argument("contract_address", help="the address of the contract you want to examine")
    parser.add_argument("web3_host", help="host domain you want to examine (ex: https://ropsten.infura.io/v3/f54e8e6ea8e73724b81518b6d5c31a07)")
    args = parser.parse_args()

    contract_address = args.contract_address
    web3_host = args.web3_host

    #verify args
    acceptable_address = re.compile('^0x\w{40}$')
    if not acceptable_address.match(contract_address):
        print("    contract_address is not in the correct format -- it should start with '0x' followed by 40 alphanumeric characters.")
        
    acceptable_host = re.compile('^http')
    if not acceptable_host.match(web3_host):
        print("    web3_host is not in the correct format -- it should start with 'http' and provide a URL and API key")

    # web3.py instance
    w3 = Web3(HTTPProvider(web3_host))

    try:
        shortest = w3.eth.getBlock('earliest')['number']
    except:
        print("\nOops.  It looks like you aren't authorized to use the Web3 host URL you provided. Please double-check your URL.\n")

    tallest = w3.eth.getBlock('latest')['number']

    block_nbr = find_block_nbr( shortest, tallest, contract_address, w3 )
    if DEBUG: print("The contract was deployed in Block number: ", block_nbr) 

    if DEBUG: print("Contract Address: ", contract_address)
    block = w3.eth.getBlock( block_nbr )
    transactions = block['transactions']

    if DEBUG: print("Looping through transactions")
    for elem in transactions:
        transaction = w3.eth.getTransactionReceipt(elem)

        if transaction['contractAddress'] == contract_address:
            print('Block Hash: ', end='', flush=True)
            pprint.pprint(transaction['blockHash'])
            print('Transaction Hash: ', end='', flush=True)
            pprint.pprint(transaction['transactionHash'])


def round_up(val):

    """
    .. function:: round_up(val)
       Rounds *val* to the nearest integer.  .5 is always rounded up.

    round_up() always rounds .5 up to the nearest integer.  This was the default behavior of the round() function before Python 3.
    In Python 3: "Exact halfway cases are now rounded to the nearest even result instead of away from zero. (For example, round(2.5) 
    now returns 2 rather than 3.)" (source: https://docs.python.org/3/whatsnew/3.0.html)

    Python 3's round() behavior would have given us inconsistent results in find_block_nbr()
    """

    if (float(val) % 1) >= 0.5:
        x = math.ceil(val)
    else:
        x = round(val)

    return x

def find_block_nbr( shortest, tallest, contract_address, w3):

    """
    .. function:: find_block_nbr(shortest, tallest, contract_address, w3)
       Returns the block number in which a smart contract was deployed

    find_block_nbr() finds the block at which the smart contract identified by the contract_address was deployed
    We find this by calling web3.eth.getCode(), which has an optional block_identifier param which specifies the block height
    If getCode() returns: Hexcode(0x) then we know that the block height is too short -- the contract was deployed in a later block
    We then choose a new block height halfway between the tallest and shortest block heights that we have tested to see whether 
    the contract had been deployed before this new block

    We're looking for the shortest and tallest block heights where the block heights are only separated by a single block, and
    at which eth.getCode() returns None for the shorter block height and bytecode for the taller block height.  When we find 
    that point, the taller block height will be the block number at which the contract was deployed.
    """

    if tallest - shortest == 1:
        return tallest

    else:
        halfway = int(round_up(((tallest-shortest)/2)));
        block_height = shortest + halfway
        bytecode = w3.eth.getCode(contract_address,block_height)

        #block_height is too short -- update shortest
        if bytecode == b'':
            shortest = block_height

        #block_height is too tall -- update tallest
        else: 
            tallest = block_height 

        return find_block_nbr(shortest, tallest, contract_address, w3)

if __name__ == '__main__':
    main()
