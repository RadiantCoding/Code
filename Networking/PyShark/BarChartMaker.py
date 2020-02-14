import pyshark
import collections
import matplotlib.pyplot as plt
import numpy as np

cap = pyshark.FileCapture('sample3.pcap',only_summaries=True)
protocolList=[]
for packet in cap:
	line = str(packet)
	formattedLine= line.split(" ")
	protocolList.append(formattedLine[4])
counter = collections.Counter(protocolList)

plt.style.use('ggplot')
y_pos = np.arange(len(list(counter.keys())))
plt.bar(y_pos,list(counter.values()),align='center',alpha=0.5,color=['b','g','r','c','m'])
plt.xticks(y_pos,list(counter.keys()))
plt.ylabel("Frequency")
plt.xlabel("Protocol Name")
plt.savefig("ProtocolGraph.png")