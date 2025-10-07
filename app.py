# class PairValue: 

#     def __init__(self, first_val , second_val):
#         self.first_val = first_val
#         self.second_val = second_val

#     def __add__(self, other):
#         return self.first_val + other.first_val , self.second_val + other.second_val
    
#     def __isub__(self , other):
#         self.first_val -= other.first_val
#         self.second_val -= other.second_val
#         return self
    
    


# class CustomAlphabet : 
#     def __init__(self, alphabet): 
#         self.__alphabet = alphabet

#     def __len__ (self):
#         return len(self.alphabet)
    

#     def __getitem__(self):
#         return self.alphabet 

#     def __iter__(self): 
#         return iter(self.alphabet)

    
# # 



# from dataclasses import dataclass

# @dataclass
# class InventoryItems:
#     name : str
#     quantity : int
#     price : float 

#     def total_price(self): 
#         return self.quantity * self.price


# item = InventoryItems("laptop", 10, 1000)

# print(item.total_price())

class Vecteur:
    def __init__(self , components): 
        self.__components = components
        self.dimension = len(components)
    
    @property
    def coords(self): 
       return self.components
    
    def norm(self): 
        return sqrt(sum(x**2 for x in self.components))
    
    def multiplication(self, facteur):
        return sum( x* facteur for x in self.components)


    def produit(self, other): 
        return [x*y for x ,y in zip(self.components, other.components)]
    






def calculate_distance(point1): 
    point1.distance += 1
    return point1.distance






def testifnewuser(user): 

    return user.is_new

import datetime as dt

def todays_expiration(user):
    return user.iseq == dt.datetime.now()