#!/bin/bash

running=1
portlist="4000 4001 4002"

declare -a children=()

for port in $portlist
do
	echo $port | ./linuxports.helper.bash &
	children+=" $!"
done

trap ctrl_c INT

function ctrl_c() {
	echo "Force Quitting..."
	for pid in $children
	do
		kill $pid
	done
	killall nc
	exit
}

echo "Press Enter To Quit..."
read

echo "Quitting..."
for pid in $children
do
	kill $pid
done
killall nc