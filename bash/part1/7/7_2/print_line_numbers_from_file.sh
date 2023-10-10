#!/bin/bash

number=1

read -p "Enter a file full path: " file_for_read

while read line
do
	echo "Line number "$number": "$line""
	number=$(expr "$number" + 1)
done < "$file_for_read"
