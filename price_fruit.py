# price dictionary
fruit_prices = {
    "apple" : 0.60,
    "orange" : 0.25
}

# sales dictionary
## the number represents which fruit is free
## (2 is buy one, second is free and 3 is buy 2, third is free)
sale_prices = {
    "apple": 2,
    "orange": 3
}

def onsale(fruit, current_totals):
    """Given the current fruit in the list, return if this fruit is free"""

    # add fruit to current totals
    if fruit in current_totals:
        current_totals[fruit] += 1
    else:
        current_totals[fruit] = 1

    if fruit in sale_prices:
        # if this fruit is free, don't add the price to the total
        if current_totals[fruit] % sale_prices[fruit] == 0:
            print (fruit+" $0.00")
            return True

def price_fruit(fruit_list):
    """Given a list of fruit, returns the total price"""

    current_totals = {}

    total = float(0.00)
    for fruit in fruit_list:
        fruit = fruit.lower()

        try:
            if not onsale(fruit, current_totals):
                price = fruit_prices[fruit]
                print (fruit+" $"+str(price))
                total += price
        except KeyError as e:
            print (fruit+" is not offered at store.")
    return float("%.02f"%total)


def main():
    fruits = input("Enter the fruit you bought in a comma separated list: ")
    fruit_list = fruits.split(',')

    total = price_fruit(fruit_list)

    print ("Total: $%.02f"%total)


if __name__ == '__main__':
    main()
