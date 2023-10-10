#!/bin/bash
read -p "Enter the first number: " number_1
read -p "Enter the second number: " number_2
read -p "Enter the action e.g.: +,-,*,/,**,sqrt: " action


calculate_sum() {
	echo "$1" + "$2" | bc -l
}

calculate_difference() {
	echo "$1" - "$2" | bc -l
}

calculate_multiplication() {
	echo ""$1" * "$2"" | bc -l
}

calculate_division() {
	echo "$1" / "$2" | bc -l
}

calculate_exponentiation() {
	echo "$1" ^ "$2" | bc -l
}

calculate_sqrt() {
	echo "sqrt ($1)" | bc -l
}

case "$action" in
	"+") echo " "$number_1" + "$number_2" =" $(calculate_sum "$number_1" "$number_2");;
	"-") echo " "$number_1" - "$number_2" =" $(calculate_difference "$number_1" "$number_2");;
	"*") echo " "$number_1" * "$number_2" =" $(calculate_multiplication "$number_1" "$number_2");;
	"/") 
		if [ "$number_2" -eq 0 ]
		then
			echo "Division by zero is not allowed!"
		else
			echo " "$number_1" / "$number_2" =" $(calculate_division "$number_1" "$number_2")
		fi
	       	;;
	"**") echo " "$number_1" ** "$number_2" =" $(calculate_exponentiation "$number_1" "$number_2");;
	"sqrt") echo " sqrt from "$number_1" =" $(calculate_sqrt "$number_1");;
	*) echo "Unknown action!"
esac
