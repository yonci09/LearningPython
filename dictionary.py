for key, value in {}.fromkeys("123456789", "pythonlearning").items():
    print(key, value)
 
fruit_items = {"menu1": "strawberry", "menu2": "apple", "menu3": "blueberry"}
print(fruit_items.pop("menu2"))
 
fruit_items.popitem()
print(fruit_items)