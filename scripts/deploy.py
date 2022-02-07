from brownie import NewGame
from scripts.helpful_scripts import get_account


def deploy_game():
    account = get_account()
    deploy_game = NewGame.deploy({"from": account})
    print(deploy_game.address)


def main():
    deploy_game()
