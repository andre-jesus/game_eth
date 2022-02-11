from brownie import accounts, config, network

LOCAL_BLOCKCHAIN_ENVIRONMENT = ["developments", "ganache-local"]


def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        # print(accounts[0].address)
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def mock_accounts():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        mock_1 = accounts[1]
        # print(mock_1)
        # mock_2 = accounts[2]
        # print(mock_2)
        return mock_1
    # else:
    #     return accounts.add(config["wallets"]["from_key"])


# def main():
#     mock_accounts()
