# imports
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from art import logo
from art import separator
from time import sleep
# imports end

# objects

cashier = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

espresso = MenuItem(name="espresso", cost=1.5, coffee=18, water=50, milk=0)

cappuccino = MenuItem(name="cappuccino", cost=2.5, coffee=24, water=250, milk=100)

latte = MenuItem(name="latte", cost=3.0, coffee=24, water=200, milk=150)

# objects end

# constants
MENU = {
    espresso,
    cappuccino,
    latte,
}

MENU_TO_PRINT = "1 - Espresso ($1.5)\n2 - Cappuccino ($2.5)\n3 - Latte ($3.0)\n"
# constants end

# global variables
point = 0
beverage = None
beverage_cost = None
on = True
choice = ""
# global variables end

# functions


def interface():
    global beverage, point, beverage_cost, choice
    if point == 0:
        print("\033c", end="", flush=True)
        print(logo)
        print(separator + "\n")
        choice = input(f"Hello, what would you like?\n{MENU_TO_PRINT}\n")
        point = 1
        return

    if point == 1:
        print("\033c", end="", flush=True)
        print(logo)
        print(separator)
        decide = input(f"You selected {beverage.name}.\nIt costs {beverage_cost}.\nProceed? (y/n)\n").lower()
        sleep(0.2)
        if decide != "y":
            point = 0
            reset()
        else:
            point = 2
            return

    if point == 2:
        print("\033c", end="", flush=True)
        print(logo)
        print(separator + "\n")
        payment(beverage_cost)
        for i in range(10):
            print("*  ", end=" ", flush=True)
            sleep(1)
        sleep(1.7)
        print("\033c", end="", flush=True)
        print("\n")
        coffee_machine.make_coffee(beverage)
        sleep(7)
        point = 0


def payment(cost):
    cashier.make_payment(cost)


def reset():
    global point, beverage, beverage_cost, on, choice
    point = 0
    beverage = None
    beverage_cost = None
    on = True
    choice = ""
    main()


def main():
    global point, beverage, beverage_cost, on, choice
    while on:
        interface()
        if choice == "1" or "2" or "3":
            if choice == "1":
                choice = "espresso"
                beverage = menu.find_drink(order_name=choice)
                beverage_cost = beverage.cost
            elif choice == "2":
                beverage = menu.find_drink("cappuccino")
                beverage_cost = beverage.cost
            elif choice == "3":
                beverage = menu.find_drink("latte")
                beverage_cost = beverage.cost
            elif choice == "report":
                coffee_machine.report()
                point = 0
                sleep(10)
                reset()
            elif choice == "money":
                cashier.report()
                sleep(10)
                point = 0
                reset()
            elif choice == "off":
                on = False
                print("\033c", end="", flush=True)
                continue
            else:
                reset()
        interface()
        if coffee_machine.is_resource_sufficient(beverage):
            interface()
        else:
            print(separator + "\n")
            print(f"We're sorry, there is not enough resources to make {beverage}\n")
            available_list = []
            for item in MENU:
                beverage = item
                if coffee_machine.is_resource_sufficient(beverage):
                    available_list.append(beverage)
            if not available_list:
                print("You can get one of the following:\n")
            else:
                print("We can't make anything, someone must be about to take care of it.")
                sleep(7)
                reset()
            for available_beverage in available_list:
                print(f"{available_beverage}\n")
        interface()


# functions end

# program

while True:
    main()
    if not on:
        on = input()
        if on == "on":
            on = True

# program end
