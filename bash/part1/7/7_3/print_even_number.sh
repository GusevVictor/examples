#!/bin/bash

number=1

while [ "$number" -le 20 ]
do
	number=$(expr "$number" + 1)

	if [ $((number%2)) -eq 0 ]
	then
		echo "$number"
	fi
done
