#!/bin/bash

number=0
line_number=1

while [ "$number" -le 9 ]
do
	fortune ru -s -n 160 |head -n1 >> fortune_out.txt
	number=$(expr "$number" + 1)
done

while read line
do
	echo ""$line_number": "$line""
	line_number=$(expr "$line_number" + 1)
done < fortune_out.txt
rm fortune_out.txt
