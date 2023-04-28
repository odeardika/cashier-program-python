import pyinputplus as pyip

def Login():        
    print("LOGIN")
    id = input("Input Id: ")
    password = pyip.inputPassword("Input Password: ")

    print(f"Id : {id}, Password : {password} ")

    idAdmin, passAdmin =  "ode", 125125
    if(id == idAdmin and password == passAdmin):
        print("Berhasil Login")
        return True
    else:
        print("Id dan Password Salah")
        return False
