from setuptools import setup, find_packages
from io import open

setup(
    name='ScholrAdmin',
    version='0.0.01',
    author='Jorge Alpedrinha Ramos',
    author_email='jalpedrinharamos@gmail.com',
    packages=find_packages(),
    #package_data = { '': ['*.yml']},
    #scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    #url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Django admin boosted for front end web apps',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django == 1.5.1",
    ],
)