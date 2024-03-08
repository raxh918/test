from bitcoinlib.wallets import Wallet
from bitcoinlib.transactions import Transaction
import random


def generate_random_words(word_file, num_words):
    with open(word_file, 'r') as file:
        words = [line.strip() for line in file]

    if len(words) < num_words:
        raise ValueError("Jumlah kata dalam file kurang dari yang diminta.")

    random_words = random.sample(words, num_words)
    return random_words

def tn():
    word_file = 'words.txt'  # Ganti dengan nama file Anda
    num_words = 1
    random_words = generate_random_words(word_file, num_words)
    return random_words

def p():
    word_file = 'words.txt'  # Ganti dengan nama file Anda
    num_words = 12
    random_words = generate_random_words(word_file, num_words)
    return random_words
        

def connect_to_wallet(wallet_name, passphrase):
    try:
        # Connect to the wallet using its name and passphrase
        wallet = Wallet(wallet_name, passphrase=passphrase)
        print("Connected to wallet:", wallet_name)
        return wallet
    except Exception as e:
        print("Error connecting to wallet:", str(e))
        return None

def check_balance(wallet):
    try:
        # Check balance of the wallet
        balance = wallet.balance()
        print("Wallet Balance:", balance)
    except Exception as e:
        print("Error checking balance:", str(e))

def send_transaction(wallet, recipient_address, amount):
    try:
        # Create a transaction
        tx = wallet.send_to(recipient_address, amount)
        print("Transaction sent. Transaction ID:", tx)
    except Exception as e:
        print("Error sending transaction:", str(e))

def main():
    # Wallet details
    wallet_name = "YourWalletName"
    passphrase = p()

def check_amount(amount):
    if amount > 0.00000000:
        print(amount)

    # Connect to the wallet
    wallet = connect_to_wallet(wallet_name, passphrase)
    if wallet:
        # Check balance
        b = check_balance(wallet)
        print(check_amount(b))

        # Example: Sending transaction
        

if __name__ == "__main__":
    main()
    