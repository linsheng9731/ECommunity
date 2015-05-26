#! /bin/bash

 cat ./pm.txt | while read line
 do
 	pip install $line
	echo $line
done
