"""Pakcage Metadata."""
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="bank-of-england",
    version="0.0.1",
    description="Retrieve data from the Bank of England's Statistical Interactive Database (IADB)",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/ronaldocpontes/bank-of-england",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    include_package_data=True,
    package_data={"": ["data/*.*"],},
    py_modules=["bank_of_england"],
    install_requires=["pandas", "requests"],
    extras_require={"dev": ["pytest", "tox"]},
)
