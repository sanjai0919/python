
from ast import While
from multiprocessing import connection
from sqlite3 import connect
from tkinter import Menu
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password= "1234",
    database = "atm_db"
    

)
mycursor = mydb.cursor()
#mycursor.execute("create table customer_data1(name varchar(300),id int,deposit int,pin int)")


print("successfully")

print("\t\t\t\t\tWELCOME TO SNA BANK ATM !!!\t\t\t\t\t")

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("press 1 for login")
print("press  0 for create new account")
n = int(input("Enter the number:\t"))

name = ""
id=""
deposit= ""
pin = ""


you_name=name
account = id
amount=deposit
password = pin


sql= "insert into customer_data1(name,id,deposit,pin) values ('{}','{}','{}','{}')".format(name,id,deposit,pin)


mycursor = mydb.cursor()

mycursor.execute(sql)

mydb.commit()
print("successfully")



if n==0 :
        You_Name = input("enter name:\t")
        accout = int(input("enter account no:\t  "))
        amount = int(input("enter starting account you want deposite:\t"))
        password = int(input("enter your password:\t"))
        
   
       
        





if n ==1:
    info = int(input("enter your id:\t"))
    pin = int(input("enter pin:\t "))
    mycursor = mydb.cursor()
    mycursor.execute("""SELECT * FROM customer_data1 where id='%s'"""%(info))
    row = mycursor.fetchone()
    
    if mycursor.rowcount == 1:
        mycursor.execute("""SELECT * FROM customer_data1 where pin='%s'"""%(pin) )
        row = mycursor.fetchone()
        

        if mycursor.rowcount ==1:
            print("login successfully\t\n")
            print("PRESS (W) OR (1) for withdrawl")
            print("PRESS (D) OR (2) for deposit")
            print("PRESS (T) OR (3) for total balance")
            print("PRESS (E) OR (4) for exit")


            d = (input("enter the number (OR) key for next move:\t"))
            if d == 1 or"W":
                a = int(input("Enter the amount you withdrawl: RS.\t₹"))
                mycursor.execute("""SELECT deposit FROM customer_data1 where pin='%s'"""%(pin))


                col = mycursor.fetchone()
                x= list(col)
                for i in x:
                    z = (int(i))
                    c = z-a

                mycursor.execute("UPDATE customer_data1 SET deposit='%s' where pin='%s'"%(c,pin))


            if d == 2 or"D":
                b= int(input("enter the amount you deposite:RS.\t₹"))
                mycursor.execute("""SELECT deposit FROM customer_data1 where pin='%s'""" % (pin))  
                col = mycursor.fetchone()
                x = list(col)
                for i in x:
                    z = (int(i))
                    c = z +b
                mycursor.execute("UPDATE customer_data1 SET deposit='%s' where pin='%s'"%(c,pin))


            if d == 3 or "T":
                mycursor.execute("SELECT deposite FROM customer_data1 where pin='%s"%(pin))
                col = mycursor.fetchone()
                c = z -a or z+b

                mycursor.execute("UPDATE customer_data1 SET deposit='%s' where pin='%s'"%(c,pin) )    




            if d == 4 or"E":
                user_exit=input("you want to exit ? yes/no:\t")
                if user_exit == "y":
                    print("Thank you for using SNA atm !!!")
                    exit(0)
                else :
                    exit(1)



            else:
                print("invalid password")        




        else:
            print("account doen't exit")
            mydb.commit()                    






 