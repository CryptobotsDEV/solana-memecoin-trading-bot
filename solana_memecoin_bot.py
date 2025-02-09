# Scans for New Tokens — Automatically searches for newly launched tokens on Raydium via DexScreener.
# Smart Buying Logic — Filters tokens based on liquidity, volume, and market cap to avoid scams and rug pulls.
# Auto-Selling — Sells tokens when the target ROI is reached or if the token dumps.
# Fully Automated Trading — Works while you sleep!
# Telegram Alerts — Get real-time updates on buy and sell orders.

# GET FULL COMPLETE CODE HERE:
# https://cryptobots.dev/
# https://t.me/cryptobots_dev
import time
import json
import base64
from solana.rpc.api import Client
from solana.transaction import Transaction
from solana.rpc.commitment import Processed
from solana.transaction import AccountMeta, Signature
from solders.transaction import VersionedTransaction
from solders.instruction import Instruction
from solders.keypair import Keypair
from spl.token.client import Token

PRIV_KEY = "the_private_key_of_bot_wallet" # change to env variable for more security
RPC = "https://api.mainnet-beta.solana.com"

found = []
current_tokens = []
tokens_in_wallet = []
pnl_current = 0

client = Client(RPC)

def fetch_pool_keys(pair_address: str) -> dict:
    try:
        amm_id = Pubkey.from_string(pair_address) #this is token mint address
        amm_data = client.get_account_info_json_parsed(amm_id).value.data
        amm_data_decoded = LIQUIDITY_STATE_LAYOUT_V4.parse(amm_data)

def get_token_balance(mint_str: str):
    try:
        pubkey_str = str(payer_keypair.pubkey())

async def buy(pair_address: str, sol_in: float = .001, slippage: int = 10) -> bool:
    try:
        if BUYSELL == True:
            logging.warning(f"Starting buy transaction for pair address: {pair_address}")
            
            logging.warning("Fetching pool keys...")
            pool_keys = fetch_pool_keys(pair_address)
          
async def sell(pair_address: str, percentage: int = 100, slippage: int = 20) -> bool:
    try:
        if BUYSELL == True:
            logging.warning(f"Starting sell transaction for pair address: {pair_address}")


async def main():
    found_counter = 0
    total_pnl = 0
    new = ()

    while True:
        if len(new) < (max_tokens):
            await get_latest_tokens()
            new = current_tokens

if __name__ == "__main__":
    print('-' * 105)
    print(f'\nThis bot will scan https://dexscreener.com/ and trade selected tokens automatically\n\nYou can adjust the trade settings as necessary\n\n{red}[ Cryptobots.DEV ]{reset}\n')
    print('-' * 105)
    print('⚠️ Get full code at: https://cryptobots.dev/ ⚠️')
    time.sleep(99999999999)
