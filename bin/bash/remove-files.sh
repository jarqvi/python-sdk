#!/bin/bash

# Function to delete a file if it exists
delete_file_if_exists() {
    if [ -e "$1" ]; then
        sudo rm -rf "$1"
        echo "Deleted $1"
    else
        echo "$1 does not exist, skipping deletion"
    fi
}

# Directory paths where files should be deleted
directories=(
    ./object_storage
    ./dbaas
    ./paas
    ./mail
    ./dns
)

# Files to delete in each directory
files_to_delete=(
    .github
    .gitignore
    .gitlab-ci.yml
    git_push.sh
    .travis.yml
    pyproject.toml
    requirements.txt
    setup.cfg
    test-requirements.txt
    tox.ini
    setup.py
)

# Loop through directories and delete specified files
for dir in "${directories[@]}"; do
    for file in "${files_to_delete[@]}"; do
        delete_file_if_exists "$dir/$file"
    done
done