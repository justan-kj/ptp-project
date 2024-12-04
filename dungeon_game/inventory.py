

class Inventory:
    def __init__(self):
        self.items = []

    def remove_item_by_name(self,item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return

    def add_item(self, item):
        self.items.append(item)

    def show(self):
        print("Inventory: ")
        for item in self.items:
            print(f"{item.name}")

    def pick_up_item(self, item, area):
        area.items.remove(item)
        self.add_item(item)

    def drop_item(self, item, area):
        area.items.add(item)
        self.items.remove(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description



