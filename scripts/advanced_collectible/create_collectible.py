#!/usr/bin/python3
from brownie import AdvancedCollectible
from scripts.helpful_scripts import get_account, get_breed, fund_with_link
import time


def main():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible.address)
    transaction = advanced_collectible.createCollectible({"from": account})
    print("Waiting on second transaction...")
    # wait for the 2nd transaction
    transaction.wait(1)
    print("Collectible created!")
    #time.sleep(35)
    #requestId = transaction.events["requestedCollectible"]["requestId"]
    #token_id = advanced_collectible.requestIdToTokenId(requestId)
    #breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
    #print("Dog breed of tokenId {} is {}".format(token_id, breed))
