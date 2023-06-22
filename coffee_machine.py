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

def is_resource_sufficient(order_ingredient):
    """check if we have enough resources to complete the order"""
    for item in order_ingredient:
        if order_ingredient[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        return True


def process_coins():
    """To collect the coins for coffee"""
    print("please insert coins.")
    global total
    total += (int(input("how many quarters?:"))) * 0.25
    total += (int(input("how many dimes?:"))) * 0.1
    total += (int(input("how many pennies?:"))) * 0.01
    total += (int(input("how many nickles?:"))) * 0.05
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when payment is accepted and vice versa"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the dollars in {change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False
    
def make_coffee(drink_name, order_ingredients):
   """Deduct the required ingredients from the resources."""
   for item in order_ingredients:
        resources[item] -= order_ingredients[item]
   print(f"Here is your {drink_name}☕")



while coffee_machine:
    """Running the machine"""
    customer_wants = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if customer_wants == "report":
        """to show the remaining resources"""
        print(f"Water : {resources['water']}ml")
        print(f"Milk : {resources['milk']}ml")
        print(f"Coffee : {resources['coffee']}g")
        print(f"Money : ${profit}")
    elif customer_wants == "off":
        """turn off the machine"""
        coffee_machine = False
    else: 
        chosen_drink = menu[customer_wants]
        if is_resource_sufficient(chosen_drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, chosen_drink["cost"]):
                make_coffee(customer_wants, chosen_drink["ingredients"])
