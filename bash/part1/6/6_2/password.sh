#!/bin/bash

read -p "Please enter a username: " username
if [ "$username" = "Viktor" ]
then
	read -sp "Please enter a password: " user_password
	if [ "$user_password" = "123" ]
	then
		echo "Добро пожаловать!"
	else
		echo "Wrong password"
		exit 1
	fi
else
	echo "bad username"
	exit 1
fi
