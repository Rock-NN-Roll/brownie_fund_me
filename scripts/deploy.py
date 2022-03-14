from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helper_scripts import(
    get_account,
    deploy_mocks,
    LOCAL_DEVELOPMENT_NETWORKS
)
def deploy_fund_me():
    account = get_account()
    # If current network is not a local dev network, ie not development and not 
    if(network.show_active() not in LOCAL_DEVELOPMENT_NETWORKS):
        price_feed_contract = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_contract = MockV3Aggregator[-1].address
    fund_me_contract = FundMe.deploy(
        price_feed_contract,
        {"from":account},
        publish_source=config["networks"][network.show_active()].get("verify")
        )
    # If I can figure out a way around VPN, turn on the publish_source to auto-verify on ETHERSCAN
    # fund_me_contract = FundMe.deploy({"from":account},publish_source=True)

    # fund_me_contract = FundMe.deploy({"from":account},publish_source=True)
    print(f"Contract deployed to {fund_me_contract.address}")
    # transaction = fund_me_contract.(,{"from": account})
    #Wait for one Block
    # transaction.wait(1)
    #  = fund_me_contract.retrieve()
    # account = accounts.load("META_MASK_PRIVATE_KEY_1")
    # account = accounts.add(os.getenv("METAMASK_PRIVATE_KEY_1"))
    # account = accounts.add(config["wallets"]["from_key"])
    # print(account)
    return fund_me_contract

def main():
    deploy_fund_me()