from MYSQLConnector import connect
import pyinputplus as pyip

# Add Product to System
def addProduct():
    nameProduct = input("Name of Product: ")
    priceProduct = pyip.inputInt("Price of Product: ")
    mydb = connect(addHost="localhost",addUser="root", addPassword="125125", addDB="store")
    mycursor =  mydb.cursor()
    sql = f"INSERT INTO item (nameItem, price) values (%s, %s)"
    val = (nameProduct, priceProduct)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Product Inserted")
    
# Add Register User
def registrationUser():
    userName = input("User name: ")
    userPass = 0
    while userPass != confirmPass:
        userPass = pyip.inputPassword("Input Password: ")
        confirmPass = pyip.inputPassword("Confirm Password: ")
        if userPass == "":
            print("User registration is failed")
            return 0
        if userPass != confirmPass:
            print("Password is not valid")
    is_admin = pyip.inputBool("Is admin: ")
    mydb = connect(addHost="localhost",addUser="root", addPassword="125125", addDB="store")
    mycursor =  mydb.cursor()
    sql = f"INSERT INTO users (fullname, pass, is_admin) values (%s, %s, %s)"
    val = (userName , userPass, is_admin )
    mycursor.execute(sql, val)
    mydb.commit()
    print("New user is inserted")    

# Main Menu
# Search by Product

def adminMenu():
    print("""
          Menu:
          1. Setting Database
          2. Register User
          3. Exit
          """)
    option = input("Masukan Pilihan: ")
    if option == "1":
        print("""Menu:
            1. Add New Product
            2. Edit Product Data
            3. Remove Product
            4. Exit              
              """)
        optionDB = input("Masukan Pilihan: ")
        if optionDB == "2":
            print(""" Menu
                  1. Search Name
                  2. Search ID
                  3. Exit
                  """)
        