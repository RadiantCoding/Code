import matplotlib.pyplot as plt
days=[1,2,3,4,5,6,7,8,9,10]
noOfJFans=[300,500,550,800,600,700,850,600,450,300]
noOfBFans=[500,700,900,600,300,150,450,550,600,800]
plt.plot(days,noOfJFans,color="r")
plt.plot(days,noOfBFans,color="b")
plt.title("Social Networking")
plt.xlabel("Day")
plt.ylabel("Number of Fans")
plt.savefig("Social Networking Line Graph")
plt.show()
plt.clf()