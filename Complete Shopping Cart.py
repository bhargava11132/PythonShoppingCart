class Product:
    def __init__(self,name,price,deal_price,ratings):
        self.name=name
        self.price=price
        self.deal_price=deal_price
        self.ratings=ratings
        self.you_save=price-deal_price
    def display_product_details(self):
        print("Name: {}".format(self.name))
        print("Price: {}".format(self.price))
        print("Deal price: {}".format(self.deal_price))
        print("Ratings: {}".format(self.ratings))
        print("You saved: {}".format(self.you_save))
class ElectronicItems(Product):
    def __init__(self,name,price,deal_price,ratings,warranty_in_months):
        super().__init__(name,price,deal_price,ratings)
        self.warranty_in_months=warranty_in_months
    def getWarranty(self):
        return self.warranty_in_months
    def display_product_details(self):
        super().display_product_details()
        print("Warranty: {}".format(self.warranty_in_months))
class GroceryItems(Product):
    def __init__(self,name,price,deal_price,ratings,expiry_date):
        super().__init__(name,price,deal_price,ratings)
        self.expiry_date=expiry_date
    def display_product_details(self):
        super().display_product_details()
        print("Expiry Date: {}".format(self.expiry_date))
class Order:
    delivery_charges={"Prime_Members":0,"Non_Prime_Members":50}
    def __init__(self,delivery_speed,delivery_address):
        self.delivery_address=delivery_address
        self.delivery_speed=delivery_speed
        self.items_in_cart=[]
    def addItems(self,product,quantity):
        self.items_in_cart.append((product,quantity))
    def display_order_details(self):
        print("----------Product Details---------")
        for product,quantity in self.items_in_cart:
            product.display_product_details()
            print("Quantity: {}".format(quantity))
        print("------------------")
        print("Delivery Speed: {}".format(self.delivery_speed))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Delivery charges: {}".format(Order.delivery_charges[self.delivery_speed]))
    def get_delivery_charges(cls):
        return Order.delivery_charges
tv=ElectronicItems("Tv",50000,40000,4,24)
keyboard=ElectronicItems("HP Keyboard",2000,1500,4.3,12)
mouse=ElectronicItems("Dell mouse",1000,850,4.2,12)

flour=GroceryItems("WheatFlour",45,41,4.0,"2nd August")
milk=GroceryItems("milk",50,40,4.5,"24th July")

order=Order("Prime_Members","Karimnagar")
order.addItems(milk,2)
order.addItems(keyboard,1)
order.display_order_details()