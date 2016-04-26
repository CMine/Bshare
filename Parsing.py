import blockcypher
import pprint

#variables
util_addresses = [["1C7qocA1rwv8Naj42hnMTW7uaiEN8cW6bJ"], ["1879fEfLY3vbtqv8uMAZb8ycofxc6o3evp"], ['14qHQKn5wyFY4vv5oHvJEtZ48na6Pqxmgn']]
income_addresses = ["19HsbkwHRtjWpzCvXzQDL7eJRVxfg9WCz8"]
work_income = 0
util_spent = 0


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

def increase_ult(value):
    '''increases the amount of btc spend on utilities'''
    global util_spent
    util_spent += value

def incoming():
    print("I don't know if am walking on solid ground")

def transations(walletaddress):
    fullchain = blockcypher.get_address_full(address = walletaddress)
    transations = fullchain.get("txs")
    for i in range(len(transations)):
        pprint.pprint(transations[i])
        trans_value = convert_to_btc((transations[i]).get("total"))
        inputs = (transations[i]).get("inputs")
        input_addr = any(d['addresses'] == [walletaddress] for d in inputs)
        
        outputs = (transations[i]).get("outputs")
        output_addr = any(d['addresses'] == [walletaddress] for d in outputs)
        
        if (input_addr == True):
            for i in range (len(util_addresses)):
                for d in outputs:
                    if(d['addresses'] == util_addresses[i]):
                        value = d.get("value")
                        print(trans_value)
                        increase_ult(trans_value)
        else:
            print ("THAT BOY AIN'T RIGHT")
        if (output_addr == True):
            print("PROPANE AND PROPANE ACCESSORIES")
        else:
            print ("DANG IT BOBBY")




if __name__ == '__main__':
    
    name = input("First and Last Name: ")
    walletaddress = "1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f"
    # input("enter address: ")
    print("The Current Balance is",balance(walletaddress), "btc")
    overview(walletaddress)
    transations('1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f')
    print ("Total Sent:",total_sent, "btc")
    print ("Total Recieved:",total_received, "btc")
    print ("Util:",util_spent, "btc")



