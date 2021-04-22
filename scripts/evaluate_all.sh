#!/bin/bash

#This script will run for all repositories in a file

#rm -rf /repos/*.csv

#python3 json_preprocess.py

#CSV File for result
rm -rf results.csv
touch results.csv
echo 'ProjectName, Covered, Not Covered, Total (Covered + Not Covered), % of Coverage, %Covered, % Not Covered'>>results.csv

repo_list=$1
while IFS= read -r line; do
    echo "$line"
    ./evaluate.sh $line
done < $repo_list
