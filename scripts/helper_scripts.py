from brownie import network, config, accounts, MockV3Aggregator
from web3 import Web3

ETHERTOUSD = 200000000000
DECIMALS = 8

FORKED_LOCAL_NETWORKS = ["mainnet-fork"]
LOCAL_DEVELOPMENT_NETWORKS = ["development","ganache-local"]


def get_account():
    if(network.show_active() in LOCAL_DEVELOPMENT_NETWORKS or
    network.show_active() in FORKED_LOCAL_NETWORKS):
        return accounts[0]
    else:
        return accounts.add(config["wallets"][network.show_active()]["from_key"])


def deploy_mocks():
    # When there has been no MockV3Aggregator contract deployed on the chain
    # Deploy a new MockV3Aggregator
    if len(MockV3Aggregator)<=0:
        print(f"The active Network is{network.show_active()}")
        print("Deploying Mocks...")
        account = get_account()
        MockV3Aggregator.deploy(DECIMALS,ETHERTOUSD ,{"from":account})
        print("Mocks Deployed!")
