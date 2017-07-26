from setuptools import setup
from sys import version_info

ver = version_info[:2]
if ver < (3, 6):
    raise SystemExit('datatyping requires python 3.6.0 or later!')


setup(
    name='datatyping',
    description='Type enforcement for python data structures.',
    license='MIT',
    version='0.0.1',
    author='Mark Jameson - aka theelous3',
    url='https://github.com/theelous3/datatyping',
    packages=['datatyping'],
    tests_require=['pytest'],
    classifiers=['Programming Language :: Python :: 3']
)
