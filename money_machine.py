class MoneyMachine:

    CURRENCY = "$"

    VALUES = {
        "Quarters": 0.25,
        "1 Dollar Note": 1,
        "5 Dollar Note": 5,
        "10 Dollar Note": 10
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Current profit is - {self.CURRENCY}{self.profit}")

    def process_bills(self, price):
        """Returns the total calculated from coins inserted."""
        print(f"Your Juice Price is {self.CURRENCY}{price}.")
        print("Please pay the bill by inserting coins or dollars.")
        bill_paid = False
        while not bill_paid:
            for money in self.VALUES:
                if self.money_received >= price:
                    bill_paid = True
                    break
                else:
                    self.money_received += int(
                        input(f"How many {money}?: ")) * self.VALUES[money]
            if not bill_paid:
                pay_more = price - self.money_received
                print(
                    f"Sorry that's not enough. You have to pay more ${pay_more}")
        return self.money_received

    def make_payment(self, cost, price):
        """Returns True when payment is done."""
        self.process_bills(price)
        if self.money_received >= price:
            change = round(self.money_received - price, 2)
            print(f"Here is {self.CURRENCY}{change} in change.")
            self.profit += price - cost
            self.money_received = 0
            return True

    def cash_out(self):
        print(f"Current profit is - {self.profit}")
        self.profit = 0
        print(f"Profit cashed out. Now balance is {self.profit}")
