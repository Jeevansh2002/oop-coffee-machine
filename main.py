from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

while is_on:
    a = menu.get_items()
    choice = input(f"Which drink would you like to have {a}: ").lower()
    if choice == 'off':
        is_on=False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            print(money_machine.make_payment(drink.cost))
            coffee_maker.make_coffee(drink)











