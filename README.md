> **2025 UPDATE:** I've come up with an even better idea to solve the inconvenience of having to type `python manage.py` every time. Let's just replace it with the `django` or, even shorter, the `dj` command! That's what my latest package, [Easy Django CLI](https://github.com/timonweb/easy-django-cli), does. I recommend you try it at first. Check it out here: [https://github.com/timonweb/easy-django-cli](https://github.com/timonweb/easy-django-cli).

# Django-manage.py-anywhere
Run manage.py commands from any directory of your Django project.

> NOTE: This tool doesn't need any further updates, so don't worry if you see that it hasn't got any updates recently. It doesn't need any. It just works with any Django version. Enjoy!

# Installation is quick and simple
One line installer:   
```
pip install django_managepy_anywhere
```

# Usage
Run ```manage.py``` from any directory of your Django project. It will find closest manage.py file to your current position and execute it. 
The closer the file, the faster it will be found and executed. Usually, if you're within your Django code directory, manage.py will be found and executed very quickly.

# Version 2.0
While version 1.0 was based on bash, I completely rewrote the script in v2.0 and now it uses Python to execute. Should be more reliable in different environments, especially in
Docker.
