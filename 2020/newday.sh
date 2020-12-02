#!/usr/bin/env zsh

days=`ls -d day* | wc -l`

(( new_day = $days + 1))

echo $new_day

day="day${(l:2::0:)new_day}"

mkdir $day
cp ./template.py "${day}/${day}.py"
touch "${day}/test.txt"
touch "${day}/input.txt"

cd $day
ls -ahl
