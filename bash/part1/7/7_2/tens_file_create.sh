#!/bin/bash

file_number=0

while [ $file_number -le 9 ]
do
	touch $file_number.file
	file_number=$(expr $file_number + 1)
done
