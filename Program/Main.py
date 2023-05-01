from login import Login

def normalMenu():
    print("""
          ================== MENU ==================
            1.Mencari Barang
            2.Exit
          """)
    option = input("Masukan Pilihan")
    if option == "1":
        print("Mencari Barang")
normalMenu()


def processLogin():
    loginResult = Login()
    if loginResult == "Admin Mode" :
        print("Admin")
    elif loginResult == "Normal Mode":
        normalMenu()
    else:
        print("Proses Login Gagal")
        processLogin()