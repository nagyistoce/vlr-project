import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
from random import shuffle
from sklearn import svm
from matplotlib import pyplot
from matplotlib import cm
import heapq

f1 = open('features.txt','r')
f2 = open('labels.txt','r')

hts_labels = []
ts_labels = []

for l in f1:
	ts_labels.append(l.strip().split('\t')[0])
f1.close()
for l in f2:
	hts_labels.append(l.strip().split('\t')[0]) 
f2.close()

lol = []
fi = open('clean_final_data.txt','r')
for line in fi:
	datum = line.split('\t')
	hts = datum[0].split(',')
	ht_is = []
	for ht in hts:
		try:
			ht_is.append(hts_labels.index(ht.lower()))	
		except ValueError:
			pass
	ts = datum[-2].split(',')
	t_is = []
	for t in ts:
		try:
			t_is.append(ts_labels.index(t.lower()))
		except ValueError:
			pass

	# make list of lists
	for hti in ht_is:
		l = []
		for ti in t_is:
			l.append(ti)
		l.append(hti)		#add label index as last element of each list
		lol.append(l)		#append list to list of lists

shuffle(lol)
s = (len(lol),len(ts_labels))
train_mat = np.zeros(s,dtype=int)
ll = []
c = 0
for l in lol:
	label = l[-1]
	inds  = l[:-1]
	ll.append(label)
	for ind in inds:
		train_mat[c,ind] += 1
	c += 1
# print(len(set(ll)))
# print(len(ll))


trm = train_mat[0:1000]
trl = ll[0:1000]
tem = train_mat[1000:]
tel = ll[1000:]
tem = trm
tel = trl

np.savetxt('train_mat.txt',trm,fmt="%d")
np.savetxt('test_mat.txt',tem,fmt="%d")

clf = svm.SVC(verbose=False,probability=True)
clf.fit(trm,trl)
res = clf.predict_proba(tem)
np.savetxt('results.txt',res,fmt="%2.4f")
resp = clf.predict(tem)

for j in range(len(tem)):
	td = ""
	for i in range(len(tem[j])):
		if(tem[j][i] == 1):
			td = td + ts_labels[i] + ";"
	tmp = sorted(range(len(res[j])), key=lambda k:res[j][k])
	ls = ""
	for ii in range(3):
		# print(hts_labels[tmp[ii]])
		ls = ls + hts_labels[tmp[ii]] + " "
	print('Data: ' + td + " Label: " + ls)

print(clf.score(tem,tel))

# # pyplot.imshow(mat[1:20,1:20], cmap=pyplot.cm.hot)    
# # pyplot.colorbar()    
# # pyplot.show()


# data = Data([
#     Heatmap(
#         z=mat,
#         x=hts_labels,
#         y=ts_labels
#     )
# ])
# plot_url = py.plot(data, filename='labelled-heatmap')