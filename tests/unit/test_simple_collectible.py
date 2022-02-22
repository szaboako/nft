from brownie import network, SimpleCollectible, convert
from scripts.helpful_scripts import get_account, LOCAL_BLOCKCHAIN_ENVIRONMENTS
from scripts.simple_collectible.deploy_and_create import deploy_and_create_nft
import pytest


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    simple_collectible = deploy_and_create_nft()
    assert simple_collectible.ownerOf(0) == get_account()
