from brownie import NewGame
from scripts.helpful_scripts import get_account, mock_accounts
from web3 import Web3

contract_address = NewGame[-1]
amount = 1000000000000000
# winner = mock_accounts()
winner = get_account()


def fund_game(contract_address, amount):
    account = get_account()
    print(f"The deposit amount is {amount}")
    print("Funding Game!")
    contract_address.fund({"from": account, "value": amount})


def fund_to_start(account, contract_address, amount):
    print("Funding Game!")
    print(f"The {account} deposited {amount}")
    contract_address.fund({"from": account, "value": amount})


def winners_prize(contract_address, winners_address):
    contract_address.withdraw({"from": winners_address})


# def main():
#     # fund_game(contract_address, amount)
#     winners_prize(contract_address, winner)
