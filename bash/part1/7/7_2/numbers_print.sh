#!/bin/bash

number=0

while [ "$number" -le 9 ]
do
	echo "$number"
	number=$(expr "$number" + 1)
done
