#!/usr/bin/env zsh

days=`ls -d day* | wc -l`

(( new_day = $days + 1))

day="day${(l:2::0:)new_day}"

mkdir $day
cp ./template.py "${day}/${day}.py"
touch "${day}/example.txt"
touch "${day}/input.txt"

cd $day

pwd
ls -Ahl
