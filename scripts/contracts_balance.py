from brownie import NewGame
from scripts.helpful_scripts import get_account

contract_address = NewGame[-1]


def get_balance(contract_address):
    print(contract_address.contracts_balance())


def main():
    get_balance(contract_address)
