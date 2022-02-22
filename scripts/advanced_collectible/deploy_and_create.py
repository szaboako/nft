from brownie import AdvancedCollectible, network, config
from scripts.helpful_scripts import fund_with_link, get_account, OPENSEA_FORMAT, get_contract

#SAMPLE_TOKEN_URI = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"

def deploy_and_create_nft():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        {"from": account},
    )
    fund_with_link(advanced_collectible.address)
    create_nft_tx = advanced_collectible.createCollectible({"from": account})
    create_nft_tx.wait(1)
    print("New token has been created!")
    return advanced_collectible, create_nft_tx
    

def main():
    deploy_and_create_nft()