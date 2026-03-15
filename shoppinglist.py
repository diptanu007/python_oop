class Product:
    def __init__(self,title,quantity):
        self.title = title
        self.quantity = quantity

    def __str__(self):
        return f"Product, title: {self.title}, Quantity: {self.quantity}"

    def change_quatity(self, new_quantity):
        self.quantity = new_quantity    


class ShoppingList:
    def __init__(self,title):
        self.title = title
        self.items = []

    def __str__(self):
        return f"Shopping List: {self.title}, {len(self.items)}"    

    def add(self,new_item):
        if isinstance(new_item, Product):
            self.items.append(new_item)
            print(f"{new_item} is added to the shopping list")
        else:
            print("Invalid item,not in product list")
    def show(self):
        print(f"number of items in shopping list: {len(self.items)}")
        for item in self.items:
            print(item.title,item.quantity)                