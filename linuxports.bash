#!/bin/bash

portlist="4000 4001 4002"

declare -a children=()

for port in $portlist
do
	nc -l -p $port & children+=" $!"
done

echo $children
for pid in $children
do
	kill $pid
done