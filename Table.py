# importing required libraries

import mysql.connector

  

dataBase = mysql.connector.connect(

  host ="localhost",

  user ="root",

  passwd ="",

  database = "hdsd"
)
 
# preparing a cursor object

cursorObject = dataBase.cursor()

  

sql = "INSERT INTO STUDENT (NAME, EMAIL) VALUES (%s, %s) "

val = ("Yuki Sato", "lhsato.kh@gmail.com")

   
cursorObject.execute(sql, val)
dataBase.commit()

val = ("Karla Sato", "kmsato15@gmail.com")
cursorObject.execute(sql, val)
dataBase.commit()
   
val = ("Soy Hok", "soyhok2018@gmail.com")
cursorObject.execute(sql, val)
dataBase.commit()

# disconnecting from server
dataBase.close()