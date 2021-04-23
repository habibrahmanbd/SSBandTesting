# How is Testing Related to Single Statement Bugs?

This repository contains the project artifacts for the graduate project of CMPUT501 - Software Quality course instructed by Prof. Sarah Nadi.

## Students
 - Habibur Rahman (habibur)
 - Saqib Ameen (saqib1)



## Directory structure

```
.
├── dataset
│   ├── bugs.txt
│   ├── by-project                                # Contains Projectwise Dataset
│   │   ├── Activiti.Activiti
│   │   ├── ...
│   ├── occurrence_of_stub.png                    # Graph of SSBs distribution
│   ├── ssb_ratio_chart.xls
│   ├── ssb_ratio.csv
│   ├── sstubs.json                               # MSR 2021 Challenge Dataset
│   └── sstubs.txt
├── projects.txt
├── README.md
├── reports                                       # Projectwise Coverage Report
│   ├── async-http-client
│   │   ├── async-http-client-project-2.0.25      # Project Versionwise Jacoco Report by Release Tag
│   │   ├── ...
│   ...
├── reports-generation                            # Contains Instructions on Generating Reports for Each Project
│   ├── alibaba.druid
│   │   ├── readme.md                             # Project specific instructions for generating report
│   │   ├── 1.1.10                                # Contains files which needs to be replaced in specific version
│   │   ├── ...
│   ...
├── scripts
│   ├── bugs_distribution                         # Contains bugs distribution graphs for projects
│   ├── dataset_split                             # Contains splitted dataset csv files
│   ├── evaluate_all.sh                           # Main script to do all the processing/calculations
│   ├── evaluate.sh                               # Script for Single Project Report Generate (used by evaluate_all.sh)
│   ├── json_preprocess.py                        # Python Script for Split Dataset by Project
│   ├── repo_list.txt                             # Contains the Git Repo Link in ssh format for cloning them
│   ├── repo_processor.py                         # Python Script to Cloning Repo, Parsing Jacoco XML and doing calculations
│   ├── repos
│   │   ├── Activiti                              # Contains the cloned Project from GitHub
│   │   ├── ...
├── final_report                                  # Contains the final report of project
```

## 📈 Generating the Results

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

⚙️ ## Generating the Coverage Reports for the Projects

The `reports_generation` folder contains all the data required to generate the coverage reports. Follow the following steps to navigate through `reports_generation` folder and generate reports.

### Step 0: Prerequisites

You need to have **Java 8**. The projects do not use the latest Java version. So it must be Java 8. It can be installed from [here](https://www.oracle.com/ca-en/java/technologies/javase/javase-jdk8-downloads.html). Run the following command to check the version:

```shell
java -version

# Expected output:
# java version "1.8.0_281"
# Java(TM) SE Runtime Environment (build 1.8.0_281-b09)
# Java HotSpot(TM) 64-Bit Server VM (build 25.281-b09, mixed mode)
```
An alternate option is to use JEnv for multiple Java versions. Here is useful [guide](https://chamikakasun.medium.com/how-to-manage-multiple-java-version-in-macos-e5421345f6d0) on setting it up in MacOS.

You need to have Maven installed. We used **Apache Maven 3.6.3**. You can confirm the installation by using following command:

```shell
mvn -version

# Sample Result:
# Apache Maven 3.6.3 (cecedd343002696d0abb50b32b541b8a6ba2883f)
# Maven home: /opt/homebrew/Cellar/maven/3.6.3_1/libexec
# Java version: 1.8.0_281, vendor: Oracle Corporation, runtime: /Library/Java/JavaVirtualMachines/jdk1.8.0_281.jdk/Contents/Home/jre
# Default locale: en_CA, platform encoding: UTF-8
# OS name: "mac os x", version: "10.16", arch: "x86_64", family: "mac"
```

### Step 1: Generating Reports

The structure of `reports-generation` directory looks like this:

```
├── reports-generation                            # Contains Instructions on Generating Reports for Each Project
│   ├── alibaba.druid
│   │   ├── readme.md                             # Project specific instructions for generating report
│   │   ├── 1.1.10                                # Contains files which needs to be replaced in specific version
│   │   ├── ...
│   ...
```
There is one readme file for each project. It contains the repo link, from which the project can be cloned. It lists all the versions for which reports are included in our repository. Other than that, for each project, for a few versions, we have added the files which needs to be updated/modified in order to generate the reports.

Each folder name, inside the project folder, corresponds to a release tag. Inside each tag folder, we have placed all the files in their appropriate path, which need to be replaced to generate the reports. For most of the projects, only `pom.xml` file needs to be updated. For others it might be different.

To generate the coverage report for a specific version, first clone the repo, using the link in the readme, then checkout to one of the version for which files are provided. For example, let's say we want to generate report for `1.1.10` release version of `alibaba.druid`. Below are the steps to do it:

1. Clone it using `git clone https://github.com/alibaba/druid.git`
2. Checkout to `1.1.10` release, using `git checkout 1.1.10`.
3. Since our `reports-generation/alibaba.druid/1.1.10` path, contains only `pom.xml` file at root, we will replace that in our project.
4. The `reports-generation/alibaba.druid/readme.md` file asks to run, `mvn clean test` at the root directory. So we will run that.

That's it. The report will be generateed in the `/target` folder at root directory.

### Step 2: Generating Reports for Next Versions

The readme file for each project contains the instructions on how to generate the reports for the next versions. For some projects, there are a lot of discrepencies, for others it is not very different for different versions. For example, for `alibaba.druid` project, the isntructions can ev found in `reports-generation/alibaba.druid/readme.md`.

## 🙌 Acknowledgement

Thanks to Prof. Sarah for guiding us throughout the project and teaching the skills necessary to execute the idea. A shoutout to CMPUT501 TAs - Batyr and Henry as well for all the lab sessions and walkthroughs on actually using different technologies.
