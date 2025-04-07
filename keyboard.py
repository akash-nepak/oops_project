import numpy as np
from item import Item

class keyboard(Item): 
    all = []
    pay_rate =  .8


    def __init__(self,name :str, price :float, quantity :float, size :str):

        super().__init__(name,price,quantity,)

        self.size = size

        keyboard.all.append(self)


