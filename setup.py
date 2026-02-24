# coding: utf-8
from setuptools import setup, find_packages
from os import path as os_path
from rplibs._version import __version__

## INFOS ##
package = "rplibs"
descr = "Libraries for rpTools"
url = "https://github.com/brsynth/rplibs"
authors = "Joan Hérisson, Melchior du Lac, Thomas Duigou"
corr_author = "joan.herisson@univ-evry.fr"

## LONG DESCRIPTION
with open(
    os_path.join(os_path.dirname(os_path.realpath(__file__)), "README.md"),
    "r",
    encoding="utf-8",
) as f:
    long_description = f.read()


setup(
    name=package,
    version=__version__,
    author=authors,
    author_email=corr_author,
    description=descr,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=url,
    packages=find_packages(),
    package_dir={package: package},
    include_package_data=True,
    test_suite="pytest",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
