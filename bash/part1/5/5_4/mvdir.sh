#!/bin/bash
# Check if original dir exists
if [ $# -ne 2 ]
then
	echo "You need two argument. Original and Target dirs"
	exit 1
fi

# Check if original dir exists
if [ ! -d "$1" ]
then
	echo "original dir "$1" does not exists"
	exit 1
fi

# Check if target dir exists
if [ ! -d "$2" ]
then
	echo "target dir "$2" does not exists"
	exit 1
fi

if cp -rp "$1" "$2" && rm -rf "$1"
then
	echo "Directory "$1" was moved to directory "$2""
	exit 0
else
	echo "Error! Something was wrong!"
	exit 1
fi
