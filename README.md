# How is Testing Related to Single Statement Bugs?

This repository contains the project artifacts for the graduate project of CMPUT501 - Software Quality course instructed by Prof. Sarah Nadi.

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
│   ├── occurrence_of_stub.png                                    # Graph of SSBs distribution
│   ├── ssb_ratio_chart.xls
│   ├── ssb_ratio.csv
│   ├── sstubs.json                                               # MSR 2021 Challenge Dataset
│   └── sstubs.txt
├── projects.txt
├── README.md
├── reports                                                       # Projectwise Coverage Report
│   ├── async-http-client
│   │   ├── async-http-client-project-2.0.25                      # Project Versionwise Jacoco Report by Release Tag
│   │   ├── ...
│   ...
├── reports-generation                                            # Contains Instructions on Generating Reports for Each Project
│   ├── alibaba.druid
│   │   ├── readme.md                                             # Project specific instructions for generating report
│   │   ├── 1.1.10                                                # Contains files which needs to be replaced in specific version
│   │   ├── ...
│   ...
├── scripts
│   ├── bugs_distribution                                         # Contains bugs distribution graphs for projects
│   ├── dataset_split                                             # Contains splitted dataset csv files
│   ├── evaluate_all.sh                                           # Main script to do all the processing/calculations
│   ├── evaluate.sh                                               # Script for Single Project Report Generate (used by evaluate_all.sh)
│   ├── json_preprocess.py                                        # Python Script for Split Dataset by Project
│   ├── repo_list.txt                                             # Contains the Git Repo Link in ssh format for cloning them
│   ├── repo_processor.py                                         # Python Script to Cloning Repo, Parsing Jacoco XML and doing calculations
│   ├── repos
│   │   ├── Activiti                                              # Contains the cloned Project from GitHub
│   │   ├── ...
├── final_report                                                  # Contains the final report of project
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

`repo_list.txt` contains the links for the repos against which the reports exist. This script clones them and process them further to get the results. The results are then saved in `results.csv` file. We have included it in out repo.

We further process it to remove outliers, we have saved our processed `.csv` file in `scripts/results_manually_processed.csv`.

Please note that it will clone the repos in the `scripts/repos/` folder from GitHub.

### Step 3: Finding Correlation

We find the correlation in Excel. For this, we use the following formula:

```
=CORREL(<RANGE_OF_PERCENTAGE_COVERAGE>,<RANGE_OF_PERCENTAGE_BUGS_IN_NOT_COVERED>)
```

For `scripts/results_manually_processed.csv`, it looks like `=CORREL(E2:E13,G2:G13)`.

## Troubleshooting

## License
