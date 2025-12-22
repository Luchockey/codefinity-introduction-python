grocery_item = "Grilled Chicken Salad"
length_of_item = len(grocery_item)
first_char = len(grocery_item[0])
second_char = len(grocery_item[8])
third_char = len(grocery_item[16])
last_char1 = len(grocery_item[-15])
last_char2 = len(grocery_item[-7])
last_char3 = len(grocery_item[-1])


# Testing
print("Length of item name:", length_of_item)
print("First character of each word:", first_char, second_char, third_char)
print("Last character of each word:", last_char1, last_char2, last_char3)