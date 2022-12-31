from setuptools import setup, find_packages

setup(
    name="pybit",
    version="1",
    description="low-level storage and manipulation of data",
    long_description=open("README.md").read()
    author="IronRocket"
    license="MIT"
    packages=find_packages(),
)