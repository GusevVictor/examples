#!/bin/bash

report_file=report.txt
until cat "$report_file" 2>null
do
	echo "We are waiting for "$report_file""
	sleep 5
done
