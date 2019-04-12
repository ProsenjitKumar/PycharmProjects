import os
from setuptools import setup
from pip.req import parse_requirements
from pip.download import PipSession

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="blood-donors-directory",
    version="0.0.3",
    author="Akhil Lawrence",
    author_email="akhilputhiry@gmail.com",
    description=("A web application to maintain blood donors database"),
    license="GNU GPLv3",
    keywords="blood donation",
    url="https://github.com/akhilputhiry/blood-donors-directory",
    packages=["bdd"],
    install_requires=[str(i.req) for i in parse_requirements("./requirements/install.txt", session=PipSession())],
    long_description=read("README.md"),
    classifiers=[
        "Development Status :: 1 - Planning",
        "Topic :: Internet :: WWW/HTTP",
        "Programming Language :: Python :: 2.7",
        "License :: Freeware",
    ],
)
