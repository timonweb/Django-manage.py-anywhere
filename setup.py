from distutils.core import setup
setup(
  name = 'django_managepy_anywhere',
  version = '1.0',
  description = 'Run your django manage.py commands from any directory within a project',
  author = 'Tim Kamanin',
  author_email = 'tim@timonweb.com',
  url = 'https://github.com/timonweb/Django-manage.py-anywhere', # use the URL to the github repo
  download_url = 'https://github.com/timonweb/Django-manage.py-anywhere/archive/master.zip', # I'll explain this in a second
  keywords = ['django', 'management', 'commands'], # arbitrary keywords
  scripts=['bin/manage.py'],
)