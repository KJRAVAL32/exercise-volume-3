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
            print(f"{product.name}--{product.code}:-")
            for a, b in product.stock_at_locations.items():
                print(a.name, b)
            print("------------------------------------------------------")
loc1 = location("warehouse", "101")
loc2 = location("store1", "102")
loc3 = location("store2", "103")
loc4 = location("store3", "104")
locations = [loc1, loc2, loc3, loc4]
prod1 = products("laptop", "001", "electric things", "60000", {loc1: 500, loc2: 0})
prod2 = products("Monitor", "002", "electric things", "100000", {loc2: 200, loc4: 10})
prod3 = products("cpu", "003", "electric things", "400000", {loc3: 20, loc4: 100})
prod4 = products("graphic card", "004", "electric things", "200000", {loc1: 900, loc2: 100})
prod5 = products("Hard disk", "005", "electric things", "10000", {loc1: 200, loc3: 100, loc4: 150, loc2: 100})
po = [prod1, prod2, prod3, prod4, prod5]
move1 = movement(loc1, loc2, prod1, 10)
move6 = movement(loc1, loc2,  prod1, 5)
move2 = movement(loc2, loc4, prod2, 20)
move3 = movement(loc3, loc4, prod3, 20)
move4 = movement(loc1, loc2, prod4, 10)
move5 = movement(loc2, loc1, prod5, 20)
movements = [move1, move2, move3, move4, move5]
print("Product Movements:-")
movement.movement_by_product(prod1, move1)
movement.movement_by_product(prod2, move2)
movement.movement_by_product(prod3, move3)
movement.movement_by_product(prod4, move4)
movement.movement_by_product(prod5, move5)
for i in locations:
    print("--------------------------------------")
    print(i.name, i.code, ":-")
    for j in po:
        if i in j.stock_at_locations.keys():
            print(j.name,j.stock_at_locations[i])
