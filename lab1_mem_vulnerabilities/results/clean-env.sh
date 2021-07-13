#!/bin/bash

if [ $# -eq 0 ]; then
	echo "Usage: $0 BIN PORT"
	echo "clean-env runs the given server binary BIN using the configuration CONFIG in"
	echo "a pristine environment to ensure predictable memory layout between executions."
	exit 0
fi

killall -w zookld zookd zookfs zookd-nxstack zookfs-nxstack zookd-exstack zookfs-exstack &> /dev/null
cp gdb_home $HOME/.gdbinit
ulimit -s unlimited

DIR=$(pwd -P)
if [ "$DIR" != /home/httpd/labs/lab1_mem_vulnerabilities ]; then
    echo "========================================================"
    echo "WARNING: Lab directory is $DIR"
    echo "Make sure your lab is checked out at "
    echo "/home/httpd/labs/lab1_mem_vulnerabilities"
    echo "========================================================"
fi
# setarch -R disables ASLR
echo exec env - PWD="$DIR" SHLVL=0 setarch "$(uname -m)" -R "$@"
exec env - PWD="$DIR" SHLVL=0 setarch "$(uname -m)" -R "$@"
