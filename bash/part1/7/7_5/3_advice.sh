#!/bin/bash
while true
do
	echo "Please type from you want to give an advice or type quit for exit: "
	cat << options
bunny
tux
daemon
vader-koala
options

	echo
	read -p "Make your chouse: " option

	if [ "$option" = "quit" ]
	then
		break
	else
		echo
		fortune ru | cowsay -f "$option"
fi
done

