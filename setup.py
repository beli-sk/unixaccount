#!/usr/bin/env python
# vim: set fileencoding=UTF-8 :
#
# Unix Account - python module to manipulate unix system accounts
# Copyright (C) 2014 Michal Belica <devel@beli.sk>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
import os, io
from setuptools import setup, find_packages

def read(*names, **kwargs):
    return io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

setup(
    name="unixaccount",
    version="0.1.0",
    url='https://github.com/beli-sk/unixaccount',
    license='GPL',
    description="Python module to manipulate unix system accounts.",
    long_description=read('README.rst'),
    author='Michal Belica',
    author_email='devel@beli.sk',
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 2.7',
        'Topic :: Utilities',
    ],
    package_dir = {'': 'src'},
    py_modules=['unixaccount'],
)

