from setuptools import setup

setup(
    name="fs2json",
    version="0.1.0",
    author="Andrew Serra",
    author_email="andy@serra.us",
    description="A command-line tool to convert a directory to a json format",
    readme="README.md",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    requires=">=3.7",
    package_dir="src",
    script_name="cli.py"
)
