from shoppinglist import ShoppingList,Product

list1 = ShoppingList("grocery")
product1 =Product("apple",30)
product2 = Product("Milk", 2)
product3 = Product("Cheese", 2)


list1.add(product1)
list1.add(product2)
list1.add(product3)
list1.add("Banana")
print(list1)
list1.show()