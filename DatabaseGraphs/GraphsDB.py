import matplotlib.pyplot as plt
import mysql.connector
import config
import random
if True:
	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd=config.Password,
		database="schooldb"
	)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("""CREATE TABLE IF NOT EXISTS students (firstname VARCHAR(255),secondname VARCHAR(255),subject VARCHAR(255), score int)""")

"""
#Function to populate database
def RandomStudentMaker(NoOfStudents):
	studentFNames = ["Alex","Brad","Diane","Jimmy","Logan","Harry","Susan","Olivia","Beth","Amy","Charles","Megan","Gareth","Tony"]
	studentSNames=["Gaston","Leslie","Copeland","Smith","Dill","Brown","Rowan","Austin","Harley","Eakin","Colgan","Fry","Cook","Laurie"]
	subjectNames=["Chemistry","Biology","Computer Science"]
	insertStudentSQL="INSERT INTO students (firstname,secondname,subject,score) VALUES(%s,%s,%s,%s)"
	
	for i in range(0,NoOfStudents):
		print("here")
		mycursor.execute(insertStudentSQL,(random.choice(studentFNames),random.choice(studentSNames),random.choice(subjectNames),random.randint(0,100)))
		mydb.commit()
RandomStudentMaker(20)
"""
subjects = ["Chemistry","Biology","Computer Science"]
def CreateScoreBarChart(subject):
	GetScoreSQL="""SELECT firstname,secondname,score FROM students WHERE subject=%s"""
	mycursor.execute(GetScoreSQL,(subject,))
	myresults = mycursor.fetchall()
	fullnames = []
	scores = []
	for person in myresults:
		fullname=person[0]+" "+person[1]
		fullnames.append(fullname)
		scores.append(person[2])
		
	plt.bar(fullnames,scores,align="center",alpha=0.5,color=['b'])
	plt.xticks(fullnames,fullnames)
	plt.ylabel("Score")
	plt.xlabel("Full Name")
	plt.title(subject+"'s Class Scores")
	plt.savefig(subject+"'s Class Scores")
	plt.show()
#CreateScoreBarChart("Chemistry")
#CreateScoreBarChart("Biology")
#CreateScoreBarChart("Computer Science")
def CreatePieChart(subjects):
	GetCount="SELECT COUNT(*) FROM students WHERE subject=%s"
	values = []
	for subject in subjects:
		mycursor.execute(GetCount,(subject,))
		count = mycursor.fetchone()[0]
		values.append(count)
	print(values)
	plt.pie(values,labels=subjects,colors=['r','g','b'],autopct='%1.1f%%')
	plt.title("Number of Students Per Subject")
	plt.axis('equal')
	plt.savefig("Number of Students Per Subject")
	
CreatePieChart(subjects)


