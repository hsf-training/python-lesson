from setuptools import setup, find_packages
from os.path import abspath, dirname, join

here = abspath(dirname(__file__))

# Get the long description from the README file
with open(join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='python_lesson',
    version='0.0.2',
    description='Helper Functions for HSF Advanced Python Lesson',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hsf-training/python-lesson',
    author='HSF',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    setup_requires=[],
    install_requires=[],
    package_data={},
    zip_safe=True,
    project_urls={
        'Bug Reports': 'https://github.com/hsf-training/python-lesson/issues',
        'Source': 'https://github.com/hsf-training/python-lesson',
    },
)
