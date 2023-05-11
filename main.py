menu = {
    "apple": {
        "cost": 1,
        "price": 2
    },
    "papaya": {
        "cost": 0.5,
        "price": 1
    },
    "pineapple": {
        "cost": 0.25,
        "price": 0.5
    },
    "watermelon": {
        "cost": 1,
        "price": 2
    },
    "kiwi": {
        "cost": 2.25,
        "price": 5
    },
    "banana": {
        "cost": 0.5,
        "price": 1
    },
    "lemon": {
        "cost": 0.1,
        "price": 0.25
    }
}

resources = {
    "apple": 5,
    "papaya": 5,
    "pineapple": 5,
    "watermelon": 5,
    "kiwi": 5,
    "banana": 5,
    "lemon": 5,
    "water": 200,
    "suger": 50
}

payment = {
    "Quarter": 0.25,
    "1 Dollar Note": 1,
    "5 Dollar Note": 5,
    "10 Dollar Note": 10
}
profit = 0
bill = 0

print("Welcome To Our Juice Vending Machine. Here you can create your own juice from your preference.")

for key in menu:
    print(key.capitalize())

juice_choice = input("What would you like to have? - ").lower()
if juice_choice == 'ajbrohi':
    admin_choice = input(
        "Report: To see resources \nUpdate: To update resources \n- ").lower()
    if admin_choice == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
    elif admin_choice == "update":
        item = input("What item would you like to add? - ").lower()
        amount = int(input("How much would you like to add? - "))
        resources[item] += amount
    elif admin_choice == "profit":
        print(f"Current profit is - {profit}")

else:
    juice_price = menu[juice_choice]["price"]
    juice_cost = menu[juice_choice]["cost"]

    size_choice = input(
        "What size of cup would you like to have? (Large/Regular) - ").lower()

    resources["water"] -= 150 if size_choice == "large" else 75
    print(f"water remaining - {resources['water']}")

    suger_choice = input("Do you like to have suger? (Yes/No) - ").lower()
    resources["suger"] -= 0 if suger_choice == "no" else 5
    print(f"suger remaining - {resources['suger']}")

    if resources[juice_choice] <= 0 or resources['water'] <= 0 or resources['suger'] <= 0:
        print("Sorry one of the item is not enough in stock. Try again later.")

    else:
        print(f"Price of {juice_choice} juice is ${juice_price}")

        print("Please insert the payment.")

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

        if bill > juice_price:
            user_return = bill - juice_price
            print(f"Here is ${user_return} in change")

        print(f"Here is your {juice_choice} juice. Enjoy!!")
        profit = bill - juice_cost
        user_choice = input(
            "Would you like to have juice again? (Yes/No) - ").lower()
