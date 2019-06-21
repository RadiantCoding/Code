import matplotlib.pyplot as plt
instruments = ["Guitar","Trumpet","Drum","Saxophone","Piano"]
salesData=[630,720,405,540,405]
y_pos = sorted(instruments)

plt.bar(y_pos,salesData,align='center',alpha=0.5,color=['b','g','r','c','m'])
plt.xticks(y_pos,instruments)
plt.xlabel("Instrument Name")
plt.ylabel("Amount Sold")
plt.title("Happy Rhythms Music Store Sales Bar Chart")
plt.savefig("Happy Rhythms Bar Chart")
plt.show()
plt.clf()
