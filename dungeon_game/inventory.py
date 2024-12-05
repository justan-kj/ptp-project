class Inventory:
    """
    A class to store items. Also has methods to manage item storage.
    """
    def __init__(self):
        """
        Initialize inventory with an empty list of items.
        :return: None
        """
        self.items = []

    def remove_item_by_name(self, item_name):
        """
        Removes the first item whose name matches item_name from the inventory's items
        :param item_name: name of the item to remove
        :return: None
        """
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return

    def add_item(self, item):
        """
        Adds an item to the inventory.
        :param item: item to add
        :return: None
        """
        self.items.append(item)

    def show(self):
        """
        Shows items in the inventory.
        :return: None
        """
        print("Inventory: ")
        for item in self.items:
            print(f"{item.name}")

    def pick_up_item(self, item, area):
        """
        removes an item from an area and places it in inventory
        :param item: item to pick up
        :param area: area to remove item from
        :return: None
        """

        self.add_item(area.items.pop())


class Item:
    """
    A simple item object with name and description.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
