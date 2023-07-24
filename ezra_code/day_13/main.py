'''

'''

def your_vat():
    #Asks the user to input the price of an item
    price = float(input("What's the price of what you're buying: "))
    #Asks the user for the vat of the item in percentage
    vat = float(input("What's the vat % of what you're buying: "))/100

    return round((price * vat) + price)

print(your_vat())