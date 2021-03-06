import os
import sys

from setuptools import setup
from setuptools.command.install import install
from setuptools import find_packages

#Change this on major/minor version number change. You must create a git tag at the same tag called with the same value
# git tag "0.1"
# git push --tags
VERSION = "0.1"


def __path(filename):
    return os.path.join(os.path.dirname(__file__),filename)

#Change this on major version number
#major_minor_version = 1.0
#This will be overriden if build.info exists
build = os.getenv('CIRCLE_BUILD_NUM',0)

if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

version= '{0}.{1}'.format(str(VERSION),str(build))




def readme():
    """print long description"""
    with open('README.rst') as f:
        return f.read()


class VerifyVersionCommand(install):
    """Custom command to verify that the git tag matches our version"""
    description = 'verify that the git tag matches our version'

    def run(self):
        tag = os.getenv('CIRCLE_TAG')

        if tag != VERSION:
            info = "Git tag: {0} does not match the version of this app: {1}".format(
                tag, VERSION
            )
            sys.exit(info)

setup(
    name="inol_rest",
    version=version,
    description="Inol RESTful API",
    long_description=readme(),
    url="https://github.com/awalker125/inol_rest",
    author="awalker125",
    author_email="awalker125@users.noreply.github.com",
    license="MIT",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7"
    ],
    keywords='inol api',
    packages=['inol_rest'],
    package_dir={'':'src'},
    install_requires=['futures','flask'],
    python_requires='>=2.7',
    include_package_data=True,
    zip_safe=False,
    cmdclass={
        'verify': VerifyVersionCommand,
    }
)

