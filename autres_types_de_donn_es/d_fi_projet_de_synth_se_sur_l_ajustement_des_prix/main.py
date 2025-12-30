grocery_inventory = {"Milk":("Dairy",3.50,8),"Eggs":("Dairy",5.50,30),"Bread":("Bakery",2.99,15),"Apples":("Produce",1.50,50)}

print(grocery_inventory)
eggs_type, eggs_price, eggs_count = grocery_inventory["Eggs"]
milk_type, milk_price, milk_count = grocery_inventory["Milk"]
apple_type, apple_price,apple_count = grocery_inventory["Apples"]
apple_price = grocery_inventory ["Apples"][1]

if eggs_price > 5:
    print("eggs are too expensive, reducing the price by $1.")
    grocery_inventory["Eggs"] = eggs_type,eggs_price -1,eggs_count
else:
    print("Eggs price is correct")

print(grocery_inventory)

grocery_inventory["Tomatoes"] = ("Produce",1.20,30)
print("Inventory after adding Tomatoes:", grocery_inventory )

if milk_count < 10:
    print("milk needs to be restocked. Increasing stock by 20 units.")
    grocery_inventory["Milk"] = (milk_type, milk_price, milk_count + 20)
    
else:
    print("Milk are sufficiently stock")
    
if apple_price > 2:
    grocery_inventory.pop("Apples")
    print("Apples removed from inventory due to high price.")

print("updated inventory:", grocery_inventory)