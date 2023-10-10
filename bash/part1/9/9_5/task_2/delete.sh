#!/bin/bash

trash_directory="$HOME/TRASH"

if [ -z "$1" ]
then
	echo "Please run script with a file name or a folder name for delete."
	exit 1
fi

test -d "$trash_directory" || mkdir $_

tar cavf "$trash_directory"/"$1".tar.lzma "$1" && rm -rf "$1"

find "$trash_directory"/* -mtime +2 -exec rm -f {} \;

