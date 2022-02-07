from brownie import NewGame
from scripts.helpful_scripts import get_account
from web3 import Web3

contract_address = NewGame[-1]
amount = 100000000000000000


def fund_game(contract_address, amount):
    contract_game = contract_address
    account = get_account()
    # fund_amount = Web3.toWei(amount, "ether")
    print(f"The deposit amount is {amount}")
    print("Funding Game!")
    contract_game.fund({"from": account, "value": amount})


def main():
    fund_game(contract_address, amount)
