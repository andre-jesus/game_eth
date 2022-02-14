from brownie import NewGame


# def get_balance(contract_address):
#     print(contract_address.contracts_balance())


contract_address = NewGame[-1]


def get_balance(contract_address):
    return contract_address.contracts_balance()


def main():
    get_balance(contract_address)
