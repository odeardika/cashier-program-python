import pyinputplus as pyip
from MYSQLConnector import connect

def getUserData(username: str):
    # According to your database
    mydb = connect(addHost="localhost",addUser="root", addPassword="125125", addDB="store")
    mycursor =  mydb.cursor()
    # MYSQL code to get pass from Database
    findPassword = "SELECT pass FROM users where fullname = "
    findIsAdmin = "SELECT is_admin FROM users where fullname = "
    
    mycursor.execute(findPassword + f"'{username}'")
    password = mycursor.fetchall()
    mycursor.execute(findIsAdmin + f"'{username}'")
    is_admin = mycursor.fetchall()
    
    dataPassword = [str(i) for i in password]
    is_admin = [i for i in is_admin]
    
    return dataPassword, is_admin
    
    


def Login():        
    print("LOGIN")
    id = input("Input Id: ")
    password = pyip.inputPassword("Input Password: ")

    print(f"Id : {id}, Password : {password} ")
    listPassword, listAdmin = getUserData(id)
    checkPassword = False
    index = 0
    # Check if password is valid
    for passwordFromDB in listPassword:
        if password == passwordFromDB[2:-3]:
            checkPassword = True
            index = listPassword.index(passwordFromDB)
            break
    # Return false if password is not valid
    if checkPassword == False:
        return False
    if listAdmin[index]:
        return "Admin Mode"
    else:
        return "Normal Mode"