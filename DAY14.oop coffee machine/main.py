from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
coffee_maker=CoffeeMaker()
money=MoneyMachine()
menu=Menu()
should_continue=True
while should_continue:
    options=menu.get_items()
    user_choice=input(f"what would you like to have {options}").lower()
    if user_choice=="report":
        coffee_maker.report()
        money.report()
    elif user_choice=="off":
        should_continue=False
    elif user_choice=="latte" or "espresso" or "cappuccino":
        drink=menu.find_drink(user_choice)
        make_drink=coffee_maker.is_resource_sufficient(drink)
        if coffee_maker.is_resource_sufficient(drink) and money.make_payment(drink.cost):

            coffee_maker.make_coffee(drink)

