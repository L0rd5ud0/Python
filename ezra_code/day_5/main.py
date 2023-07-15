'''
A function called my_discount.
The function takes no arguments but asks the user to input the price and the 
discount (percentage) of the product. 
Once the user inputs the price and discount, it calculates the price after the discount. 
The function returns the price after the discount.
'''

#create function my_discount
def my_discount(price, discount):
    discount_price = price * (discount/100)
    return price - discount_price

print(my_discount(150,15))