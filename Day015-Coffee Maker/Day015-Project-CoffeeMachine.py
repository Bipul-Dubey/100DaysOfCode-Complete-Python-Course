MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 15.00,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 25.00,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 30.00,
    }
}

profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def report(resource):
    for key, values in resource.items():
        print(key, values)


def is_resource_sufficient(order_ingredients):
    """return true when order can be made,False if ingredients"""
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Return the total calculated from coins inserted"""
    print("Please insert coins.")
    total=int(input("How many rupees??: "))
    return total


def is_transaction_successful(money_received,drink_cost):
    """Return True when the payment is accepted, False if money is insufficient"""
    if money_received>=drink_cost:
        global profit
        change=round((money_received-drink_cost),2)
        print(f"Here is Rs.{change} in change.")
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name,order_ingredients):
    """deduct the required ingredients from resources"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ☕☕")


machine_on=True
while machine_on:
    choice=input("What would you like? (espresso-15.00/latte-25.00/cappuccino-30.00):")
    if choice=='off':
        machine_on=False
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: Rs.{profit}")
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice,drink["ingredients"])