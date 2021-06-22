#!/usr/bin/bash
for i in {0..34}
do
  if [ $i -lt 10 ]
  then
    mkdir "level0$i"
    touch "level0$i/level0$i.txt"
  else
    mkdir "level$i"
    touch "level$i/level$i.txt"
  fi
done
