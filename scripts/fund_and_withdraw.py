from brownie import FundMe
from scripts.helper_scripts import get_account
from web3 import Web3


def fund():
    fund_me_contract = FundMe[-1]
    account = get_account()
    entrance_fee_in_Gwei = fund_me_contract.getEntranceFeeInGwei()
    print(f"The entrance Fee is {entrance_fee_in_Gwei}")

def withdraw():
    fund_me_contract = FundMe[-1]
    account = get_account()
    fund_me_contract.withdraw({"from":account})
    print(f"Withdrawing all fund to {account}")

def main():
    fund()
    withdraw()
