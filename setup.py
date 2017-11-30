from distutils.core import setup

setup(
    name='django_managepy_anywhere',
    version='2.0',
    description='Allows to run manage.py commands from any level of the Django project by typing "manage.py <subcommand>"',
    author='Tim Kamanin',
    author_email='tim@timonweb.com',
    url='https://timonweb.com/oss/django-managepy-anywhere/',
    download_url='https://github.com/timonweb/Django-manage.py-anywhere/archive/master.zip',
    keywords=['django', 'management', 'commands'],
    scripts=['bin/manage.py'],
)
