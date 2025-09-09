class products:
    def __init__(self, name, code, categeoy, price, stock_at_locations):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)
        self.stock_at_locations = stock_at_locations
class location:
    def __init__(self, name, code):
        self.name = name
        self.code = int(code)
class movement(products):
    def __init__(self, from_location, to_location, product, quantity):
        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = int(quantity)
    @staticmethod
    def movement_by_product(product, move):
        for i in movements:
            print(f"Product: {i.product.name} : {i.from_location.name}  --> {i.to_location.name}  Quantity: {i.quantity}")
        print("------------------------------------------------------------------------------------")
        if product.stock_at_locations[move.from_location] < move.quantity:
            print("Not have stock")
        else:
            product.stock_at_locations[move.from_location] -= move.quantity
            product.stock_at_locations[move.to_location] += move.quantity
        print("Stock at locations:")
        print(f"{product.name}-{product.code}:{product.stock_at_locations}")
        print("---------------------------------------------------------------------")

loc1 = location("warehouse", "101")
loc2 = location("store1", "102")
loc3 = location("store2", "103")
loc4 = location("store3", "104")
locations = [loc1, loc2, loc3, loc4]
prod1 = products("laptop", "001", "electric things", "60000", {'warehouse': 500, 'store1': 0})
prod2 = products("Monitor", "002", "electric things", "100000", {'store1': 200, 'store3': 10})
prod3 = products("cpu", "003", "electric things", "400000", {'store2': 20, 'store3': 100})
prod4 = products("graphic card", "004", "electric things", "200000", {'warehouse': 900, 'store1': 100})
prod5 = products("Hard disk", "005", "electric things", "10000", {'warehouse': 200, 'store2': 100, 'store3': 150, 'store1': 10})
po = [prod5, prod4, prod3, prod2, prod1]
# movements=[
move1 = movement(loc1, loc2, prod1, 10)
move6 = movement(loc1, loc2,  prod1, 5)
move2 = movement(loc2, loc4, prod2, 20)
move3 = movement(loc3, loc4, prod3, 20)
move4 = movement(loc1, loc2, prod4, 10)
move5 = movement(loc2, loc1, prod5, 200)
movements = [move5, move4, move3, move2, move1]
# ]
print("Product Movements:")
movement.movement_by_product(prod1, move1)
movement.movement_by_product(prod2, move2)
movement.movement_by_product(prod3, move3)
movement.movement_by_product(prod4, move4)
movement.movement_by_product(prod5, move5)
movement.movement_by_product(prod5, move6)
for i in locations:
    print("--------------------------------------")
    print(i.name, i.code, ":")
    for j in po:
        if i.name in j.stock_at_locations:
            print(j.name,j.stock_at_locations[i.name])
