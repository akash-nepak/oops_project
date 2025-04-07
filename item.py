import csv
import numpy as np

class Item:
    pay_rate = 0.8   #class attributes.
    all =[]          #To store all instances of the class               
    def __init__(self,name: str,price: float,quantity=0):  #we can assign any quantity as 0 if it is not mandatory
       #run validtaion on the received input
      assert quantity >=0
      assert price >=0
      
      self.__name = name   #using __ sets name as private attribute that cannot be accessed outside the class
      self.__price = price
      self.quantity = quantity

      Item.all.append(self)
         
    @property #property decorater it read only attribute
    def name(self):
        return self.__name
     
    @property
    def price(self):  # here this method makes price attribute read only
        return self.__price
       
    @price.setter  #but @price.setter lets user to edit the attribute price anytime 
    def price(self, value):
        if value<=0:
           raise Exception("this cannot be accomodated")
        else: 

    
         self.__price = value

       
 


    def calculate_total_price(self):
        return self.__price * self.quantity 
    
    def apply_discount(self,):
        self.__price = self.__price * self.pay_rate
    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value
           
    def __repr__(self): #to represent it properly
       return f"Item('{self.name}', '{self.price}','{self.quantity}')" 
       
    @classmethod   #this Decorator works and effects the entire class 
    def instantiate_from_csv(cls): 
       with open('items.csv', 'r+') as f: # r+ is for bith reading and writing into csv file
          reader = csv.DictReader(f) 
          items = list(reader)  #converting dict into list 

          for item in items: # instantiating from the csv file.
            Item(name = item.get('name'),
                  price = float(item.get('price')), #type casting into float
                  quantity =float(item.get('quantity')))
    @staticmethod # it is a decorator has relation with class and insatance but doesnt depend on them
    def is_integer(num):
       #Counting number of floats that are point 0
       if isinstance(num,float):
          #count out the floats that are point 0
          return num.is_integer()
       elif isinstance(num,int):
          return True
       else:
          False
    
            