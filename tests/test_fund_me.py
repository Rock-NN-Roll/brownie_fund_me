from black import get_cache_info
from brownie import FundMe, accounts,config,network,exceptions
import pytest
from scripts.fund_and_withdraw import fund
from scripts.helper_scripts import get_account,deploy_mocks,MockV3Aggregator,LOCAL_DEVELOPMENT_NETWORKS,FORKED_LOCAL_NETWORKS
from scripts.deploy import deploy_fund_me

def test_can_fund_and_withdraw():
    account = get_account()
    fund_me_contract = deploy_fund_me()
    entrance_fee = fund_me_contract.getEntranceFeeInGwei()+100
    tx = fund_me_contract.fund({"from":account,"value": entrance_fee})
    tx.wait(1)
    assert fund_me_contract.addressToAmountFunded(account.address) == entrance_fee
    tx2 = fund_me_contract.withdraw({"from":account})
    tx2.wait(1)
    assert fund_me_contract.addressToAmountFunded(account.address) == 0

def test_only_owner_can_withdraw():
    if network.show_active() not in LOCAL_DEVELOPMENT_NETWORKS and network.show_active() not in FORKED_LOCAL_NETWORKS:
        pytest.skip("Only for local testing!")
    bad_actor = accounts.add()
    fund_me_contract = deploy_fund_me()
    with pytest.raises(exceptions.VirtualMachineError):
        fund_me_contract.withdraw({"from":bad_actor})
    