# Store sensor data and datetime in a persistent media (MySQL or local file) (6)

dataBase = mysql.connector.connect(

    host="localhost",

    user="root",

    passwd="",

    database="hdsd"
)


cursorObject = dataBase.cursor()
f = open("Report.txt", "r")
end_of_file = f.readline()
for x in f:
    res = x.split()
    sql = "INSERT INTO tbl_STUDENT (NAME, EMAIL) VALUES (%s, %s)"
    val = (str(res[0]), str(res[1]))
    cursorObject.execute(sql, val)
    dataBase.commit()
    if not end_of_file:
        break