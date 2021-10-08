#!/bin/bash

printf "> n = "
read n
cp $n.py $((n+1)).py

pwd=`python3 $n.py`
echo $pwd
# this changes the username in new file
sed -i -e "s/password[[:space:]]=[[:space:]]'.*'/password = '$pwd'/g"  -e "s/natas$((n))/natas$((n+1))/g"  $((n+1)).py
# this changes the password in the new file with the output of previous .py file
# sed -r "s/password\s=\s'.*'/password = '$pwd'/g" <$((n+1)).py >> $((n+1)).py
