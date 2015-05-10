fi = open('clean_final_data.txt','r')
fd1 = open('hashtags_dict.txt','w')
fd2 = open('tag_dict.txt','w')
for line in fi:
	data = line.split('\t')
	ht = (data[0]).split(',')
	ts = (data[-2]).split(',')
	for h in ht:
		fd1.write(h + '\n')
	for t in ts:
		fd2.write(t + '\n')



