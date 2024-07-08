import time

def all_sucess_call():
    print("all the conditions have been met and the user is ready to connect to the server")
    time.sleep(5)
    print("you are free to pass")
    return 

def god_function(connection = False, user = False, password = False):
    if connection == False:
        print("connection failed")
        return
    print("connection successful")
    time.sleep(5)

    if user == False:
        print("user not found")
        return
    print("user found") 
    time.sleep(5)   
    if password == False:
        print("password not found")
        return
    print("password found")
    time.sleep(5)
    all_sucess_call()
    return

con = bool(input("enter the connection status : "))
usr = bool(input("enter the user status : "))
pwd = bool(input("enter the password status : "))
god_function(con, usr, pwd)
