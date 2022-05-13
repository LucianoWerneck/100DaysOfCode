MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins")
    total = int(input("How many quarters coins $0.25: $")) * 0.25
    total += int(input("How many dimes coins $0.10: $")) * 0.10
    total += int(input("How many nickles coins $0.05: $")) * 0.05
    total += int(input("How many pennies coins $0.01: $")) * 0.01
    return total


def check_coins(coin_in, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if coin_in >= drink_cost:
        global profit
        profit += drink_cost
        change = round(coin_in - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕ . Enjoy!️")


coffee_on = True

while coffee_on:
    choice = str(input("What would you like? (espresso/latte/cappuccino): "))
    if choice == 'off':
        coffee_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Coins: {profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if check_coins(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])


