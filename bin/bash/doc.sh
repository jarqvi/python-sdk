#!/bin/bash

# Directory paths where files should be moved
directories=(
    object-storage
    dbaas
    paas
    mail
    dns
)

# Loop through directories and move specified files
for dir in "${directories[@]}"; do
    # Move README.md file if it exists
    if [ -e ./"$dir"/README.md ]; then
        sudo mv ./"$dir"/README.md ./doc/"$dir"
    fi

    # Move all mark down files except README.md file in the doc directory
    if find ./"$dir"/docs -name "*.md" -print -quit | grep -q .; then
        sudo mv -v ./"$dir"/docs/*.md ./doc/"$dir"/docs
        sudo rm -rf ./"$dir"/docs
    fi
done