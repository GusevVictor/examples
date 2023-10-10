#!/bin/bash
# Check if two arguments there
if [ $# -ne 2 ]
then
	echo "You need two arguments. Original and Target files"
	exit 1
fi

# Check if original file exist
if [ ! -f "$1" ]
then
	echo "original file "$1" does not exist"
	exit 1
fi

if cp -rp "$1" "$2" && rm -rf "$1"
then
	echo "File "$1" was rename to file "$2""
	exit 0
else
	echo "Error! Something was wrong!"
	exit 1
fi
