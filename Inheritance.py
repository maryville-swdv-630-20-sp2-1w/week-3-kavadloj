class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name + ', ' + '$' + str(self.price) + ', ' + str(self.quantity) + '\n' + self.get_description()

    def get_description(self):
        return 'No description available.'
    
    def get_price(self):
        return prixe
    
    def set_quantity(self, new_quantity):
        self.quantity = new_quantity        


class Pizza(Item):
    def __init__(self):
        Item.__init__(self, 'Pizza', 6.99, 0)
        self.toppings = []
    
    def get_description(self):
        return 'Hand-tossed crust topped with sauce and cheese, with toppings of your choice.'
    
    def add_topping(self, new_topping):
        self.toppings.append(new_topping)
        
    def get_toppings(self):
        return self.toppings
            

class Breadsticks(Item):
    def __init__(self, sauce):
        Item.__init__(self, 'Breadsticks', 4.99, 0)
        self.sauce = sauce
    
    def get_description(self):
        return 'Handmade from fresh buttery-tasting dough and baked to a golden brown.'
    
    def set_sauce(self, new_sauce):
        self.sauce = new_sauce
        
    def get_sauce(self):
        return self.sauce
    
class Salad(Item):
    def __init__(self, dressing):
        Item.__init__(self, 'Salad', 3.99, 0)
        self.dressing = dressing
    
    def get_description(self):
        return 'A crisp combination of tomatoes, onion, carrots, cheese and brioche garlic croutons, all atop a blend of romaine and iceberg lettuce.'
    
    def set_dressing(self, new_dressing):
        self.dressing = new_dressing
        
    def get_dressing(self):
        return self.dressing

def view_item(item):
  print (item)

