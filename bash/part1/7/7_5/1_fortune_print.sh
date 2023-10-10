#!/bin/bash

number=0

while [ $number -lt 10 ]
do
	if [ $((number%2)) -eq 0 ]
	then
		echo ""$number": "$(fortune ru -s -n 160 | head -n 1)""
	fi

	number=$((number + 1))
done

