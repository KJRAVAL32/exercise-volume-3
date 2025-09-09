class products:
    def __init__(self,name,code,categeoy,price,stock_at_locations):
        self.name = name
        self.code = int(code)
        self.categeoy = categeoy
        self.price = int(price)
        self.stock_at_locations=stock_at_locations
class location:
    def __init__(self,name,code):
        self.name=name
        self.code=int(code)
class movement(products):
    def __init__(self,from_location,to_location,product,quantity):
        self.from_location=from_location
        self.to_location=to_location
        self.product=product
        self.quantity=int(quantity)
    @staticmethod
    def movement_by_product(product,move):
        print(f"Product: {move1.product} : {move1.from_location}  --> {move1.to_location}  Quantity: {move1.quantity}")
        print(f"Product: {move2.product} : {move2.from_location}  --> {move2.to_location}  Quantity: {move2.quantity}")
        print(f"Product: {move3.product} : {move3.from_location}  --> {move3.to_location}  Quantity: {move3.quantity}")
        print(f"Product: {move4.product} : {move4.from_location}  --> {move4.to_location}  Quantity: {move4.quantity}")
        print(f"Product: {move5.product} : {move5.from_location}  --> {move5.to_location}  Quantity: {move5.quantity}")
        print("------------------------------------------------------------------------------------")
        if product.stock_at_locations[move.from_location] < move.quantity:
            print("Not have stock")
        else:
            product.stock_at_locations[move.from_location]-=move.quantity
            product.stock_at_locations[move.to_location]+=move.quantity
        print("Stock at locations:")
        print(f"{product.name}-{product.code}:{product.stock_at_locations}")
        print("---------------------------------------------------------------------")
loct1=location("warehouse","101")
loct2=location("store1","102")
loct3=location("store2","103")
loct4=location("store3","104")
prod1=products("laptop","001","electric things","60000",{'warehouse':500,'store1':0})
prod2=products("Monitor","002","electric things","100000",{'store1':200,'store3':10})
prod3=products("cpu","003","electric things","400000",{'store2':20,'store3':100})
prod4=products("graphic card","004","electric things","200000",{'warehouse':900,'store1':100})
prod5=products("Hard disk","005","electric things","10000",{'warehouse':200,'store2':100,'store3':150,'store1':10})
# movements=[
move1=movement("warehouse","store1","laptop",10)
move6=movement("warehouse","store1","laptop",5)
move2=movement("store1","store3","monitor",20)
move3=movement("store2","store3","cpu",20)
move4=movement("warehouse","store1","graphic card",10)
move5=movement("store1","warehouse","hard disk",200)
# ]
print("Product Movements:")
movement.movement_by_product(prod1,move1)
movement.movement_by_product(prod2,move2)
movement.movement_by_product(prod3,move3)
movement.movement_by_product(prod4,move4)
movement.movement_by_product(prod5,move5)
movement.movement_by_product(prod5,move6)
