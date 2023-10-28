import io
import os
import re

from setuptools import find_packages
from setuptools import setup
from pip._internal.req import parse_requirements


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type("")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


# parse_requirements() returns generator of pip._internal.req.InstallRequirement objects
install_reqs = parse_requirements("./requirements.txt", session="hack")
# reqs is a list of requirements
reqs = [str(ir.requirement) for ir in install_reqs]

setup(
    name="emblio",
    version="0.1.4",
    url="https://github.com/nishantb06/emblio",
    license="MIT",
    author="Nishant Bhansali",
    author_email="nishantbhansali80@gmail.com",
    description="python package that gets embeddings from various ML models for  different content types, like image video audio text",
    long_description=read("README.rst"),
    packages=find_packages(exclude=("tests",)),
    install_requires=["torch", "whisper"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
