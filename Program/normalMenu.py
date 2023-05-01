from MYSQLConnector import connect
import re


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
    fff = input("Input Keyword : ")
    mydb = connect(addHost="localhost",addUser="root", addPassword="125125", addDB="store")      
    mycursor = mydb.cursor()
    sql = "SELECT nameItem FROM item"
    mycursor.execute(sql)
    item = mycursor.fetchall()
    # Get all items from DB
    item = [str(i)[2:-3] for i in item ]
    result = doResearch(fff, item)
    option = input("Want to search again? (y/n) ").lower()
    print(option)
    if option == "y":
        findItem()
    else:
        selectedItem = input("Select Item : ")
        print(getPrice(mycursor, selectedItem))    
findItem()