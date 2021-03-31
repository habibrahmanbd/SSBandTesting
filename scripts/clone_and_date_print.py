#!/usr/bin/python

import os
import datetime
import sys
from dateutil.relativedelta import relativedelta
import subprocess

def clone_repo(repo_link, repo_name):
	os.system('rm -rf repos/'+str(repo_name)+' && ' + 'cd repos && git clone '+repo_link)
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

def last_commit_date(repo_name):
	os.chdir('repos/'+str(repo_name))
	cmd = 'git log -1 --format="%at" | xargs -I{} date -d @{} +%Y/%m/%d_%H:%M:%S'
	returned_output = subprocess.check_output(cmd, shell=True)
	_last_commit_date = clean_time_output(returned_output)
	return _last_commit_date

#def checkout_last_commit_date(repo_name, date):
#	os.chdir('repos/'+str(repo_name))

def print_months_by_commit(repo_name, last_commit_time):
	with open('../'+str(repo_name)+'_months.txt', 'w') as f:
		today = last_commit_time
		sys.stdout = f
		for i in range(0, 5):
			print((today - relativedelta(months=i)).strftime("%b %d %Y"))
	return

def run_build(repo_name):
	try:
		#print(os.path.dirname(os.path.realpath(__file__)))
		#f = open('build_report.txt', 'w')
		cmd = 'mvn -f repos/'+str(repo_name)+'/pom.xml clean compile'
		subprocess.call(cmd, shell=True)
		#process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
		#output, error = process.communicate()
	except:
		print('-------------!!BUILD FAILED!!-----------------')


def run_test(repo_name):
	try:
		cmd = 'mvn -f repos/'+str(repo_name)+'/pom.xml clean test'
		subprocess.call(cmd, shell=True)
	except:
		print('------------!TEST FAILED!----------------------')

def jacoco_xml_generation():
	return

if __name__=="__main__":
	args = sys.argv[1:]
	repo_link = args[0]
	repo_name = args[1]

	clone_repo(repo_link, repo_name)
#	_last_commit_date = last_commit_date(repo_name)
#	print_months_by_commit(repo_name, _last_commit_date)

	run_build(repo_name)
	run_test(repo_name)
