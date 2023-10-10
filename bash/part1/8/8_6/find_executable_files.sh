#!/bin/bash
#find /usr -type f

for file in $(find /usr -type f)
do
	if [ -x "$file" ]
	then
		echo ""$file" is executable!"
	fi
done

