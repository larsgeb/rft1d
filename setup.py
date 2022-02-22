import setuptools
from distutils.core import setup


long_description = """
**rft1d** is a Python package for exploring and validating Random Field Theory (RFT)
expectations regarding upcrossings in univariate and multivariate 1D continua.
These expectations can be used to make statistical inferences regarding signals
observed in experimentally measured 1D continua including scalar and vector time series.

This repo is restart of the original version from 2015, to keep it running on the newest
Python/PIP versions.
"""

setup(
    name="rft1d",
    version="0.2.0",
    description="One-Dimensional Random Field Theory",
    author="Todd Pataky, Lars Gebraad",
    author_email="lars.gebraad@erdw.ethz.ch",
    url="https://github.com/larsgeb/rft1d",
    download_url="https://github.com/larsgeb/rft1d/archive/master.zip",
    project_urls={
        "Bug Tracker": "https://github.com/larsgeb/rft1d/issues",
    },
    packages=setuptools.find_packages(),
    package_data={"rft1d": ["examples/*.*"]},
    long_description=long_description,
    keywords=["statistics", "time series analysis", "bayesian inference"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
    ],
    extras_require={
        "dev": [
            "black",
            "flake8",
        ]
    },
)
