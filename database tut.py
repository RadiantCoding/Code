import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",
    database="testdatabase"
    )
print(mydb)
mycursor = mydb.cursor()
tableSQL="""CREATE TABLE IF NOT EXISTS pupils (pupilID int,pupilName VARCHAR(255))"""
mycursor.execute(tableSQL)
print("done")
