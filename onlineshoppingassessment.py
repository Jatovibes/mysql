import datetime
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv('password.env')

user = os.environ.get('user')
password = os.environ.get('password')
host = os.environ.get('host')


class Product:
    def init(self, productID, productname, category, price, stock_quantity):
     self.productID = productID
     self.productname = productname
     self.category = category
     self.price = price
     self.stock_quantity = stock_quantity


class Customer:
    def init(self, customerID, name, email, shipping_address):
        self.customerID = customerID
        self.name = name
        self.email = email
        self.shipping_address = shipping_address      

class OrderItem:
    def init(self, productID, quantity,sub_total):
        self.productID = productID
        self.quantity = quantity
        self.sub_total = sub_total

class Order:
    def init(self,orderID, customerID, total_amount):
        self.orderID = orderID
        self.customerID = customerID
        self.total_amount = total_amount


class DB:
    def __init__(self) -> None:
        self.__db = sql.connect(
            host=host,
            user=user,
            password=password,
            database='shoppingsystem'
        )    

        self.productT = 'product'
        self.customerT = 'customer'
        self.orderT = 'order'
        self.orderItem = 'order'
        self.__cursor = self.__db.cursor()

    def add_new_product(self, product: Product):
        self.__cursor.execute(f'INSERT INTO {self.productT} (name, category,price, stock_quantity) VALUES (%s, %s,%s,%s)', (product.productID, product.name, product.category, product.stock_quantity))
        self.__db.commit()

        
    def all_product(self):
        self.__cursor.execute(f'SELECT * FROM {self.productT}')
        return self.__cursor.fetchall()    

    def remove_product(self, id):
        self.__cursor.execute(f'DELETE FROM {self.productT} WHERE product_id = {id}')
        self.__db.commit()

    def update_product(self, product: Product):
        self.__cursor.execute(f'UPDATE {self.productT} SET name = {product.productname}, category = {product.category}, price = {product.price}, stock_quantity = {product.stock_quantity} WHERE product_id = {product.productID}')
        self.__db.commit()    

        

class ShoppingSystem:   
    def __init__(self) -> None:
        self.db = DB()
        self.product = []
        self.customers = []
        self.orders = []
    
    def add_product_to_db(self, product : Product):  
        for product in self.db.all_product():
            if product[1] == product.productname and product[2] == product.productname:
                raise Exception
        else:
            self.db.add_new_product(product)
            print('success') 

    def remove_product_from_db(self, productID: id ):
        for product in self.db.all_product():
            if product.productID == productID:
                self.db.remove_product(product)
                return 'removed'
            return 'not found'
        
    def update_product_info(self, productID, price, stock_quantity):    
        for product in self.db.all_product():
            if product['productID'] == productID:
                self.db.update_product
                return 'product has been updated'

        else:
            print('product not found')
    





def main():
    print("Welcome to SuperMart - Your Online Shopping Destination!")

    shopping_system = ShoppingSystem()

    while True:
        print("\n1. Browse products")
        print("2. Add a product to cart")
        print("3. View cart")
        print("4. Place an order")
        print("5. View order history")
        print("6. Register as a new customer")
        print("7. Update customer information")
        print("8. Exit")

        choice = input("\nPlease enter your choice: ")

        if choice == '1':
            # Implement browsing products functionality
        elif choice == '2':
            # Implement adding a product to cart functionality
        elif choice == '3':
            # Implement viewing cart functionality
        elif choice == '4':
            # Implement placing an order functionality
        elif choice == '5':
            # Implement viewing order history functionality
        elif choice == '6':
            # Implement registering as a new customer functionality
        elif choice == '7':
            # Implement updating customer information functionality
        elif choice == '8':
            print("Thank you for shopping at SuperMart! Goodbye!")
            shopping_system.conn.close()
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if name == "main":
    main()

