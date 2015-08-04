# price dictionary
fruit_prices = {
    "apple" : 0.60,
    "orange" : 0.25
}

def price_fruit(fruit_list):
    """Given a list of fruit, returns the total price"""

    total = float(0.00)
    for fruit in fruit_list:
        fruit = fruit.lower()
        try:
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
