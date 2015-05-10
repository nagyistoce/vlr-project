import matplotlib.pyplot as plt
import numpy
import statistics


f1 = open('idiht.txt','r')
f2 = open('idit.txt','r')

ht_fs = []
for line in f1:
	[t,f] = line.split('\t')
	ht_fs.append(int(f))
f1.close()

t_fs = []
for line in f2:
	[t,f] = line.split('\t')
	t_fs.append(int(f))
f2.close()

sd = statistics.stdev(ht_fs)
m = statistics.mean(ht_fs)
md = statistics.median(ht_fs)
print("Stats for HT: Mean" +str(m) + " Std Dev: " + str(sd) + " Median: " + str(md))

sd = statistics.stdev(t_fs)
m = statistics.mean(t_fs)
md = statistics.median(t_fs)
print("Stats for T: Mean" + str(m) + " Std Dev: " + str(sd) + " Median: " + str(md))
# dist = numpy.random.normal(m,sd,len(fs))


plt.plot(range(1,len(ht_fs)+1),ht_fs,'r')
plt.title("Distribution")
plt.xlabel("Tags & Hashtags")
plt.ylabel("Frequency")
plt.hold(True)
plt.plot(range(1,len(t_fs)+1),t_fs,'b')
plt.show()

# plt.plot(range(1,len(fs)+1),fs)
# plt.title("Distribution of ConvNet Tags")
# plt.xlabel("ConvNet Tags")
# plt.ylabel("Frequency")
# plt.show()
