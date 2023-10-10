#!/bin/bash
read -p "Please enter outside web site. E.g.: ya.ru: " outside_internet_web_site

if nslookup "$outside_internet_web_site" &> /dev/null
then
	echo "DNS is work. Test host by ping echo send req"
	if ping -qc2 "$outside_internet_web_site" > /tmp/$(basename $BASH_SOURCE)_data.tmp 2>null
	then
		echo "Internet is working"
	else
		echo "Internet may be is not work! Please try another web site"
	fi
	echo "Ping statistic:"
	cat /tmp/$(basename $BASH_SOURCE)_data.tmp | tail -n3
	rm /tmp/$(basename $BASH_SOURCE)_data.tmp
else
	echo "DNS is not working! Please try another web site"
fi
