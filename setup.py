from setuptools import find_packages, setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='real-time-analog-monitoring-tool',
    version='0.0.9',
    description='A tool for real time analog monitoring.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nickovic/rtamt',
    author='Nickovic Dejan, Tomoya Yamaguchi',
    author_email='dejan.nickovic@ait.ac.at, tomoya.yamaguchi@toyota.com',
    license='BSD',
    python_requires='>=2.7',
    install_requires=[
        'antlr4-python2-runtime==4.5',
        'enum34'
    ],
    package_data={'': ['*.so']},
    packages=find_packages(),

    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: C++',
    ],
)
