import blockcypher
import pprint


#functions
def convert_to_btc(satoshis):
    '''converts the satoshis value into btc for easier reading)'''
    return blockcypher.from_satoshis(satoshis,'btc')

def balance(walletaddress):
    '''returns the wallet's balance in btcs'''
    satoshis_val = blockcypher.get_total_balance(walletaddress)
    balance = convert_to_btc(satoshis_val)
    return balance 

def overview(walletaddress):
    '''gets the general overview of the wallet while also setting the
    total received btc and total sent btc'''
    global total_received 
    global total_sent     
    x = blockcypher.get_address_overview(walletaddress)
    total_received = convert_to_btc(x.get("total_received"))
    total_sent = convert_to_btc(x.get("total_sent"))
    return x

def transations(walletaddress):
    fullchain = blockcypher.get_address_full(address = walletaddress)
    transations = fullchain.get("txs")
    for i in range(len(transations)):
        print(transations[i], "\n")
        trans_value = convert_to_btc((transations[i]).get("total"))
        print(trans_value, "\n")
        outputs
    

if __name__ == '__main__':
    
    walletaddress = "1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f"
    # input("enter address: ")
    print("The Current Balance is",balance(walletaddress), "btc")
    overview(walletaddress)
    print ("Total Sent:",total_sent, "btc")
    print ("Total Recieved:",total_received, "btc")
    
    #x = blockcypher.get_address_full(address='1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f')
    #w = x.get("txs")
    transations('1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f')
    #pprint.pprint(w)
    #pprint.pprint(w[0].get("addresses"))
   
    
