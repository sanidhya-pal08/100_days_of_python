MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 19
        },
        "cost": 1.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    }
}

resources = {
    "water": 800,
    "milk": 500,
    "coffee": 200,
    "money": 2.5
}


def is_resources_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins")
    total = float(input("How many quarters? ")) * 0.25
    total += float(input("How many dimes? ")) * 0.10
    total += float(input("How many nickels? ")) * 0.05
    total += float(input("How many pennies? ")) * 0.01
    return total


def make_coffee(ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]


while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == "off":
        break

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    elif choice in MENU:
        drink = MENU[choice]

        if is_resources_sufficient(drink["ingredients"]):
            money_received = process_coins()

            if money_received >= drink["cost"]:
                change = round(money_received - drink["cost"], 2)
                print(f"Here is ${change} in change.")
                make_coffee(drink["ingredients"])
                resources["money"] += drink["cost"]
                print(f"Here is your {choice}. Enjoy ☕")

            else:
                print("Sorry that's not enough money. Money refunded.")

    else:
        print("Invalid choice.")
