from menu import Menu
from juice_maker import JuiceMaker
from money_machine import MoneyMachine
from admin import Admin
from art import logo

menu = Menu()
juice_maker = JuiceMaker()
money_machine = MoneyMachine()
admin = Admin()

machine_run = True

while machine_run:
    options = menu.get_items()
    print(logo)
    print("Welcome To Our Juice Vending Machine. Here you can create your own juice from your preference.")
    print(f"Menu -\n{options}")
    flavor_choice = input("What would you like to have? - ").lower()

    if flavor_choice == 'ajbrohi':
        admin.admin_process()

    else:
        juice = menu.find_drink(flavor_choice)
        size_choice = input(
            "What size of cup would you like to have? (Large/Regular) - ").lower()
        sugar_choice = input("Do you like to have suger? (Yes/No) - ").lower()

        if juice_maker.is_resource_sufficient(juice.name) and money_machine.make_payment(juice.cost, juice.price):
            juice_maker.make_juice(juice.name, size_choice, sugar_choice)
