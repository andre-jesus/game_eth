from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["developments", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        # print(accounts[0].address)
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
