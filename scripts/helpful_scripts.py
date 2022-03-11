from brownie import accounts, config, network
from enum import Enum

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["developments", "ganache-local"]


def player_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        account = accounts[1]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])


def arbiter_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        account = accounts[0]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])


def mock_accounts():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        mock_1 = accounts[1]
        return mock_1


def main():
    arbiter_account()


def play_again():
    play = input("Would you like to play again? Y/N \n").lower()
    if play == "y":
        player = False
        return player
    elif play == "n":
        exit()
    else:
        print("Please enter a valid answer. ")
        play_again()
