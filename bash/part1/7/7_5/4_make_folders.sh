#!/bin/bash

count=0

while [ $count -le 6 ]
do
	mkdir /tmp/directory-`date "+%Y%m%d_%H%M"`
	count=$((count + 1))
	sleep 7m
done

