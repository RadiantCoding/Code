import mysql.connector
import config
import xlsxwriter
import os
mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd=config.dbpass,
	database="northwind"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT id, company, last_name, first_name, job_title FROM customers")
myresults = mycursor.fetchall()

workbook = xlsxwriter.Workbook("Customers.xlsx")
bold = workbook.add_format({'bold': True})

customerworksheet = workbook.add_worksheet("Customers")

colNum=0

for fieldname in ['id','company','last_name','first_name','job_title']:
	customerworksheet.write(0,colNum,fieldname,bold)
	colNum+=1

rowNum=1
colNum=0
for id,company,last_name,first_name,job_title in myresults:
	customerworksheet.write(rowNum,colNum,id)
	colNum+=1
	customerworksheet.write(rowNum, colNum, company)
	colNum += 1
	customerworksheet.write(rowNum, colNum, last_name)
	colNum += 1
	customerworksheet.write(rowNum, colNum, first_name)
	colNum += 1
	customerworksheet.write(rowNum, colNum, job_title)
	rowNum+=1
	colNum=0
	
	
workbook.close()
os.startfile("Customers.xlsx")
