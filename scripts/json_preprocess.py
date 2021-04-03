import json
from pandas.io.json import json_normalize
import os
import sys

def write_in_file(file_name, data):
	with open(file_name, 'a' ) as f:
		sys.stdout = f
		for i in range(len(data)):
			if i == 0:
				print(str(data[i]))
			else:
				print(' ,' + str(data[i]))
		f.close()
	return

if __name__=="__main__":
	with open('../dataset/sstubs.txt') as f:
		data = json.load(f)
		f.close()
	cur_dir = os.path.dirname(os.path.realpath(__file__))
	print(data[0])
	count = 0
	for i in range(len(data)):
		try:
			temp = []
			temp.append(str(data[i]['projectName'].rstrip("\n")))
			temp.append(str(data[i]['bugFilePath']).rstrip("\n"))
			temp.append(str(data[i]['bugLineNum']).rstrip("\n"))
			temp.append(str(data[i]['fixCommitSHA1']).rstrip("\n"))
			temp.append(str(data[i]['fixCommitParentSHA1']).rstrip("\n"))
			write_in_file(cur_dir+'/repos/'+str(data[i]['projectName'])+'.csv', temp)

		except:
			count += 1
#			print("-----------File Error!------------------")

