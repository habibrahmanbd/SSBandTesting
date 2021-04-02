#!/usr/bin/python

import os
import datetime
import sys
from dateutil.relativedelta import relativedelta
import subprocess
from pathlib import Path


def clone_repo(target_dir, repo_link, repo_name): #target_dir = cur_dir + 'repos/'
	os.system('rm -rf '+str(target_dir)+'/'+str(repo_name)+' && ' + 'cd '+str(target_dir)+' && git clone '+repo_link)
	return

def clean_time_output(meta_time):
	meta_time = str(meta_time)
	meta_time = meta_time.replace('b', '')
	meta_time = meta_time.replace('\'', '')
	meta_time = meta_time.replace('_', '/')
	_year = meta_time.split("/")[0]
	_month = meta_time.split("/")[1]
	_day = meta_time.split("/")[2]
	_date = datetime.date(int(_year),int(_month), int(_day))
	print(_date)
	return _date

def last_commit_date(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	os.chdir(target_dir)
	cmd = 'git log -1 --format="%at" | xargs -I{} date -d @{} +%Y/%m/%d_%H:%M:%S'
	returned_output = subprocess.check_output(cmd, shell=True)
	_last_commit_date = clean_time_output(returned_output)
	return _last_commit_date

def release_tag_list(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	os.chdir(target_dir)
	cmd = 'git tag -l'
	returned_output = subprocess.check_output(cmd, shell=True)
	returned_output = str(returned_output).replace('b', '')
	returned_output = returned_output.replace('\'', '')
	returned_output = returned_output.replace("\\n", ' ')
	returned_output = returned_output.split()
	print(returned_output)
	return returned_output

def clean_number(num):
	ret = ''
	for i in num:
		if i >= '0' and i<='9':
			ret+=i
	return int(ret)

def git_time_in_ms(target_dir, tag_name_or_sha):
	os.chdir(target_dir)
	cmd = 'git log -1 --format="%at" '+str(tag_name_or_sha)
	returned_output = subprocess.check_output(cmd, shell=True)
	returned_output = clean_number(str(returned_output))
	print(str(tag_name_or_sha) + ' : ' + str(returned_output))
	return int(returned_output)

#def checkout_last_commit_date(repo_name, date):
#	os.chdir('repos/'+str(repo_name))

def print_months_by_commit(target_dir, repo_name, last_commit_time): #target_dir = cur_dir + 'repos/'
	with open(str(target_dir)+'/'+str(repo_name)+'_months.txt', 'w') as f:
		today = last_commit_time
		sys.stdout = f
		for i in range(0, 5):
			print((today - relativedelta(months=i)).strftime("%b %d %Y"))
	return

def print_taglist_by_dates(target_dir, repo_name, tag_dict): #target_dir = cur_dir + 'repo    s/'
	with open(str(target_dir)+str(repo_name)+'_taglist.csv', 'w') as f:
		sys.stdout = f
		for key, value in tag_dict.items():
			print(str(key)+','+str(value))
	return

def run_build(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	try:
		cmd = 'mvn -f '+str(target_dir)+'/pom.xml clean compile'
		subprocess.call(cmd, shell=True)
	except:
		print('-------------!!BUILD FAILED!!-----------------')
	return


def run_test(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	try:
		cmd = 'mvn -f '+str(target_dir)+'/pom.xml clean test'
		subprocess.call(cmd, shell=True)
	except:
		print('------------!TEST FAILED!----------------------')
	return
def jacoco_xml_generation():
	return

def create_repos(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	try:
		Path(target_dir).mkdir(parents=True, exist_ok=True)
	except:
		print('!Failed to create \'repos\'')
	return

def checkout_by_tags(target_dir, desired_tag):
	print('[INFO]-------------------< Checking out at '+str(desired_tag)+'>---------------------')
	try:
		os.chdir(target_dir)
		cmd = 'git checkout tags/'+str(desired_tag)
		subprocess.call(cmd, shell=True)
	except:
		print('-------------Checkout Failed for '+str(desired_tag)+' -------------')
	return

def binary_search_in_dictory(data_dictionary, to_find):
	low = 0
	high = len(data_dictionary) - 1
	mid = 0

	while low < high:
		mid = (high + low ) //2

		if data_dictionary.key()[mid] >= to_find:
			high = mid
		else:
			low = mid

	if low == high:
		return data_dictionary.value()[mid]
	else:
		return null


if __name__=="__main__":
	args = sys.argv[1:]
	repo_link = args[0]
	repo_name = args[1]

	cur_dir = os.path.dirname(os.path.realpath(__file__))
	create_repos(cur_dir+'/repos')

	clone_repo(str(cur_dir)+'/repos/', repo_link, repo_name)

#	_last_commit_date = last_commit_date(cur_dir+'/repos/' + str(repo_name))

#	print_months_by_commit(cur_dir+'/repos/', repo_name, _last_commit_date)

	taglist = release_tag_list(cur_dir + '/repos/' + str(repo_name))
	tag_date = {}
	for i in range(len(taglist)):
		_datetime = git_time_in_ms(cur_dir + '/repos/' + str(repo_name), taglist[i])
		tag_date[int(_datetime)] = taglist[i]
		#checkout_by_tags(cur_dir + '/repos/' + str(repo_name), taglist[i])
		#run_build(cur_dir + '/repos/' + str(repo_name))
		#run_test(cur_dir + '/repos/' + str(repo_name))

	print_taglist_by_dates(cur_dir+'/repos/', repo_name, tag_date)
