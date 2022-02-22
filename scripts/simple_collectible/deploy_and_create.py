from brownie import SimpleCollectible
from scripts.helpful_scripts import get_account

SAMPLE_TOKEN_URI = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"
OPENSEA_URL = "https://testnets.opensea.io/assets/{}/{}"

def deploy_and_create_nft():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({"from": account})
    tx = simple_collectible.createCollectible(SAMPLE_TOKEN_URI, {"from": account})
    tx.wait(1)
    print(f"Awsome, you can now view your NFT at {OPENSEA_URL.format(simple_collectible.address, simple_collectible.tokenCounter() - 1)}")
    return simple_collectible

def main():
    deploy_and_create_nft()