# The item's discount and stock status have been defined
discounted = False
lowStock = True
movingProduct = lowStock or discounted

promotion = not discounted and not lowStock

print("Is the item eligible for promotion? ", promotion)