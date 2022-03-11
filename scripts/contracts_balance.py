from brownie import NewGame

contract_address = NewGame[-1]


def get_balance(contract_address):
    balance = contract_address.totalGameBalance()
    print(balance)
    return balance


def main():
    get_balance(contract_address)
