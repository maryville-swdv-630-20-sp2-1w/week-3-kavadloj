from Inheritance import *

item = Item('Item', '0.00', '0')
print(item)


pizza = Pizza()
pizza.set_quantity(2)
pizza.add_topping('Olives')
pizza.add_topping('Pepperoni')

view_item(pizza)
print(pizza.get_toppings())

breadsticks = Breadsticks('Marinara')
breadsticks.set_quantity(3)
breadsticks.set_sauce('Garlic')

view_item(breadsticks)
print(breadsticks.get_sauce())

salad = Salad('None')
salad.set_quantity(1)
salad.set_dressing('Ranch')

view_item(salad)
print(salad.get_dressing())