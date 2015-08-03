# price dictionary
fruit_prices = {
    "apple" : 0.60,
    "orange" : 0.25
}

# scanning fruit
fruit = input("Enter the fruit you bought in a comma separated list: ")

fruit_list = fruit.lower().split(',')

# calculate total
total = float(0.00)
for f in fruit_list:
    try:
        price = float(fruit_prices[f])
        print (f+" $"+str(price))
        total += price
    except KeyError as e:
        print (f+" is not offered at store.")

print ("Total: $"+str(total))
