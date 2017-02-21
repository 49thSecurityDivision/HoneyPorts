#!/bin/bash
running=1

read port

while [ running ]; do
	nc -l -p $port
	echo "Port: $port" >> linuxports.log
done
