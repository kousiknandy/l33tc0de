#!/bin/bash

tokens=$(for i in `cat words.txt`
	 do
	     echo $i
	 done)

sorted=$(echo $tokens | tr ' ' '\n' | sort)
words=$(echo $sorted | tr ' ' '\n' | uniq)

freq=$(
    for w in `echo $words`
    do
	echo -n "$w," 
	   echo $sorted | tr ' ' '\n' | grep -c $w
    done
    )
echo $freq | tr ' ' '\n' | sort -nrk2 -t, | tr ',' ' '
