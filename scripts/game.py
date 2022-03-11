from webbrowser import get
from brownie import NewGame
from scripts.helpful_scripts import (
    arbiter_account,
    mock_accounts,
    player_account,
    play_again,
)
from scripts.contracts_balance import get_balance
from scripts.fund_game import fund_to_start, winners_prize
from random import randint
from enum import Enum
import time


class GameState(Enum):
    TIE = 1
    COMPUTER_WIN = 2
    PLAYER_WIN = 3


contract_address = NewGame[-1]
# Arbiter's account address
arbiter_account = arbiter_account()

# ===== Computer's Settings ======
# List of Play options
t = ["rock", "paper", "scissors"]
# assign a ramdon play to computer
computer = t[randint(0, 2)]
# assigning computer's mock account
computer_account = mock_accounts()

# ===== Player's Settings
# set player to False
player = False
# settings player's account
players_account = player_account()


# ====== Starting Game =======
while player == False:

    # ===== Set Deposit Amount =====
    amount = 10 ** 15

    # ====== GAME STARTS ======
    print("=====  ROCK,  PAPER,  SCISSORS =====")
    time.sleep(2)
    print("===  STARTING GAME ===")
    time.sleep(5)

    # == Funding contract ==
    print("Player funding contract!")
    time.sleep(2)
    fund_to_start(players_account, contract_address, amount)
    print(f"Player has deposited {amount}\n ===================================")
    print("Computer is funding the contract!")
    time.sleep(2)
    fund_to_start(computer_account, contract_address, amount)
    print(f"Computer has deposited {amount}\n ====================================")

    # Games Balance
    time.sleep(4)
    balance = get_balance(contract_address)
    print(f"The Game's banlace is {balance}")

    # Player's input
    print("=========== The Game Has Started =============")
    time.sleep(4)
    print("Player, please select one option")
    player = input("=== Rock, Paper, Scissors? ===\n").lower()

    # Computer's input
    print(f"The Computer has chosen: {computer} \n")

    # Game Play

    # === You Lose ===
    if player == computer:
        game_result = GameState.TIE
        print("you lose")
        play_again()

    elif player == "rock" and computer == "paper":
        game_result = GameState.COMPUTER_WIN
        print("you lose")
        play_again()

    elif player == "paper" and computer == "scissors":
        game_result = GameState.COMPUTER_WIN
        print("you lose")
        play_again()

    elif player == "scissors" and computer == "rock":
        game_result = GameState.COMPUTER_WIN
        print("you lose ")
        play_again()

    else:
        # === You Win ===
        game_result = GameState.PLAYER_WIN
        print("you win")
        play_again()
    player = False
    computer = t[randint(0, 2)]
