#!/bin/bash

read -p "Please insert three numbers for compare: " number_1 number_2 number_3
if [ "$number_1" -gt "$number_2" ]
then
	number_2=$number_1
fi

if [ "$number_2" -gt "$number_3" ]
then
	number_3=$number_2
fi
echo "$number_3"
