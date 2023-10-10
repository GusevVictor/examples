#!/bin/bash


unarchive_file() {

	dir_name=unarchived_$(echo "$1" | sed 's/\./_/g')_$(date +'%H-%M-%S-%d-%m-%Y')

	case "$1" in 

	*.gz|*.bz2|*.lzma)
		mkdir -p "$dir_name" ; cd "$_" ; tar xvaf ../"$1" ;;

	*.zip)
		check_unzip_is_installed
		unzip -o "$1" -d "$dir_name" ;;

	*)
		echo "Unsupported archive extension. Only support: gz,bz2,lzma,zip"
	        exit 1 ;;
	esac
}

check_unzip_is_installed() {

	if ! [ -x "$(command -v unzip)" ]
	then
		echo "Error: unzip is not installed. Please install it!" >&2
		exit 1
	fi
}


if [ -z "$1" ]
then
	echo "Please give an archive file as an argument to unarchive"
	exit 1
else
	unarchive_file "$1"
fi
