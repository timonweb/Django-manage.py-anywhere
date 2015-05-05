# Django-manage.py-anywhere
Run manage.py commands anywhere. Find the closest to current path manage.py file and executes commands using it.

# Installation is quick and simple
One line installer:   
```
cd /usr/local/bin && sudo wget https://raw.githubusercontent.com/timonweb/manage.py-anywhere/master/manage.py && sudo chmod +x /usr/local/bin/manage.py
```

# Usage
Run ```manage.py``` anywhere. It will find closest manage.py file to your current position and execute it. 
The closer the file, the faster it will be found and executed. Usually, if you're within your Django code directory, manage.py will be found and executed very quickly.
