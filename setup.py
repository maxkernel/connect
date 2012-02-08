#!/usr/bin/env python

import os
from setuptools import setup

def read(fname):
	return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
	name='maxconnect',
	version='0.5',
	description='Coroutine-based networking library',
	author='Andrew Klofas',
	author_email='andrew@maxkernel.com',
	url='http://www.maxkernel.com',
	packages=['maxconnect'],
	long_description=read('README'),
	classifiers=[
		"License :: OSI Approved :: GNU General Public License (GPL)",
		"Programming Language :: Python",
		"Development Status :: 4 - Beta",
		"Intended Audience :: Developers",
		"Topic :: Utilities",
	],
	keywords='maxkernel robotics automation',
	license='GPL',
	entry_points={
        'gui_scripts': [
            'max-deploy = maxconnect.main:gui_deploy',
        ]
    },
)
