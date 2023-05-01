from login import Login

def processLogin():
    loginResult = Login()
    if loginResult == "Admin Mode" :
        print("Admin")
    elif loginResult == "Normal Mode":
        print("Normal")
    else:
        print("Proses Login Gagal")
        processLogin()
processLogin()