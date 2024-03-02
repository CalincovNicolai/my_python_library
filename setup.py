from setuptools import setup, find_packages

setup(
    name="py-kek",
    version="0.0.1",
    author="ncalincov",
    author_email="nicolai.calincov@gmail.com",
    url="",
    description="KEK lib",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    entry_points={"console_scripts": ["py-kek = py-kek.main:download"]},
)