import operator

fi = open('clean_final_data.txt','r')
hts = {}
ts = {}

for line in fi:
	datum = line.split('\t')
	ht = datum[0].split(',')
	for h in ht:
		try:
			hts[h.lower()] += 1
		except KeyError:
			hts.update({h.lower():1})
	ht = datum[-2].split(',')
	for h in ht:
		try:
			ts[h.lower()] += 1
		except KeyError:
			ts.update({h.lower():1})
fi.close

sorted_ts = sorted(ts.items(), key=operator.itemgetter(1),reverse=True)
sorted_hts = sorted(hts.items(), key=operator.itemgetter(1),reverse=True)
# print(sorted_hts)
fo = open('idiht.txt','w')
for h in sorted_hts:
	fo.write(h[0] + '\t' + str(h[1]) + '\n')
fo.close()
fo = open('idit.txt','w')
for h in sorted_ts:
	fo.write(h[0] + '\t' + str(h[1]) + '\n')
fo.close()

