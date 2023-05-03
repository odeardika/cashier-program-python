from MYSQLConnector import connect
import re

# Research Item from Database
def doResearch(keyword, item):
    searchResult = []
    for i in item:
        if re.search(keyword+r".*", i, re.I) != None:
            print(i)
            searchResult.append(i)
    return searchResult

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
    result = doResearch(keyword, item)
    option = input("Want to search again? (y/n) ").lower()
    if option == "y":
        totalPrice, selectedItem, productPrice, quantity = findItem()
        return totalPrice, selectedItem, productPrice, quantity
    else:
        selectedItem = input("Select Item : ")
        quantity = int(input("How many want to buy? "))
        productPrice = float(getPrice(mycursor, selectedItem))
        totalPrice = productPrice * quantity 
        return totalPrice, selectedItem, productPrice, quantity
    
def calculator(count, recipt):
    totalPrice, productName, productPrice, quantity = findItem()
    count += totalPrice
    recipt = recipt + f"\n{quantity} {productName}\t{productPrice}"
    check = input("+/= :")
    if check == "+":
        resultPrice, resultRecipt = calculator(count, recipt)
        return resultPrice, resultRecipt
    else:
        return count, recipt
        
def normalMenuGUI():
    print("""
          Menu:
          1. Kalkulator
          2. Exit
          """)
    option = input("Masukan Pilihan: ")
    if option == "1":
        count = float()
        recipt =  "List Product:"
        result, recipt = calculator(count, recipt)
        print(result)
        print(recipt)

normalMenuGUI()