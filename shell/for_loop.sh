#!/usr/bin/env bash

#for x in one two three four
for x in /etc/r*
do
    #echo number $x
    if [ -d "$x" ]
    then
        echo "$x (dir)"
    else
        echo "$x"
    fi
done
