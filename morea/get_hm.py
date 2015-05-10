import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *
from random import shuffle

from matplotlib import pyplot
from matplotlib import cm

f1 = open('idit.txt','r')
f2 = open('idiht.txt','r')

hts_labels = []
ts_labels = []

for l in f1:
	ts_labels.append(l.strip().split('\t')[0])
f1.close()
for l in f2:
	hts_labels.append(l.strip().split('\t')[0]) 
f2.close()

# shuffle(ts_labels)
# shuffle(hts_labels)
ts_labels = ts_labels[:100]
hts_labels = hts_labels[:30]

s = (len(ts_labels),len(hts_labels))
mat = np.zeros(s,dtype=float)
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
	for ti in t_is:
		for hti in ht_is:
			mat[ti,hti]+=1

for i in range(0,(mat.shape)[0]):
	s = 0
	for j in range(0,mat.shape[1]):
		s += mat[i,j]
	for j in range(0,mat.shape[1]):
		mat[i,j] /= s 

fi.close
np.savetxt('mat_bottom50.txt',mat,fmt="%f")
# pyplot.imshow(mat[1:20,1:20], cmap=pyplot.cm.hot)    
# pyplot.colorbar()    
# pyplot.show()


data = Data([
    Heatmap(
        z=mat,
        x=hts_labels,
        y=ts_labels
    )
])
plot_url = py.plot(data, filename='labelled-heatmap')