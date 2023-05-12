from data import menu, resources, payment


def print_menu():
    for key in menu:
        print(key.capitalize())


def admin():
    global machine_run
    log_out = False

    while not log_out:
        print("\nWelcome to admin panel. Type to execute the options.")
        admin_choice = input(
            """Report: To see resources
Update: To update resources
Profit: To see current profit
Cash Out: To cash out the profit
Off: Logout
- """).lower()
        if admin_choice == "report":
            for key in resources:
                print(f"{key}: {resources[key]}")
        elif admin_choice == "update":
            item = input("What item would you like to add? - ").lower()
            amount = int(input("How much would you like to add? - "))
            resources[item] += amount
        elif admin_choice == "profit":
            global profit
            print(f"Current profit is - {profit}")
        elif admin_choice == "cash out":
            print(f"Current profit is - {profit}")
            profit = 0
            print(f"Profit cashed out. Now balance is {profit}")
        else:
            log_out = True
            machine_run = False


def get_cost(juice_choice):
    return menu[juice_choice]["cost"]


def get_price(juice_choice):
    return menu[juice_choice]["price"]


def update_resources(size_choice, suger_choice):
    resources["water"] -= 150 if size_choice == "large" else 75
    # print(f"water remaining - {resources['water']}")
    resources["suger"] -= 5 if suger_choice == "yes" else 0
    # print(f"suger remaining - {resources['suger']}")
    return (
        resources[juice_choice] >= 0
        and resources['water'] >= 0
        and resources['suger'] >= 0
    )


def bill_payment(juice_price):
    global bill
    bill_paid = False

    while not bill_paid:
        for key in payment:
            if bill >= juice_price:
                bill_paid = True
                break
            else:
                bill += payment[key] * int(input(f"How many {key}? = "))
            print(bill)
        if not bill_paid:
            pay_more = juice_price - bill
            print(
                f"Sorry that's not enough. You have to pay more ${pay_more}")


def update_profit(juice_cost):
    global profit, bill
    profit = profit + (bill - juice_cost)


def juice_processing(juice_choice, juice_price, juice_cost):
    global bill, machine_run

    print(f"Price of {juice_choice} juice is ${juice_price}")

    print("Please pay the bill by inserting coins or dollars.")

    bill_payment(juice_price)

    if bill > juice_price:
        user_return = bill - juice_price
        print(f"Here is ${user_return} in change")

    print(f"Here is your {juice_choice} juice. Enjoy!!")

    update_profit(juice_cost)

    user_choice = input(
        "Would you like to have juice again? (Yes/No) - ").lower()
    if user_choice == 'no':
        machine_run = False


def user(juice_choice):
    global machine_run
    juice_price = get_price(juice_choice)
    juice_cost = get_cost(juice_choice)

    size_choice = input(
        "What size of cup would you like to have? (Large/Regular) - ").lower()
    suger_choice = input("Do you like to have suger? (Yes/No) - ").lower()
    enough_resources = update_resources(size_choice, suger_choice)

    if not enough_resources:
        print("Sorry one of the item is not enough in stock. Try again later.")
        machine_run = False
    else:
        juice_processing(juice_choice, juice_price,
                         juice_cost)


profit = 0
bill = 0
machine_run = True

while machine_run:
    print("\nWelcome To Our Juice Vending Machine. Here you can create your own juice from your preference.")

    print_menu()

    juice_choice = input("What would you like to have? - ").lower()

    if juice_choice == 'ajbrohi':
        admin()
    else:
        user(juice_choice)
