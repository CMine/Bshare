import blockcypher
import pprint
import textwrap
import datetime


#variables
util_addresses = [
                  ["1C7qocA1rwv8Naj42hnMTW7uaiEN8cW6bJ"],
                  ["1879fEfLY3vbtqv8uMAZb8ycofxc6o3evp"],
                  ['14qHQKn5wyFY4vv5oHvJEtZ48na6Pqxmgn']]
income_addresses = ["1JUxTXrEncctsRUQL31HXCaGFcQe6Sc9o6"]
work_income,util_spent,other_expenses = 0,0,0


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

def increase_other(value):
    '''increases the amount of btc spend on non utilities'''
    global other_expenses
    other_expenses += value

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
            #address is found in the input section [spent]
            for i in range (len(util_addresses)):
                for d in outputs:
                    if(d['addresses'] == util_addresses[i]):
                        value = d.get("value")
                        print(trans_value)
                        increase_ult(trans_value)
                    else:
                        increase_other(trans_value)
    
        else:
            #wallet address was not found in the input section [earned]
            print ("THAT BOY AIN'T RIGHT")
if (output_addr == True):
    #wallet address found in output addresses
    print("PROPANE AND PROPANE ACCESSORIES")
        else:
            #wallet address not found in outpu
            print ("DANG IT BOBBY")

def final_report(username, walletaddress):
    transcript="""On %s, %s has submitted his/her wallet address: %s, for asset examination. The information presented below is based on the most recent twenty transacations available on the given blockchain."""
    
    disclaimer = """The information and views provided by BSCORE, our website and all the services we provide are believed to be reliable, but we do not accept any responsibility or liability for errors of fact or opinion. Sincere efforts have been made to present the right recommendations and the information herein is based on technical analysis and resources we consider reliable. However the information does not provide tailor-made legal advice and should be treated as only a factor, while users are encouraged to choose the options that suit them most. We do not vouch for the accuracy or the completeness of any of the information provided and are not responsible for any loss which may arise from it."""
    
    print ("\n".join(textwrap.wrap(transcript, width=50)) % (now.strftime("%Y-%m-%d %H:%M"),username, walletaddress))
    print ("\n")
    print("The Current Balance is",balance(walletaddress), "btc")
    print ("Total Sent:",total_sent, "btc")
    print ("Total Recieved:",total_received, "btc")
    print ("Util:",util_spent, "btc")
    print ("\n")
    print ("\n".join(textwrap.wrap(disclaimer, width=50)))



if __name__ == '__main__':
    
    name = input("First and Last Name: ")
    walletaddress = "1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f"
    # input("enter address: ")
    overview(walletaddress)
    transations('1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f')
    now = datetime.datetime.now()
    final_report(name, walletaddress)






