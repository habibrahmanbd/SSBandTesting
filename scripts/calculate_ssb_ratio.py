import json
import csv

ROOT_DIRECTORY = './../'
SSB_PATH = 'dataset/sstubs.txt'
ALL_BUGS_PATH = 'dataset/bugs.txt'
DATASET_BY_PROJECT_ABS_PATH = 'dataset/by-project/'
DATASET_PATH = 'dataset/'
PROJECT_NAME = 'projectName'
SSB = 'Single Statement Bugs'
ALL_BUGS = 'All Bugs'
SSB_PRCNT = 'SSB Percentage'
SSB_RATIO_NAME = 'ssb_ratio'
CSV_EXT = '.csv'
SSB_RATIO_CSV_PATH = ROOT_DIRECTORY + DATASET_PATH + SSB_RATIO_NAME + CSV_EXT
PROJECT_NAME_STR = 'Project Name'


ssb_raw_dataset = open(ROOT_DIRECTORY + SSB_PATH)
ssb_dataset = json.load(ssb_raw_dataset)
ssb_raw_dataset.close()
project_names = list(set(entry[PROJECT_NAME] for entry in ssb_dataset))

all_bugs_raw_dataset = open(ROOT_DIRECTORY + ALL_BUGS_PATH)
all_bugs_dataset = json.load(all_bugs_raw_dataset)
all_bugs_raw_dataset.close()


ssb_ratio_csv = open(SSB_RATIO_CSV_PATH, 'w')
filed_names = [PROJECT_NAME_STR, SSB, ALL_BUGS, SSB_PRCNT]
csv_writer = csv.DictWriter(ssb_ratio_csv, fieldnames = filed_names)
csv_writer.writeheader()

for project in project_names:
    ssb_for_project = list(filter(lambda bug: bug[PROJECT_NAME] == project, ssb_dataset))
    all_bugs_for_project = list(filter(lambda bug: bug[PROJECT_NAME] == project, all_bugs_dataset))
    csv_writer.writerow({PROJECT_NAME_STR: project, SSB: len(ssb_for_project), ALL_BUGS: len(all_bugs_for_project), SSB_PRCNT: len(ssb_for_project)/len(all_bugs_for_project)})

ssb_ratio_csv.close()

print("CSV Generated!")
print("Path: ", SSB_RATIO_CSV_PATH)
