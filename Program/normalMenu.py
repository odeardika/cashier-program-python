from MYSQLConnector import connect
import re

# Research Item from Database
def doResearch(keyword, item):
    for i in item:
        # search string that include the keyword in the the string, re.I set it to not case-sensitive
        if re.search(keyword+r".*", i, re.I) != None:
            print(i)

def getPrice(mycursor, item):
    sql = "SELECT price FROM item where nameItem =" + f"'{item}'"
    mycursor.execute(sql)
    price = mycursor.fetchall()
    price = [str(i)[1:-2] for i in price]
    return price[0]

def findItem():
    keyword = input("Input Keyword : ")
    mydb = connect(addHost="localhost",addUser="root", addPassword="125125", addDB="store")      
    mycursor = mydb.cursor()
    sql = "SELECT nameItem FROM item"
    mycursor.execute(sql)
    item = mycursor.fetchall()
    # Get all items from DB
    item = [str(i)[2:-3] for i in item ]
    
    doResearch(keyword, item)
    option = input("Want to search again? (y/n) ").lower()
    if option == "y":
        # Do recursion with findItem() to show list of item according to the keyword
        totalPrice, selectedItem, productPrice, quantity = findItem()
        return totalPrice, selectedItem, productPrice, quantity
    else:
        # When the item, type the item name to select it
        selectedItem = input("Select Item : ")
        quantity = int(input("How many want to buy? "))
        # To get Price of the item
        productPrice = float(getPrice(mycursor, selectedItem))
        # Get the total price according to how many its buy the item
        totalPrice = productPrice * quantity
        # Return the result to the start of the recursion (return to calculator function)
        return totalPrice, selectedItem, productPrice, quantity
    
def calculator(count, recipt):
    totalPrice, productName, productPrice, quantity = findItem()
    count += totalPrice
    recipt = recipt + f"\n{quantity} {productName}\t{productPrice}"
    check = input("+/= :")
    if check == "+":
        # Do recursion to calculate the total of spending
        resultPrice, resultRecipt = calculator(count, recipt)
        return resultPrice, resultRecipt
    else:
        # Return the result to the start of the recursion
        return count, recipt
        
def normalMenuGUI():
    print("""
          Menu:
          1. Kalkulator
          2. Show Product
          3. Exit
          """)
    option = input("Masukan Pilihan: ")
    if option == "1":
        count = float()
        recipt =  "List Product:"
        result, recipt = calculator(count, recipt)
        print(result)
        print(recipt)

normalMenuGUI()