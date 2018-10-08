# which_block
Accepts an Ethereum contract address and a web3 host, quickly traverses the block chain, and returns the block hash and transaction hash in which the contract was deployed.

# Installation:

sudo pip install git+https://github.com/cbrooks42/which_block.git#egg=which_block

# Usage:

which-block contract_address web3_host

Example: 

```
which-block 0xe61b13797911b5a496Ec678db7EDd667F706aFdc https://ropsten.infura.io/v3/f54e8e6ea8e73724b81518b6d5c31a07

  Block Hash: HexBytes('0x1f97549b206ce1fde9f4d861aab0fcf1ace447ac876d45d10c468d0574f5974d')
  Transaction Hash: HexBytes('0x14ae13ea060d67808056cc02ccf3a3007ca52af30ca0988c36c1aea8c9fc4f38')
```
