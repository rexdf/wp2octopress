#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages
import sys
import wp2oct.authoring
from wp2oct.version import get_version

setup(
    name='wp2oct',
    description='A script to convert Wordpress XML dumps to plain text/markdown files.',
    version=get_version(),
    license=wp2oct.authoring.__license__,
    author=wp2oct.authoring.__author__,
    author_email=wp2oct.authoring.__email__,
    url=wp2oct.authoring.__url__,
    long_description=open('README.md').read(),
    platforms=['any'],
    packages=find_packages(),
    install_requires=[
      'markdown',
      'html2text'
    ],
    entry_points={'console_scripts': ['wp2oct = wp2oct.wp2oct:main']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
       'Development Status :: 5 - Production/Stable',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: GNU General Public License (GPL)',
       'Programming Language :: Python',
       'Programming Language :: Python :: 2.7',
       'Programming Language :: Python :: 3.3',
    ],
    dependency_links=[
        'https://github.com/aaronsw/html2text/tarball/master#egg=html2text'
    ],
)
