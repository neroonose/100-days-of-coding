# TODO 1: write menu
menu = {
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

resources = {"water": 300,
           "milk": 200 ,
           "coffee": 100}

coffee_machine = True
total = 0
profit = 0

def payment():
    """To collect the coins for coffee"""
    print("please insert coins.")
    total += (int(input("how many quarters?:"))) * 0.25
    total += (int(input("how many dimes?:"))) * 0.1
    total += (int(input("how many pennies?:"))) * 0.01
    total += (int(input("how many nickles?:"))) * 0.05
    return total


while coffee_machine:
    """Running the machine"""
    customer_wants = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_wants == "report":
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    elif customer_wants == "off":
        coffee_machine = False
    else: 
        choosen_drink = (menu[customer_wants])
