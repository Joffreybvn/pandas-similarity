import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pandas-similarity",
    version="1.0.0",
    description="Python library for measuring similarity between entries of a Pandas Dataframe.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/joffreybvn/pandas-similarity",
    author="Joffrey Bienvenu",
    author_email="joffreybvn@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["pandas_similarity"],
    include_package_data=True,
    install_requires=["pandas", "scikit-learn", "nltk", "numpy"]
)