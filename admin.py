from juice_maker import JuiceMaker
from money_machine import MoneyMachine
from art import admin_logo


class Admin:
    def __init__(self):
        self.log_out = False

    def admin_process(self):
        global machine_run
        money_machine = MoneyMachine()
        juice_maker = JuiceMaker()

        print(admin_logo)

        while not self.log_out:
            print("Welcome to admin panel. Type to execute the options.")
            admin_choice = input(
                """Report: To see resources
Update: To update resources
Profit: To see current profit
Cash Out: To cash out the profit
Off: Logout
- """).lower()
            if admin_choice == "report":
                juice_maker.report()
            elif admin_choice == "update":
                item = input("What item would you like to add? - ").lower()
                amount = int(input("How much would you like to add? - "))
                juice_maker.resources[item] += amount
            elif admin_choice == "profit":
                money_machine.report()
            elif admin_choice == "cash out":
                money_machine.cash_out()
            else:
                self.log_out = True
                machine_run = False
