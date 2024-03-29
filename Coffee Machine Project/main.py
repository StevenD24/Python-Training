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


def check_resources(recipe):
    """Returns True if there is enough resources to make the selected drink, otherwise returns False."""
    for items in recipe:
        if recipe[items] > resources[items]:
            print(f"Sorry there is not enough {items}")
            return False
    return True


def process_coins():
    """Returns the total number of coins inserted into the coffee machine."""
    print("Please insert coins")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def transaction_successful(money_inserted, drink_cost):
    """Returns True if the transaction is successful, else returns False for an insufficient transaction."""
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"You were refunded ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that is not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Makes the coffee and depletes the resources in the coffee machine respectively."""
    for ingredients in drink_ingredients:
        resources[ingredients] -= drink_ingredients[ingredients]
    print(f"Here is your {drink_name}. Enjoy! ☕")


machine_on = True
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if check_resources(drink['ingredients']):
            payment = process_coins()
            if transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
