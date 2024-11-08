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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0
}
def resource_balance(name):
    if name in MENU:
        for i in MENU[name]["ingredients"].keys():

            resources[i]-=MENU[str(name)]["ingredients"][i]

    else:
        print("enter a item in the menu")
def coin_input(coin_name):
    while True:
        try:
            return int(input(f"how many {coin_name}"))
        except ValueError:
            print("enter a valid number")
def collect_cash(prize,name):
    print("please insert coin")

    no_quarters = coin_input("quarters")
    no_dimes = coin_input("dimes")
    no_nickles = coin_input("nickles")
    no_pennies = coin_input("pennies")

    total_cash=(0.25*no_quarters + 0.10*no_dimes + 0.05*no_nickles + 0.01*no_pennies)
    if total_cash==prize:
        resources["money"]+=prize
        resource_balance(name)
    elif total_cash>prize:
        resources["money"] += prize
        resource_balance(name)
        print(f"here is your change ${round(total_cash-prize,2)}")
        print(f"here is your {name} enjoy: ")
    else:
        print(f"sorry that's not enough money ,money refunded")
should_continue=True
while should_continue:
    user_choice=input("what would you like? (espresso/latte/cappuccino) ").lower()
    if user_choice=="report":
        for i in resources:
            print(f"{i}: {resources[i]}")
        continue
    elif user_choice=="off":
        should_continue=False
        continue
    resources_full = True
    for i in ["espresso", "latte", "cappuccino"]:

        if user_choice == i:
            for k in MENU[i]["ingredients"].keys():
                if MENU[i]["ingredients"][k] > resources[k]:

                    print(f"Sorry that is not enough to buy a {k}.")
                    resources_full=False
                    break

    if resources_full:
        try:
            collect_cash(prize=MENU[user_choice]["cost"], name=user_choice)
        except KeyError:
            print("enter a name correctly")


