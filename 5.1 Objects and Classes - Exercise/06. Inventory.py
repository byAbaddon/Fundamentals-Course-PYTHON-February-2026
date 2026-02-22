class Inventory:

    def __init__(__self, capacity):
        __self.capacity = capacity
        __self.items = []

    def add_item(self,item: str):
        if self.capacity > 0:
            self.capacity -=1
            return self.items.append(item)
        else:
            return 'not enough room in the inventory'

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self.capacity}"


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)