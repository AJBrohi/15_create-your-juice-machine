class JuiceMaker:
    """Models the machine that makes the coffee"""

    def __init__(self):
        self.resources = {
            "apple": 5,
            "papaya": 5,
            "pineapple": 5,
            "watermelon": 5,
            "kiwi": 5,
            "banana": 5,
            "lemon": 5,
            "water": 500,
            "sugar": 30
        }

    def report(self):
        """Prints a report of all resources."""
        for key, item in self.resources.items():
            print(f"{key.capitalize()}: {item}")

    def is_resource_sufficient(self, drink):
        """Returns True when order can be made, False if ingredients are insufficient."""
        return (
            self.resources[drink] >= 1
            and self.resources['water'] >= 75
            and self.resources['sugar'] >= 5
        )

    def make_juice(self, order, size, sugar):
        """Deducts the required ingredients from the resources."""
        self.resources["water"] -= 150 if size == "large" else 75
        self.resources["sugar"] -= 5 if sugar == "yes" else 0
        print(f"Here is your {order}. Enjoy!")
