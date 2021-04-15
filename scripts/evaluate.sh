#!/bin/bash

repo_link=$1


echo "----------Working with------$repo_name-----------"

repo_name_git=$(echo $repo_link| cut -d'/' -f 2)
repo_name=$(echo $repo_name_git| cut -d'.' -f 1)

python3 repo_processor.py $repo_link $repo_name
#./run_gradle.sh "repos/$repo_name"
echo "----------End working with--$repo_name-----------"

