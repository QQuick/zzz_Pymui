import os
import sys

sys.path.append ('pymui')
import __base__

from setuptools import setup

def read (*paths):
	with open (os.path.join (*paths), 'r') as aFile:
		return aFile.read()

setup (
	name = 'Pymui',
	version = __base__.pm_version,
	description = 'A Material UI library for Transcrypt',
	long_description = (
		read ('README.rst') + '\n\n' +
		read ('pymui/license_reference.txt')
	),
	keywords = ['transcrypt', 'react', 'material', 'pyact', 'python', 'browser'],
	url = 'https://github.com/QQuick/Pymui',	
	license = 'Apache 2.0',
	author = 'Jacques de Hooge',
	author_email = 'jacques.de.hooge@qquick.org',
	packages = ['pymui'],
	install_requires = [
		'transcrypt', 'pyact'
	],
	include_package_data = True,
	classifiers = [
		'Development Status :: 1 - Planning',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: Apache Software License',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.9',
	],
)
