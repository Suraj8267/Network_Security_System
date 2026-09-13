from setuptools import setup, find_packages
from typing import List




setup(
    name="Network Security System",
    author="Suraj Singh",
    author_email="singhsuraj182005@gmail.com",
    version='0.0.1',
    packages= find_packages(),
    requires= ["numpy", "pandas"]
)