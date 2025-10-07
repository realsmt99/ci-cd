class Pizza: 
    def __init__(self, name , price): 
        self.name = name
        self.price = price
    

    


class CartPizza: 

    def __init__(self):
        self.pizzas = []
    


    def add_pizza(self,pizza):
        self.pizzas.append(pizza)

    @property
    def is_empty(self):
        return len(self.pizzas) == 0
    
    @property
    def number_of_pizzas(self):
        return len(self.pizzas)
    
    def add_pizza(self,pizza): 
        self.pizzas.append(pizza)
    
    def remove(self, name): 
        for pizza in self.pizzas: 
            if pizza.name == name :
                self.pizzas.remove(pizza)
                break
        raise CartPizzaException("pizza not found")




class CartPizzaException(Exception):
    def __Init__(self, message = "pizza not found"): 
        super().__init__(message)
