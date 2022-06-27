import mysql.connector
from admin import admin_register, admin_login
from user import user_register

mydb = mysql.connector.connect(host = '127.0.0.1', user = 'root', passwd = '' , database  = 'project')
mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE project")
# mycursor.execute("SHOW DATABASES")
# for database in mycursor:
#     print(database)

# table one
# sql = "DROP TABLE admin_table"
# mycursor.execute(sql)
# mycursor.execute("CREATE TABLE user_tab (Full_name VARCHAR(30), User_id INT(6), Password VARCHAR(20))")
# sql = 'DROP TABLE user_tab'
# mycursor.execute(sql)
# mycursor.execute('CREATE TABLE admin_tab (Full_name VARCHAR(30), Admin_Id INT(6), password VARCHAR(20))')
# mycursor.execute("CREATE TABLE Question (question VARCHAR(20), option_a VARCHAR(10), option_b VARCHAR(10), option_c VARCHAR(10), answer VARCHAR(10))")

opt = input(" 1. Admin 2. User\n")
if opt == '1':
    print('1. register 2. log in\n')
    optx = input(">>>")
    if optx == '2':
        admin_login.login()
    elif optx == '1':
        admin_register.register()

elif opt == '2':
    print('1. register 2. log in\n')
    opty = input('>>>')
    if opty == '1':
         user_register.register()
    elif opty =='2':
        user_login.login()
        
else:
    quit()