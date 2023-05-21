class MenuItem:
    """Models each Menu Item."""

    def __init__(self, name, cost, price):
        self.name = name
        self.cost = cost
        self.price = price


class Menu:
    """Models the Menu with drinks."""

    def __init__(self):
        self.menu = [
            MenuItem(name="apple", cost=1, price=2),
            MenuItem(name="papaya", cost=0.5, price=1),
            MenuItem(name="pineapple", cost=0.25, price=0.5),
            MenuItem(name="watermelon", cost=1, price=2),
            MenuItem(name="kiwi", cost=2.25, price=5),
            MenuItem(name="banana", cost=0.5, price=1),
            MenuItem(name="lemon", cost=0.1, price=0.25)
        ]

    def get_items(self):
        """Returns all the names of the available menu items"""
        return "".join(f"{(item.name).capitalize()} Juice\n" for item in self.menu)

    def find_drink(self, order_name):
        """Searches the menu for a particular drink by name. Returns that item if it exists, otherwise returns None"""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")
