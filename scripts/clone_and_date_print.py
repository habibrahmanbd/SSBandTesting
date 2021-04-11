#!/usr/bin/python

import os
import datetime
import sys
from dateutil.relativedelta import relativedelta
import subprocess
from pathlib import Path
import csv
import xml.dom.minidom
import xml.etree.ElementTree as ET
import logging
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')


def clone_repo(target_dir, repo_link, repo_name): #target_dir = cur_dir + 'repos/'
	logging.info('Cloning ... '+str(repo_name))
	if os.path.isdir(str(target_dir)+'/'+str(repo_name)) == False:
		os.system('rm -rf '+str(target_dir)+'/'+str(repo_name)+' && ' + 'cd '+str(target_dir)+' && git clone '+repo_link)
	return

def clean_time_output(meta_time):
	logging.info('Cleaning time Output .. Metatime: '+str(meta_time))
	meta_time = str(meta_time)
	meta_time = meta_time[1:]
	meta_time = meta_time.replace('\'', '')
	meta_time = meta_time.replace('_', '/')
	_year = meta_time.split("/")[0]
	_month = meta_time.split("/")[1]
	_day = meta_time.split("/")[2]
	_date = datetime.date(int(_year),int(_month), int(_day))
	print(_date)
	return _date

def last_commit_date(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	logging.info('Last Commit Date for ..' + str(target_dir))
	os.chdir(target_dir)
	cmd = 'git log -1 --format="%at" | xargs -I{} date -d @{} +%Y/%m/%d_%H:%M:%S'
	returned_output = subprocess.check_output(cmd, shell=True)
	_last_commit_date = clean_time_output(returned_output)
	return _last_commit_date

def release_tag_list(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	logging.info('Release Taglist for ..'+str(target_dir))
	os.chdir(target_dir)
	cmd = 'git tag -l'
	returned_output = subprocess.check_output(cmd, shell=True)
	returned_output = str(returned_output)[1:]
	returned_output = returned_output.replace('\'', '')
	returned_output = returned_output.replace("\\n", ' ')
	returned_output = returned_output.split()
#	print(returned_output)
	return returned_output

def clean_number(num):
	logging.info('Cleaning Number ..'+str(num))
	ret = ''
	for i in num:
		if i >= '0' and i<='9':
			ret+=i
	return int(ret)

def git_time_in_ms(target_dir, tag_name_or_sha):
	logging.info('Git time for '+str(target_dir) + ' of tag/sha:' +str(tag_name_or_sha))
	try:
		os.chdir(target_dir)
		cmd = 'git log -1 --format="%at" '+str(tag_name_or_sha)
		returned_output = subprocess.check_output(cmd, shell=True)
		returned_output = clean_number(str(returned_output))
		#print(str(tag_name_or_sha) + ' : ' + str(returned_output))
		return int(returned_output)
	except Exception as e:
		logging.exception("Exception occurred")
		return 0

#def checkout_last_commit_date(repo_name, date):
#	os.chdir('repos/'+str(repo_name))

def print_months_by_commit(target_dir, repo_name, last_commit_time): #target_dir = cur_dir + 'repos/'
	logging.info('Printing months for '+str(target_dir) + ' of ' +str(repo_name))
	with open(str(target_dir)+'/'+str(repo_name)+'_months.txt', 'w') as f:
		today = last_commit_time
		sys.stdout = f
		for i in range(0, 5):
			print((today - relativedelta(months=i)).strftime("%b %d %Y"))
	return

def print_taglist_by_dates(target_dir, repo_name, tag_dict): #target_dir = cur_dir + 'repo    s/'
	logging.info('Print Taglist for '+str(target_dir) + ' of ' +str(tag_name_or_sha)+' by date')
	with open(str(target_dir)+str(repo_name)+'_taglist.csv', 'w') as f:
		sys.stdout = f
		for key, value in tag_dict.items():
			print(str(key)+','+str(value))
	return

def run_build(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	logging.info('Building '+str(target_dir))
	try:
		cmd = 'mvn -f '+str(target_dir)+'/pom.xml clean compile'
		subprocess.call(cmd, shell=True)
	except Exception as e:
		logging.exception('-------------!!BUILD FAILED!!-----------------')
	return


def run_test(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	logging.info('Running Test for '+str(target_dir))
	try:
		cmd = 'mvn -f '+str(target_dir)+'/pom.xml clean test'
		subprocess.call(cmd, shell=True)
	except Exception as e:
		logging.exception('------------!TEST FAILED!----------------------')
	return
def jacoco_xml_generation():
	return

def create_repos(target_dir): #target_dir = cur_dir + 'repos/' + $repo_name
	logging.info('Make Directory for '+str(target_dir))
	try:
		Path(target_dir).mkdir(parents=True, exist_ok=True)
	except Exception as e:
		logging.exception('!Failed to create \'repos\'')
	return

def checkout_by_tags(target_dir, desired_tag):
	logging.info('[INFO]-------------------< Checking out at '+str(desired_tag)+'>---------------------')
	try:
		os.chdir(target_dir)
		cmd = 'git checkout tags/'+str(desired_tag)
		subprocess.call(cmd, shell=True)
	except Exception as e:
		logging.exception('-------------Checkout Failed for '+str(desired_tag)+' -------------')
	return

def search_in_dictory(data_dictionary, to_find):
	logging.info('Searching for '+str(to_find))
	count = 0
	for row in data_dictionary:
		if row[0] == to_find:
			return row[0],row[1], count
		elif row[0] < to_find:
			count += 1
			continue
		else:
			return row[0], row[1], count
	return -1, -1, count

def load_csv(file_path):
	logging.info('Loading CSV '+str(file_path))
	with open(file_path, newline='') as csvfile:
		data = csv.reader(csvfile)
		returned_list = list(data)
	return returned_list

def tag_and_datetime(taglist, cur_dir, repo_name):
	logging.info('Taglist with date and time for '+str(repo_name))
	tag_date = []
	for i in range(len(taglist)):
		_datetime = git_time_in_ms(cur_dir + '/repos/' + str(repo_name), taglist[i])
		tag_date.append([int(_datetime), taglist[i]])
	return tag_date

def is_covered(bugLine_number, bug_filename, root):
	logging.info('Is Covered? for '+str(bug_filename))
	#print(bug_filename.split('/')[-1])
	bug_filename = bug_filename.split('/')[-1]
	for elem in root.iter('package'):
		for elem_next in elem.iter('sourcefile'):
			#print(elem_next.attrib)
			if elem_next.attrib['name'] == str(bug_filename): #Expected Java File
	#			print('----------'+elem_next.attrib['name']+'--------')
				for line in elem_next.iter('line'):
					#print('-----------'+line.attrib['nr']+'------------')
					if int(line.attrib['nr']) == int(bugLine_number): #Expected Bug Line Number
						if int(line.attrib['ci']) > 0:
							return 1
						else:
							return 0


def load_jacoco(target_dir, _version):
	logging.info('Loading JACOCO for '+str(target_dir) + ' of '+str(_version))
	jacoco_report = None
	#jacoco_report = xml.dom.minidom.parse(target_dir+'/'+_version+'/jacoco.xml')
	try:
		jacoco_report = ET.parse(str(target_dir)+'/'+str(_version)+'/jacoco.xml')
		jacoco_report = jacoco_report.getroot()
		#print('[VERSION] ' +str(_version))

	except Exception as e:
		'''
		try:
			os.system('rm -rf '+target_dir + '/log.txt')
		except Exception as e:
			print("------------------------------------------------------------Removing no existing file --------------------------------")
		
		with open(target_dir + '/log.txt', "a") as f:
			print(str(e), file=f)
			f.close()
		'''
		logging.exception('Exception in Loading Jacoco: '+str(e))
		logging.exception(target_dir+'/'+_version+'/jacoco.xml')
		jacoco_report = None
	return jacoco_report

def print_logfile(target_dir, data):
	with open(target_dir + '/log.txt', "a") as f:
		print(str(data), file=f)
		f.close()


def print_report_final(target_dir, data, fileName):
	logging.info('Printing Final Covered Statistics in '+str(fileName))
	print(fileName+' => '+data)
	with open(target_dir+'/'+fileName, "w+") as f:
		print(fileName+' => '+data, file=f)
		f.close()

if __name__=="__main__":
	args = sys.argv[1:]
	repo_link = args[0]
	repo_name = args[1]
	logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

	cur_dir = os.path.dirname(os.path.realpath(__file__))
	create_repos(cur_dir+'/repos')

	clone_repo(str(cur_dir)+'/repos/', repo_link, repo_name)

#	_last_commit_date = last_commit_date(cur_dir+'/repos/' + str(repo_name))
#	print_months_by_commit(cur_dir+'/repos/', repo_name, _last_commit_date)

	taglist = release_tag_list(cur_dir + '/repos/' + str(repo_name))
	tag_date = tag_and_datetime(taglist, cur_dir, repo_name)
#	print(tag_date)
	tag_date = sorted(tag_date, key=lambda l:l[0])
	projectName = (str(repo_link).replace('git@github.com:', '')).split('/')[0]+'.'+repo_name+'.csv'
	project_dataset = load_csv(cur_dir+'/repos/'+projectName)

	count_covered = 0
	count_uncovered = 0
	total_coverage = 0
	cov_str = ""
	cov_dic = {}
	for row in project_dataset:
	#	try:
		time_commit = git_time_in_ms(cur_dir+'/repos/'+repo_name, row[4])
		next_release_time, next_release_tag, index = search_in_dictory(tag_date, int(time_commit))
#		print(next_release_time)
		logging.info(repo_name+" => "+next_release_tag)
		if next_release_time > 0:
			bug_file_name = row[1]
			#print('Version: '+str(next_release_tag))
			jacoco_report = load_jacoco(cur_dir+'/../reports/'+repo_name, next_release_tag)
			#print(jacoco_report)
			it = 0
			while(jacoco_report == None and index+it+1 < len(tag_date) and it+1 < 7 ):
				it +=1
				next_release_tag = tag_date[index+it][1]
				jacoco_report = load_jacoco(cur_dir+'/../reports/'+repo_name, next_release_tag)
			if jacoco_report == None:
				print_logfile(cur_dir+'/../reports/'+repo_name, next_release_tag)
			if jacoco_report != None:
				bugLine_number = row[2]
				_is_covered = is_covered(bugLine_number, bug_file_name, jacoco_report)
				if _is_covered == 1:
					count_covered += 1
				else:
					count_uncovered += 1
				#	except:
				#		count_covered += 0
				#print('-----------------Exception----------------')
				htmlFile = open(cur_dir+'/../reports/'+repo_name+'/'+next_release_tag+'/index.html', "r")
				soup = BeautifulSoup(htmlFile,'html.parser')
				print("----------INDEX.HTML PATH: "+cur_dir+'/../reports/'+repo_name+'/'+next_release_tag+'/index.html')
				coverage = int((str(soup.select('#coveragetable tfoot tr td:nth-child(3)')[0]).replace('<td class="ctr2">', '')).replace('%</td>', ''))
				#cov_str += '\nVersion: ' + str(next_release_tag)+' Coverage: '+str(coverage)+'\n'
				#total_coverage += coverage
				htmlFile.close()
				cov_dic[str(next_release_tag)] = coverage
	for key, value in cov_dic.items():
		total_coverage += value
	cov_avg = total_coverage / len(cov_dic.items())
	cov_str += ', Average Coverage: '+str(cov_avg)+'\n'
	print_report_final(cur_dir+'/repos/', 'Covered: '+str(count_covered)+', Not Covered: '+str(count_uncovered)+ ', Total: '+str(count_covered + count_uncovered) + ''+str(cov_str), projectName.replace('.csv', '.res'))
	print("---------------Result Printed to .res file with Project Name--------------------")
	#checkout_by_tags(cur_dir + '/repos/' + str(repo_name), taglist[i])
	#run_build(cur_dir + '/repos/' + str(repo_name))
	#run_test(cur_dir + '/repos/' + str(repo_name))

#	print_taglist_by_dates(cur_dir+'/repos/', repo_name, tag_date)
