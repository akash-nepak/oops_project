from item import Item
import csv
import numpy as np
class Phone (Item):#inheritance from the original class
   all = []
   def __init__(self,name:str,price:float,quantity=0,broken_Phones=0):
      #call to super function to have access to all attributes/methods
      super().__init__(name,price,quantity)
       
      assert broken_Phones >=0
      #assigning to self object in different attribute
      self.broken_phones = broken_Phones
   
   

      Phone.all.append(self) # optional to make anyways it inherits from the item class