def all_sucess_call():
    print("all the conditions have been met and the user is ready to connect to the server")
    return 

def god_function(connection = False, user = False, password = False):
    if connection == False:
        print("connection failed")
        return
    if user == False:
        print("user not found")
        return
    if password == False:
        print("password not found")
        return
    all_sucess_call()
    return

con = bool(input("enter the connection status : "))
usr = bool(input("enter the user status : "))
pwd = bool(input("enter the password status : "))
god_function(con, usr, pwd)
