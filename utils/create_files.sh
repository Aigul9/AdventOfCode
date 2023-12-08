#!/bin/bash

read -p "year: " year
read -p "day in 2-digit format: " day

year_folder="year$year"
day_folder="Day_$day"

cd $year_folder

mkdir $day_folder

cd $day_folder

touch input.txt
touch test.txt
touch main.py
touch task.txt

echo "done"

read
