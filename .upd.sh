#!/bin/bash
clear
if sudo apt update -y; then
	clear
	echo "updated"
elif apt update -y; then
	clear 
	echo "updated"
else
	clear
	echo "update manually"
fi

echo "Do you want to upgrade system"
read choice

if [[ "$choice" == "1" ]]; then
	if sudo apt upgrade -y; then
		echo "system upgraded"
	elif apt upgrade -y; then
		echo "system upgraded"
	else
		echo "upgrade manuall"
	fi
fi
