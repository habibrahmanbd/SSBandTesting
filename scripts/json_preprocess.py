import json
from pandas.io.json import json_normalize
import os
import sys

def write_in_file(file_name, data):
	with open(file_name, 'a' ) as f:
		sys.stdout = f
		print(data)
		f.close()
	return

def clean_string(in_str):
	#print('Prev: ' + in_str)
	in_str = ''.join([c for c in in_str if c not in [' ', '\t', '\n']])
	#print('Post: ' + in_str)
	return in_str

if __name__=="__main__":
	cur_dir = os.path.dirname(os.path.realpath(__file__))
	f = open('../dataset/sstubs.json', 'r', encoding='utf-8')
	data = json.load(f)
	#cur_dir = os.path.dirname(os.path.realpath(__file__))
	#print(data[0])
	count = 0
	print('----------------CSV-----------------')
	#print('Len: '+str(len(data)))
	for i in data['sstubs']:
		new_data = i.copy()
		temp = ''
		#print('-------------CSV--'+str(i)+'-------')
		temp += clean_string((new_data["projectName"])) + ', '
		temp += clean_string((new_data["bugFilePath"]))+ ', '
		temp += clean_string(str(new_data["bugLineNum"]))+ ', '
		temp += clean_string((new_data["fixCommitSHA1"]))+ ', '
		temp += clean_string((new_data["fixCommitParentSHA1"]))
		write_in_file(cur_dir+'/repos/'+str(new_data['projectName'])+'.csv', temp)
	f.close()

