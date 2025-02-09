# setup.py

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_signalmap",
    version="0.1.1",
    author="Ibrahim Muhaisen",
    author_email="ibrahim.muhaisen.2015@gmail.com",
    description="A Django package to map and visualize signal connections",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hemaxox/django-signalmap",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
