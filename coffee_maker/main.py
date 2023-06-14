# TODO 1: write menu
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

# TODO 1: Ask what the user want

customer_wants = input("What would you like? (espresso/latte/cappuccino):").lower()

coffee_machine = False
total = 0
def coffee_type():
    customer_wants = input("What would you like? (espresso/latte/cappuccino):").lower()


def payment():
    print("please insert coins.")
    total += (int(input("how many quarters?:"))) * 0.25
    total += (int(input("how many dimes?:"))) * 0.1
    total += (int(input("how many pennies?:"))) * 0.01
    total += (int(input("how many nickles?:"))) * 0.05



    # if customer_wants == "off":
    #     coffee_machine = True
    # coffee_machine = True
