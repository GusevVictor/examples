#!/bin/bash
read -p "Enter the first number: " number_1
read -p "Enter the second number: " number_2
read -p "Enter the action e.g.: +,-,*,/,**: " action

case "$action" in
	"+") echo " "$number_1" + "$number_2" =" $(expr "$number_1" + "$number_2");;
	"-") echo " "$number_1" - "$number_2" =" $(expr "$number_1" - "$number_2");;
	"*") echo " "$number_1" * "$number_2" =" $(expr "$number_1" \* "$number_2");;
	"/") 
		if [ "$number_2" -eq 0 ]
		then
			echo "Division by zero is not allowed!"
		else
			echo " "$number_1" / "$number_2" =" $(expr "$number_1" \/ "$number_2")
		fi
	       	;;
	"**") echo " "$number_1" ** "$number_2" =" $(( "$number_1" ** "$number_2"));;
	*) echo "Unknown action!"
esac
