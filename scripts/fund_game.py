from brownie import NewGame
from scripts.helpful_scripts import arbiter_account, player_account, mock_accounts

contract_address = NewGame[-1]
amount = 1000000000000000
computer_account = mock_accounts()
player_acc = player_account()
arbiter = arbiter_account()


def fund_to_start(account, contract_address, amount):
    print("Funding Game!")
    print(f"The {account} deposited {amount}")
    contract_address.depositToGame({"from": account, "value": amount})


def player1_deposit_to_game(account, contract_address, amount):
    print("Funding Game!")
    print(f"The {account} deposited {amount}")
    contract_address.player1Deposit({"from": account, "value": amount})


def player2_deposit_to_game(account, contract_address, amount):
    print("Funding Game!")
    print(f"The {account} deposited {amount}")
    contract_address.player2Deposit({"from": account, "value": amount})


def is_winner(contract_address, game_result):
    game_results = game_result.value
    if game_results == 2:
        contract_address.winner({"from": arbiter, "to": computer_account})
        print("Computer Win")
    elif game_results == 3:
        contract_address.winner({"from": arbiter, "to": player_acc})
        print("Player Win")


def main():
    # fund_game(contract_address, amount)
    pass
