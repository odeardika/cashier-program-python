import mysql.connector

def connect(addHost, addUser, addPassword, addDB):
    mydb = mysql.connector.connect(
        host = addHost,
        user = addUser,
        password = addPassword,
        database = addDB, 
    )
    return mydb