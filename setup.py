#!/usr/bin/env python3

# parse_requirements() returns generator of pip.req.InstallRequirement objects

# reqs is a list of requirement
# e.g. ['django==1.5.1', 'mezzanine==1.4.6']
with open('requirements.txt','r') as r:
    reqs = r.readlines()

import os
import codecs
from setuptools import setup

__version__ = "0.0.4"


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


def getversion():
    if 'BUILD_VERSION' in os.environ:
        return os.environ['BUILD_VERSION']
    else:
        return __version__

setup(
    python_requires='>=3.8',  # Your supported Python ranges
    name='pytest-xdist',
    version=getversion(),
    url='https://github.com/kurt-cb/pytest-xdist',
    description='clone of xdist',
    license='GPL v3',
    long_description=open('README.rst').read(),
    install_requires=reqs,
    entry_points={"pytest11": ["xdist = xdist.plugin"]},
    # custom PyPI classifier for pytest plugins
    classifiers=["Framework :: Pytest"],
)
