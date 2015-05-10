
f1 = open('td.txt','r')
f2 = open('htd.txt','r')

hts_labels = []
ts_labels = []

for l in f1:
	ts_labels.append(l.strip().split('\t')[0])
f1.close()
for l in f2:
	hts_labels.append(l.strip().split('\t')[0]) 
f2.close()

comm = set(ts_labels) & set(hts_labels)
print(comm)
