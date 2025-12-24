# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"

if "Fruits" in product_type and "Monday" in day_of_week:
	print("10% discount on Fruits today!")
elif "Vegetables" in product_type and "Tuesday" in day_of_week:
	print("15% discount on Vegetables today!")
elif "Dairy" in product_type and "Wednesday" in day_of_week:
	print("20% discount on Dairy today!")
elif "Other" in product_type:
	print("No discount available.")
else:
	print("No special discounts today.")