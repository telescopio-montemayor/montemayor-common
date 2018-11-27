import os
from setuptools import find_packages, setup

from montemayor.common import __version__


with open(os.path.join(os.path.dirname(__file__), 'README.md'), encoding='utf-8') as readme:
    README = readme.read()

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='montemayor-common',
    version=__version__,
    packages=find_packages(),
    namespace_packages=['montemayor'],
    include_package_data=True,
    install_requires=[
        'astropy',
        'attrs'
    ],
    license='AGPL-3.0',
    description='Shared code for Montemayor and related projects',
    long_description=README,
    long_description_content_type='text/markdown',
    url='http://github.com/telescopio-montemayor/montemayor-common',
    author='Adrián Pardini',
    author_email='github@tangopardo.com.ar',
    classifiers=[
        'Environment :: Web Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Education',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Communications',
        'Topic :: Education',
        'Topic :: Scientific/Engineering :: Astronomy'
    ],
    keywords='astronomy, telescope',
)
