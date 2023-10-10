#!/bin/bash

trash_directory="$HOME/TRASH"
target_object="$1"
target_object_type="dir_or_file"

main_function() {
	test -d "$trash_directory" || mkdir $_
	check_target_object_is_exist "$target_object"
	check_target_object_type "$target_object"
	do_action_with_target "$target_object" "$target_object_type" "$trash_directory"
	find "$trash_directory"/* -mtime +1 -delete
}

check_target_object_is_exist() {
	if ! stat $"$1" &> /dev/null
	then
		echo "Please run script with a real file name or a real folder name for delete."
		exit 1
	fi
}

check_target_object_type() {
	test -L "$1" && target_object_type="softlink"
	[[ $(ls -li "$1" | cut -d " " -f 3) -gt 1 ]] && target_object_type="hardlink"
}

do_action_with_target() {
	case $2 in
	
		"softlink")
		echo "Softlink was removed."
	        echo "The origin file $(file "$1" | cut -d " " -f 5) was not touched."
		unlink "$1"
		;;

		"hardlink")
		echo "Deleting "$1"..."
		echo "Link list to the hardlink file: $(find $HOME -inum $(ls -li "$1" | cut -d " " -f 1))"
		rm -f "$1"
		;;

		"dir_or_file")
		tar cavf "$3"/"$1".tar.lzma "$1" && rm -rf "$1"
		;;
	esac
}

main_function

