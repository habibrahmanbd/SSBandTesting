import json
from pprint import pprint

ROOT_DIRECTORY = './../'
DATASET_ABS_PATH = 'dataset/sstubs.txt'
DATASET_BY_PROJECT_ABS_PATH = 'dataset/by-project/'
PROJECT_NAME = 'projectName'
TXT_EXTENSION = '.txt'

raw_dataset = open(ROOT_DIRECTORY + DATASET_ABS_PATH)
dataset = json.load(raw_dataset)
raw_dataset.close()
project_names = list(set(entry[PROJECT_NAME] for entry in dataset))

group_by_project = {}
for project in project_names:
    data_for_project = list(filter(lambda bug: bug[PROJECT_NAME] == project, dataset))
    group_by_project[project] = data_for_project
    project_file = open(ROOT_DIRECTORY + DATASET_BY_PROJECT_ABS_PATH + project, 'w', encoding="ascii")
    # project_file.write()
    json.dump(data_for_project, project_file, indent = 2)
    # pprint(json.dumps(data_for_project), stream=project_file)
    project_file.close()
