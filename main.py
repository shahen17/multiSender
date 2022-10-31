from web3 import web3, Web3
import time
import csv
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from config import*


web3 = Web3(Web3.HTTPProvider(data_seed))
default_address = address_default
private_key = private_k_default

def check_connection():
    return web3.isConnected()

def balance():

    balance = web3.eth.get_balance(default_address)
    format_balance = web3.fromWei(balance,'ether')
    return format_balance

def transfer(amount,address):
    nonce = web3.eth.getTransactionCount(default_address)
    tx = {
        'nonce': nonce,
        'to': address,
        'value': web3.toWei(amount, 'ether'),
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei')
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)

add_pub = []
with open('address.csv', 'r') as file:
    reader = csv.reader(file, delimiter = ',')
    for row in reader:
        add_pub.append(row)

print("<Bot by SHAHEN B>")
if check_connection() == True:
    print("Sucessfull Connection with HTTP-Provider")
start_bot = input("Type ( launch ) if config setup is done:  ")
if start_bot == "launch":
    print(f"WALLET BNB/ETH VALUE:{balance()} ")
    print(f"Number of wallets detected: {len(add_pub)}")
    s2 = float(input("Transfer amount :"))
s1 = len(add_pub)
i = s1 -1
v = 0

while v < i:
    with open('address.csv', 'r') as file:
        reader = csv.reader(file, delimiter=',')
        line_count = 0
        for row in reader:
            if line_count == v:
                result = ', '.join(str(item) for item in row)
                break
            line_count += v
    x = web3.toChecksumAddress(result)
    print(f"Transaction hash {transfer(s2,x)}")
    v = v+1
    time.sleep(8)
print("Multi-Transactions Sucessfully Completed")
print(f"Total amount sent {s2} BNB/ETH ")
print(f"WALLET BNB/ETH VALUE:{balance()} ")
