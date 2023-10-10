#!/bin/bash

while true
do
	sleep $(awk 'BEGIN {srand(); print int(rand()*10)}')
	fortune ru -s -n 160 | head -n 1
done

