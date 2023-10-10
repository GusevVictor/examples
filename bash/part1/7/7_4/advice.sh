#!/bin/bash
while true
do
	echo "Please chouse from you want to give an advice: "
	cat << options
bunny
tux
daemon
kitty
vader-koala
options
echo
read -p "Make your chouse: " option
echo
fortune ru | cowsay -f "$option"
done

