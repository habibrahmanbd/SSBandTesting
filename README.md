# How is Testing Related to Single Statement Bugs?

This repository contains the project artifacts for the graduate project of CMPUT501 - Software Quality course instructed by Dr. Sarah Nadi.

## Students
 - Saqib Ameen (saqib1)
 - [Habibur Rahman](https://habibrahman.me) (habibur)


## Directory structure

```
.
├── dataset
│   ├── bugs.txt
│   ├── by-project                                                # Contains Projectwise Dataset
│   │   ├── Activiti.Activiti
│   │   ├── ...
│   ├── occurrence_of_stub.png                                    # Graph of STUB Occurrence
│   ├── ssb_ratio_chart.xls
│   ├── ssb_ratio.csv
│   ├── sstubs.json                                               # MSR 2021 Challenge Dataset
│   └── sstubs.txt
├── projects.txt
├── proposal
│   ├── CMPUT501-Project Proposal.pdf                             # Project Proposal
│   ├── proposal2021.bib
│   ├── proposal2021.pdf
│   └── proposal2021.tex
├── README.md
├── reports                                                       # Projectwise Coverage Report
│   ├── async-http-client
│   │   ├── async-http-client-project-2.0.25                      # Project Versionwise Jacoco Report by Release Tag
│   │   ├── ...
├── scripts
│   ├── build_report.txt
│   ├── calculate_ssb_ratio.py
│   ├── coco.png
│   ├── evaluate_all.sh                                           # Run Corelation Generation Script
│   ├── evaluate.sh                                               # Script for Single Project Report Generate
│   ├── json_preprocess.py                                        # Python Script for Split Dataset by Project
│   ├── log.txt                                                   # Log of evaluate_all.sh script
│   ├── repo_list.txt                                             # Contains the Git Repo Link in ssh format for Specfic Project for Evaluation
│   ├── repo_processor.py                                         # Python Script to Clone Repo, Parse Jacoco XML and Coorelation Calucation
│   ├── repos
│   │   ├── Activiti.Activiti.csv                                 # Username.RepoName.csv contains specfific info for a SSB, each line in this file is info for a single SSB
│   │   ├── Activiti.Activiti.res                                 # Store Result in a .res file that contains Project Name, Issue in Covered Part, Issue in Not Covered Part, Average Code Coverage Percentage
│   │   ├── ...
│   │   ├── Activiti                                              # Contains the cloned Project from Git
|   |   ├── ...
```

## Generating the Results

This section describes how you can generate the final results *from the already generated reports* for all the projects. All the scripts are tested with Python 3.9.1(latest). All the steps should be performed inside `scripts/` directory.


### Step 0: Resolving Dependencies

Make sure you have Python3 installed. We use some Python libraries during the automation/processing of our data. The are all listed in the `scripts/requiremens.txt` file. Run the following command the install the dependencies:

 ````shell
 pip3 install -r requirements.txt
 ````

### Step 1: Preprocessing Data

It splits the dataset from a single file to project wise `.csv` files, that we use later on. It generates the `.csv` files in `scripts/dataset_split/` directory. You can omit this step if you want, since we have already have added the results folder.

```shell
python3 json_preprocess.py
```

### Step 2: Calculating the Results

Final step is calculate the percentage of bugs in the covered and uncovered parts as well as the percentage coverage. To do this, run the following command:

```shell
./evaluate_all.sh repo_list.txt
```

`repo_list.txt` contains the links for the repos against which the reports exist. This script clones them and process them further to get the results. The results are then saved in `result.csv` file.

Our `.csv` file is saved as `scripts/results_manually_processed.csv`. We have manually processed it further after getting the results to remove any outliers.

### Step 3: Finding Correlation

We find the correlation in Excel. For this, we use the following formula:

```
=CORREL(<RANGE_OF_PERCENTAGE_COVERAGE>,<RANGE_OF_PERCENTAGE_BUGS_IN_NOT_COVERED>)
```

For `scripts/results_manually_processed.csv`, it looks like `=CORREL(E2:E13,G2:G13)`.

## Troubleshooting

## License
