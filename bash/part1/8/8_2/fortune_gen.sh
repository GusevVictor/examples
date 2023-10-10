#!/bin/bash

for fortune_number in {1..10}
do
	echo "Fortune $fortune_number : $(fortune ru -s -n 160 | head -n 1)" >> /tmp/fortunes.txt
done
