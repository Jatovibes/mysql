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
        self.__cursor.execute(f'INSERT INTO {self.productT} (name, category,price, stock_quantity) VALUES (%s, %s,%s,%s)', (product.productID, product.productname, product.category, product.stock_quantity))
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

    
    def get_all_data(self, tableName):
        self.__cursor.execute(f'SELECT * FROM {tableName}')
        return self.__cursor.fetchall()

    def new_customer(self, customer: Customer):
        self.__cursor.execute(f'INSERT INTO {self.customerT} (name,email,address) VALUES (%s,%s,%s)', (customer.name, customer.email, customer.shipping_address))
        self.__db.commit()

    def update_customer(self, customer: Customer):
        self.__cursor.execute(f'UPDATE {self.customerT} SET name = {customer.name}, email = {customer.email}, address = {customer.shipping_address} WHERE cust_id = {customer.customerID}')
        self.__db.commit()

    def place_order(self):
        self.__cursor.execute(f'INSERT INTO {self.orderT} (cust_id,total_amount) VALUES(%s,%s)', )
        self.__db.commit()

    def get_order(self, tableName, id):
        self.__cursor.execute(f'SELECT * FROM {tableName} WHERE cust_id = {id}')
        print(self.__cursor.fetchall())    

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

    def remove_product_from_db(self, productID):
        for product in self.db.all_product():
            if product.productID == productID:
                self.db.remove_product(product)
                return 'removed'
            return 'not found'
        
    def update_product_info(self, productID):    
        for product in self.db.all_product():
            if product['productID'] == productID:
                self.db.update_product
                return 'product has been updated'

        else:
            print('product not found')

    def register_customer(self, customer,id):
        self.db.new_customer(customer,id)
        print('new customer has been registered')   


    

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


