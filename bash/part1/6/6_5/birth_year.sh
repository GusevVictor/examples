#!/bin/bash

read -p "Please enter your birth year: " birth_year
echo "You was born in "$birth_year"". So, you are $(expr $(date "+%Y") - "$birth_year") "years old. You too young for die!"
