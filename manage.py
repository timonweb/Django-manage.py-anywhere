#!/bin/bash
# Install as: cd /usr/local/lib && sudo wget && sudo chmod u+x manage.py

managepy_path=0
while [[ "`pwd`" != '/' ]]; do
	managepy_path=$(find $(pwd) -type f -name "manage.py" -print | head -n 1)
	if [[ -n $managepy_path ]]; then
	    echo "Running 'python $managepy_path $@' command:"
		python $managepy_path $@
		break
	else
		cd ..
	fi
done 

if [[ managepy_path == 0 ]]; then
	echo 'Cant find manage.py'
fi