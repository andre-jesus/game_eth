from brownie import NewGame
from scripts.helpful_scripts import arbiter_account, player_account, mock_accounts

contract_address = NewGame[-1]
amount = 1000000000000000
computer_winner = mock_accounts()
player_winner = player_account()
arbiter = arbiter_account()


def fund_to_start(account, contract_address, amount):
    print("Funding Game!")
    print(f"The {account} deposited {amount}")
    contract_address.depositToGame({"from": account, "value": amount})


def winners_prize(contract_address, winners_address):
    contract_address.winner({winners_address})


def main():
    # fund_game(contract_address, amount)
    winners_prize(contract_address, player_winner)
