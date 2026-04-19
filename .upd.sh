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
echo "1. yes"
echo "2. no"
read choice

if [[ "$choice" == "1" ]]; then
	if sudo apt upgrade -y; then
		echo "system upgraded"
	elif apt upgrade -y; then
		echo "system upgraded"
	else
		echo "upgrade manually by running sudo apt upgrade -y"
	fi
fi
