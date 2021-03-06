data_file_path = 'songsSetSingers.txt'
my_dict = dict()
top10_singers = dict()
for x in ([line.rstrip('\n') for line in open(data_file_path)]):
	data = x.split('\t')
	if data[0] not in my_dict:
		my_dict[data[0]] = 1
	else:
		my_dict[data[0]] += 1
		if data[0] in top10_singers:
			top10_singers[data[0]] += 1

	if len(top10_singers) < 10:
		top10_singers[data[0]] = my_dict[data[0]]
	else:
		for y in top10_singers:
			if top10_singers[y] < my_dict[data[0]] and data[0] not in top10_singers:
				del top10_singers[y]
				top10_singers[data[0]] = my_dict[data[0]]

	 

print('Top 10 singers:')
printNum = 1
for singer in sorted(top10_singers.items(), key=lambda kv: kv[1], reverse=True):
	print(str(printNum) + '. ' + singer[0] + '\t' + str(singer[1]))
	printNum += 1
singers_num = len(my_dict)



data_file_path = 'songsSetWriters.txt'
my_dict = dict()
top10_writers = dict()
for x in ([line.rstrip('\n') for line in open(data_file_path)]):
	data = x.split('\t')
	if data[0] not in my_dict:
		my_dict[data[0]] = 1
	else:
		my_dict[data[0]] += 1
		if data[0] in top10_writers:
			top10_writers[data[0]] += 1

	if len(top10_writers) < 10:
		top10_writers[data[0]] = my_dict[data[0]]
	else:
		for y in top10_writers:
			if top10_writers[y] < my_dict[data[0]] and data[0] not in top10_writers:
				del top10_writers[y]
				top10_writers[data[0]] = my_dict[data[0]]



	 

print('\nTop 10 writers:')
printNum = 1
for writer in sorted(top10_writers.items(), key=lambda kv: kv[1], reverse=True):
	print(str(printNum) + '. ' + writer[0] + '\t' + str(writer[1]))
	printNum += 1
writers_num = len(my_dict)




data_file_path = 'songsSetComposers.txt'
my_dict = dict()
top10_composers = dict()
for x in ([line.rstrip('\n') for line in open(data_file_path)]):
	data = x.split('\t')
	if data[0] not in my_dict:
		my_dict[data[0]] = 1
	else:
		my_dict[data[0]] += 1
		if data[0] in top10_composers:
			top10_composers[data[0]] += 1

	if len(top10_composers) < 10:
		top10_composers[data[0]] = my_dict[data[0]]
	else:
		for y in top10_composers:
			if top10_composers[y] < my_dict[data[0]] and data[0] not in top10_composers:
				del top10_composers[y]
				top10_composers[data[0]] = my_dict[data[0]]



	 

print('\nTop 10 composers:')
printNum = 1
for composer in sorted(top10_composers.items(), key=lambda kv: kv[1], reverse=True):
	print(str(printNum) + '. ' + composer[0] + '\t' + str(composer[1]))
	printNum += 1
composers_num = len(my_dict)






songsS = dict()
songsW = dict()
songsC = dict()
data_file_path = 'songsSetSingers.txt'
for x in ([line.rstrip('\n') for line in open(data_file_path)]):
	data = x.split('\t')
	for singer in top10_singers:
		if data[0] == singer:
			song = ''
			for i in range(1, len(data)):
				if i == len(data) - 1:
					song += data[i]
				else:
					song += data[i] + ' '
			if singer not in songsS:
				songsS[singer] = list()
			songsS[singer].append(song)
			break


data_file_path = 'songsSetWriters.txt'
for x in ([line.rstrip('\n') for line in open(data_file_path)]):
	data = x.split('\t')
	for writer in top10_writers:
		if data[0] == writer:
			song = ''
			for i in range(1, len(data)):
				if i == len(data) - 1:
					song += data[i]
				else:
					song += data[i] + ' '
			if writer not in songsW:
				songsW[writer] = list()
			songsW[writer].append(song)
			break


data_file_path = 'songsSetComposers.txt'
for x in ([line.rstrip('\n') for line in open(data_file_path)]):
	data = x.split('\t')
	for composer in top10_composers:
		if data[0] == composer:
			song = ''
			for i in range(1, len(data)):
				if i == len(data) - 1:
					song += data[i]
				else:
					song += data[i] + ' '
			if composer not in songsC:
				songsC[composer] = list()
			songsC[composer].append(song)
			break


print('Amount of singers:',singers_num)
print('Amount of writers:',writers_num)
print('Amount of composer:',composers_num)

# for x in sorted(top10_singers.items(), key=lambda kv: kv[1], reverse=True):
# 	print(x[0] + '\t' + str(x[1]))
export = input("Export to a file?<y/n>: ")
if export == 'y':
	printNum = 1
	songsPrintNum = 1
	file_path = input("File path: ")
	with open(file_path, 'w') as f:
		f.write('Top 10 singers:\n')
		for singer in sorted(top10_singers.items(), key=lambda kv: kv[1], reverse=True):
			f.write(str(printNum) + '. ' + singer[0] + '\t' + str(singer[1]) + ':\n')
			songsPrintNum = 1
			for song in songsS[singer[0]]:
				f.write('\t' + str(songsPrintNum) + '. ' + song + '\n')
				songsPrintNum += 1
			printNum += 1
		printNum = 1
		f.write('\nTop 10 writers:\n')
		for writer in sorted(top10_writers.items(), key=lambda kv: kv[1], reverse=True):
			f.write(str(printNum) + '. ' + writer[0] + '\t' + str(writer[1]) + ':\n')
			songsPrintNum = 1
			for song in songsW[writer[0]]:
				f.write('\t' + str(songsPrintNum) + '. ' + song + '\n')
				songsPrintNum += 1
			printNum += 1
		printNum = 1
		f.write('\nTop 10 composers:\n')
		for composer in sorted(top10_composers.items(), key=lambda kv: kv[1], reverse=True):
			f.write(str(printNum) + '. ' + composer[0] + '\t' + str(composer[1]) + ':\n')
			songsPrintNum = 1
			for song in songsC[composer[0]]:
				f.write('\t' + str(songsPrintNum) + '. ' + song + '\n')
				songsPrintNum += 1
			printNum += 1
		f.write('Amount of singers: ' + str(singers_num) + '\n')
		f.write('Amount of writers: ' + str(writers_num) + '\n')
		f.write('Amount of composers: ' + str(composers_num))
print('Done')