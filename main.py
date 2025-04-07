from item import Item
from phone  import Phone
from keyboard import keyboard


Item.instantiate_from_csv()

item1 = Item("my_item",750,40)

print(item1.price)
item1.apply_increment(0.4)
print(item1.calculate_total_price())
print(item1.price)

key1 = keyboard("royal-axe",1000, 10,"small")
print(key1.size)
key1.apply_discount()
print(key1.price)