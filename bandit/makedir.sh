#!/usr/bin/bash
for i in {0..34}
do
  mkdir "level$i"
  cd "level$i"
  touch "level$i.txt"
  cd ..
done
