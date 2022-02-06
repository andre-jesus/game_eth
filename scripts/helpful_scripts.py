from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["developments", "ganache-local"]


def get_account():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
