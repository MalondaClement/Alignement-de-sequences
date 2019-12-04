#! /bin/bash

for i in `ls ../Instances_genome`; do
    echo "$i" >>mesure.txt
    TIME = $({ time python3 sol_1.py ../Instances_genome/$i; } 2>>mesure.txt)
    echo "$i fait" >>mesure.txt
    sleep 5
done
