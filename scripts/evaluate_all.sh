#!/bin/bash

#This script will run for all repositories in a file

repo_list=$1
while IFS= read -r line; do
    echo "$line"
    ./evaluate.sh $line
done < $repo_list