from setuptools import find_packages, setup

setup(
    name='real-time-analog-monitoring-tool',
    version='0.0.0',
    description='A tool for real time analog monitoring.',
#    url='http://github.com/',
    author='Niokovic Dejan, Tomoya Yamaguchi',
    author_email='dejan.nickovic@ait.ac.at, tomoya.yamaguchi@toyota.com',
    license='BSD',
	python_requires='>=2.7',
    install_requires=[
		'antlr4-python2-runtime==4.5',
	],
	package_data={'': ['*.so']},
    packages=find_packages(),
)
