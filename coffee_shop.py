# create basic information
shop_name = 'Hello C'
coffee_size = ['Super big', 'Super medium', 'Super small']
coffee_roast = ['dark', 'light', 'local']

def order_coff(size, roast): 
    return f"Here is your {coffee_size} coffee and {coffee_roast} roasted"

# welcome customers
print(f"Welcome to {shop_name}")
print(f"We have those coffee sizes: {coffee_size}")
print(f"We have those roasted coffee: {coffee_roast}")

# ask customers' order and check
ans_size = input('Coffee size you wanna order: ')
ans_rst = input('Roasted coffee you wanna order: ')

# confirm 
print(f"Your order is {ans_size} coffee and {ans_rst} coffee")
ans_milk = input("Do you want to add milk? (Y/N)") # i want to print 2 more buttons and i want to have a box 
def add_milk(ans_milk):
    if ans_milk == 'Y':
        print('You added milk')
    else: 
        print('Continue to pay')
# any additional order? - add milk

# if yes, print out 

# give tip & thank u 
print('Thank you')






