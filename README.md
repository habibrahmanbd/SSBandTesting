# CMPUT501 - Software Quality - Graduate Project Artifacts
This repository contains the graduate project artifacts for CMPUT501 - Software Quality course instructed by Dr. Sarah Nadi.

## Graduate Students:
 - Saqib Ameen (saqib1)
 - [Habibur Rahman](https://habibrahman.me) 

## Dependencies
 - Python 3
 - [github3](https://github.com/sigmavirus24/github3.py)
 ````shell
 # Quick Installtion steps
 pip3 install -r requirements.txt
 ````
 These scripts have been tested with Python 3.9.1(latest).
 
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
## Instructions
### Step 1: Projectwise Dataset Split
    ```
    python3 json_preprocess.py
    ```
### Step 2: Print Coverage, and Bug Result in .res file and print Projectwise Bug Distribution Graph in <repo_name>.png file
    ```
        ./evaluate_all.sh
    ```
### Step 3: Corelation Report Generation

## Troubleshooting

## License
