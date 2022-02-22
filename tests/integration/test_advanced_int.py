from brownie import network, AdvancedCollectible
from scripts.helpful_scripts import (
    get_account,
    get_contract,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)
from scripts.advanced_collectible.deploy_and_create import deploy_and_create_nft
import pytest
import time


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip("Only for local testing")
    #Act
    advanced_collectible, creation_transaction = deploy_and_create_nft()
    time.sleep(120)
    # Assert
    assert advanced_collectible.tokenCounter() == 1

