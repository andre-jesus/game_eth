from brownie import NewGame
from scripts.helpful_scripts import arbiter_account


def deploy_game():
    account = arbiter_account()
    deploy_game = NewGame.deploy({"from": account})
    print("Contract Deployed: {deploy_game}")


def main():
    deploy_game()
