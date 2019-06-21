import matplotlib.pyplot as plt
labels=["Full meal","Hot snack","Cold snack","Packed lunch"]
choiceData=[200,290,260,150]
colors=['b','g','r','m']
explode=[0.1,0,0,0.3]
plt.pie(choiceData,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=140,explode=explode)
plt.title("School Lunch Choice Pie Chart")
plt.axis('equal')
plt.savefig("School Lunch Pie Chart")
plt.show()
plt.clf()
