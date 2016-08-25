#!/usr/bin/env python
from setuptools import setup, find_packages

__doc__ = "Python wrapper for yr weather service"

install_requires = [
    'xmltodict>=0.9.2',
]


version = '0.0.1.dev0'

PACKAGE_NAME = 'py_yr'

setup(
    name=PACKAGE_NAME,
    version=version,
    author="Sindre Nerdal",
    author_email="Sindre.nerdal@gmail.com",
    url="https://github.com/Matmonsen/py-yr",
    keywords="python yr xml",
    description=__doc__,
    #long_description=read('README.rst') + '\n\n' + read('CHANGELOG.rst'),
    packages=find_packages(),
    install_requires=install_requires,
    py_modules=['yr'],
    #tests_require=
    #zip_safe=
    #test_suite=
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        #'Framework :: ',
        #'Intended Audience :: Developers',
        #'License :: OSI Approved :: BSD License',
        #'Topic :: Internet :: WWW/HTTP',
        #'Programming Language :: Python',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
    ],
)