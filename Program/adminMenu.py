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

def inputKeywordPrice(type):
    if type == 1:
        q = "Input the product name: "
    elif type == 2:
        q = "Input the product id"
    keyword = input(q)
    newPrice = pyip.inputInt("Add the new price: ")
    return keyword, newPrice


def showSearchProduct(typeKey, mycursor):
    if typeKey == 1:
        q = "Input the product name: "
    elif typeKey == 2:
        q = "Input the product id"
    keyword = input(q)
    mycursor.execute(f"SELECT * FROM item WHERE nameItem = '{keyword}'")
    item = mycursor.fetchall()
    print(type(item))
    print()
    for i in item:
        print(i)
    option = input("Want to search again?y/n").lower()
    if option == "y":
        showSearchProduct()
        return 0
    else :
        return 0

# Search by Product
def searchAndUpdateProduct(type : int):
    mydb = connect(addHost="localhost",addUser="root", addPassword="125125", addDB="store")
    mycursor =  mydb.cursor()
    showSearchProduct(type, mycursor)
    keyword, newPrice = inputKeywordPrice(type)
    #search by itemName
    if type == 1 :
        sql = f"UPDATE item SET price = {newPrice} WHERE nameItem = '{keyword}'"
    #search by id
    elif type == 2:
        sql = f"UPDATE item SET price = {newPrice} WHERE id = '{keyword}'"
    
    mycursor.execute(sql)
    mydb.commit()

searchAndUpdateProduct(type=1)

#Show Database

def adminMenu():
    print("""
          Menu:
          1. Setting Database
          2. Register User
          3. Show Database
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
        