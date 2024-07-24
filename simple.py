# imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
# imports end

# variables

is_on = False

# variables end

# objects

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# objects end

# code

while True:
    while is_on:
        options = menu.get_items()
        choice = input(f"Choose: {options}\n")
        if choice == "off":
            is_on = False
        elif choice == "report":
            money_machine.report()
            coffee_maker.report()
        else:
            drink = menu.find_drink(choice)
            if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
    is_on = input()
    if is_on == "on":
        is_on = True

# code end
