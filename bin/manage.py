#!/bin/bash
# Yes, this is not python file, but it has .py extension to make it sound as vanilla Django manage.py file.
#
# One line installer: 
# pip install django_managepy_anywhere

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