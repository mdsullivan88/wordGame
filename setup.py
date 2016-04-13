## setup.py

try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
	
config = {
	'description': 'Simple command line word game',
	'author': 'Mitch Sullivan',
	'url': 'None',
	'download_url': 'None',
	'author_email': 'm.sullivan@mun.ca',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['wordGame'],
	'scripts': [],
	'name': 'wordGame'
}

setup(**config)

##