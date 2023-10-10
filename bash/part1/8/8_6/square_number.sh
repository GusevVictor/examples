#!/bin/bash

for number in {10..20}
do
	echo "$number ^ 2 is: `echo $number ^ 2 | bc -l`"
done

