from MYSQLConnector import connect
# Add Product to System
def addProduct(nameProduct, priceProduct : int):
    mydb = connect(addHost="localhost",addUser="root", addPassword="125125", addDB="store")
    mycursor =  mydb.cursor()
    sql = f"INSERT INTO item (nameItem, price) values (%s, %s)"
    val = (f"{nameProduct}", priceProduct)
    mycursor.execute(sql, val)
    mydb.commit()
    print("Product Inserted")
    
# Add Register User
def registrationUser():
    pass
# Add Admin User
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
        