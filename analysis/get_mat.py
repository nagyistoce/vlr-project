import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *

from matplotlib import pyplot
from matplotlib import cm

f1 = open('tft.txt','r')
f2 = open('tfht.txt','r')

hts_labels = []
ts_labels = []

for l in f1:
	ts_labels.append(l.strip().split('\t')[0])
f1.close()
for l in f2:
	hts_labels.append(l.strip().split('\t')[0]) 
f2.close()


s = (len(ts_labels),len(hts_labels))
mat = np.zeros(s,dtype=int)
fi = open('clean_final_data.txt','r')
for line in fi:
	datum = line.split('\t')
	hts = datum[0].split(',')
	ht_is = []
	for ht in hts:
		ht_is.append(hts_labels.index(ht.lower()))	
	# print(ht_is)
	ts = datum[-2].split(',')
	t_is = []
	for t in ts:
		t_is.append(ts_labels.index(t.lower()))
	# print(t_is)
	# input('e')
	for ti in t_is:
		for hti in ht_is:
			mat[ti,hti]+=1

fi.close
# np.savetxt('test.txt',mat,fmt="%d")
# pyplot.imshow(mat[1:20,1:20], cmap=pyplot.cm.hot)    
# pyplot.colorbar()    
# pyplot.show()