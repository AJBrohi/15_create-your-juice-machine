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
    "apple": {
        "stock": 5
    },
    "papaya": {
        "stock": 5
    },
    "pineapple": {
        "stock": 5
    },
    "watermelon": {
        "stock": 5
    },
    "kiwi": {
        "stock": 5
    },
    "banana": {
        "stock": 5
    },
    "lemon": {
        "stock": 5
    },
    "water": 200,
    "suger": 200
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

# juice_choice = input("What would you like to have?").lower()
juice_choice = "kiwi"

# size_choice = input("What size of cup would you like to have? (Large/Regular)").lower()
size_choice = "large"

resources["water"] -= 150 if size_choice == "large" else 75
print(f"{resources['water']}")

# suger_choice = input("Do you like to have suger? (Yes/No)").lower()
suger_choice = "no"
resources["suger"] -= 0 if suger_choice == "no" else 5

print(f"Price of {juice_choice} juice is ${menu[juice_choice]['price']}")

print("Please insert the payment.")

bill_paid = False

while not bill_paid:
    for key in payment:
        if bill >= menu[juice_choice]['price']:
            bill_paid = True
            break
        else:
            bill += payment[key] * int(input(f"How many {key}? = "))
        print(bill)
    pay_more = menu[juice_choice]['price'] - bill
    print("Sorry that's not enough. You have to pay more ${pay_more}")

if bill > menu[juice_choice]['price']:
    user_return = bill - menu[juice_choice]['price']
    print(f"Here is ${user_return} in change")

print(f"Here is your {juice_choice} juice. Enjoy!!")
user_choice = input("Would you like to have juice again? (Yes/No)").lower()
