def order_drink(drink_name, size = 'medium'):
    price_dict = {
        "small": 2,
        "medium": 3,
        "large": 4
    }

    print("Thank you for ordering a", size, drink_name, 'Your total is $', price_dict.get(size))

name = input()
print("do you want to specify size? (y/n):")
choice = input()

if choice[0] == 'y':
    size = input()
    order_drink(name, size)
else:
    order_drink(name)