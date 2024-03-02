from setuptools import setup, find_packages

setup(
    name="pykek",
    version="0.0.1",
    author="CalincovNicolai",
    author_email="nicolai.calincov@gmail.com",
    url="",
    description="KEK lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["pykek = pykek.main:main"]},
)