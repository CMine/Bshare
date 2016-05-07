from blockcypher import get_address_full
from blockcypher import from_satoshis
from blockcypher import get_address_overview
from blockcypher import get_total_balance
import pprint
import textwrap
import datetime

###################################################################

#VARIABLES
util_addresses = [
                  ["1C7qocA1rwv8Naj42hnMTW7uaiEN8cW6bJ"],
                  ["1879fEfLY3vbtqv8uMAZb8ycofxc6o3evp"],
                  ["14qHQKn5wyFY4vv5oHvJEtZ48na6Pqxmgn"]]
income_addresses = [
                    ["1JUxTXrEncctsRUQL31HXCaGFcQe6Sc9o6"],
                    ["1JqwAq2VSRztL2Z4o5M1vpJ1onU8vTR5dC"],
                    ["1CoeSmtxXMC4cpq1Dsbi59t2ySwEcYYBHG"],
                    ["138CtH8woNmaMUMvUsnsa5Au5jRdm72V2r"],
                    ["1BuFAoJhZMy4i8zBSr5vMPUCNzxfHnjVsN"]]
work_income = 0
util_spent= 0
other_expenses = 0

###################################################################

#FUNCTION DEFINITIONS
def convert_to_btc(satoshis):
    '''converts the satoshis value into btc for easier reading)'''
    return from_satoshis(satoshis,'btc')

def balance(walletaddress):
    '''returns the wallet's balance in btcs'''
    satoshis_val = get_total_balance(walletaddress)
    balance = convert_to_btc(satoshis_val)
    return balance

def increase_ult(value):
    '''increases the amount of btc spend on utilities'''
    global util_spent
    util_spent += value

def increase_income(value):
    '''increases the amount of btc recieved from an income provider'''
    global work_income
    work_income += value

def increase_other(value):
    '''increases the amount of btc spend on non utilities'''
    global other_expenses
    other_expenses += value

def find_output_value(listofinputs):
    '''returns the value taken out of the walletaddress'''
    for s in listofinputs:
        if (s["addresses"] == [walletaddress]):
            out_value = s["output_value"]
            return out_value

def find_input_value(listofinputs):
    '''returns the value added to the walletaddress'''
    for s in listofinputs:
        if (s["addresses"] == [walletaddress]):
            out_value = s["value"]
            return out_value

def standing50 (x):
    '''Determines wallet address' standing in regards to the 50/20/30 rule.
    50% being the max amount that should be ever spent of one's given income.
    '''
    if (x == 49 or x == 50):
        return "Watching spending"
    if (x > 50):
        return "Bad Standing"
    if (x < 50):
        return "Good Standing"

def standing20 (x):
    '''Determines wallet address' standing in regards to the 50/20/30 rule.
    20% being the principle that you should have at least 20 percent of your income
    for flexiable spending.
        '''
    if (x == 0):
        return "Bad Standing"
    if (x > 20):
        return "Good Standing"
    if (x < 19):
        return "Average Standing"
    if (x == 19 or x == 20):
        return "Perfect"

def standing30 (x):
    '''Determines wallet address' standing in regards to the 50/20/30 rule.
        30% being the principle that you should have at least 30 percent of your income
        going to your personal goals.
        '''
    if (x > 30):
        return "Bad Standing"
    if (x == 0):
        return "Bad Standing"
    if ( 10<= x >= 30):
        return "Good Standing"


def transations(walletaddress):
    
    global total_received
    global total_sent
    
    fullchain = blockcypher.get_address_full(address = walletaddress)
    transations = fullchain.get("txs")
    total_received = convert_to_btc(fullchain.get("total_received"))
    total_sent = convert_to_btc(fullchain.get("total_sent"))
    
    for i in range(len(transations)):
        inputs = (transations[i]).get("inputs")
        outputs = (transations[i]).get("outputs")
        
        input_addr = any(d['addresses'] == [walletaddress] for d in inputs)
        output_addr = any(d['addresses'] == [walletaddress] for d in outputs)
        
        if (input_addr == True):
            #address is found in the input section [spent]
            for i in range (len(util_addresses)):
                for d in outputs:
                    if(d['addresses'] == util_addresses[i]):
                        increase_ult(find_output_value(inputs))
    
        else:
            #wallet address was not found in the input section [earned]
            for i in range(len(income_addresses)):
                for d in inputs:
                    if(d['addresses'] == income_addresses[i]):
                        increase_income(find_input_value(outputs))


def final_report(username, walletaddress):
    transcript="""On %s, %s has submitted his/her wallet address: %s, for asset examination. The information presented below is based on the most recent twenty transacations available on the given blockchain."""
    
    disclaimer = """The information and views provided by BSCORE, our website and all the services we provide are believed to be reliable, but we do not accept any responsibility or liability for errors of fact or opinion. Sincere efforts have been made to present the right recommendations and the information herein is based on technical analysis and resources we consider reliable. However the information does not provide tailor-made legal advice and should be treated as only a factor, while users are encouraged to choose the options that suit them most. We do not vouch for the accuracy or the completeness of any of the information provided and are not responsible for any loss which may arise from it."""
    
    now = datetime.datetime.now()

    print ("\n")
    print ("\n".join(textwrap.wrap(transcript, width=50)) % (now.strftime("%Y-%m-%d %H:%M"),username, walletaddress))
    print ("\n")
    print ("BTC Net Flow")
    print ("##############")
    print("The Current Balance is",balance(walletaddress), "btc")
    print ("Total Sent:",total_sent, "btc")
    print ("Total Recieved:",total_received, "btc\n")
    
    print ("BTC Categorical Flow")
    print ("##############")
    x = convert_to_btc(util_spent)/ total_sent
    y = convert_to_btc(work_income)/ total_received
    z = q - total_received
    print ("Util:",convert_to_btc(util_spent), "btc", "("'{:.2f}'.format(x * 100),"%)")
    print ("Income:",convert_to_btc(work_income), "btc","("'{:.2f}'.format(y* 100),"%)\n")
    
    print ("BTC Flow Score")
    print ("##############")
    print ("Util", standing50(x))
    print ("Flex Spending", standing20(z))
    w = ((total_sent - convert_to_btc(util_spent))/total_sent *100)
    print ("Personal Goals", standing30(w))
  
  
    print ("\n")
    print ("\n".join(textwrap.wrap(disclaimer, width=50)))



if __name__ == '__main__':
    #Gather User input date: name and the wallet address
    name = input("First and Last Name: ")
    walletaddress = input("enter address: ")
    transations(walletaddress)
    final_report(name, walletaddress)

    #'1FXqE2ixnnSB1kvwbMtWma5xQ2bVbkSq3f'






