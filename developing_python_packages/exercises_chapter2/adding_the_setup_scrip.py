# Import required functions
from setuptools import setup, find_packages

# Call setup function
setup(
    author="<your-name>",
    description="A package for converting imperial lengths and weights.",
    name="impyrial",
    packages=find_packages(include=["impyrial", "impyrial.*"]),
    version="0.1.0",
)
