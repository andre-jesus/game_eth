from brownie import NewGame
from scripts.helpful_scripts import get_account
from web3 import Web3

contract_address = NewGame[-1]
amount = 1000000000000000


def fund_game(contract_address, amount):
    account = get_account()
    print(f"The deposit amount is {amount}")
    print("Funding Game!")
    contract_address.fund({"from": account, "value": amount})


def main():
    fund_game(contract_address, amount)
