from setuptools import setup

setup(
    name="fs2json",
    version="0.1.1",
    author="Andrew Serra",
    author_email="andy@serra.us",
    description="A command-line tool to convert a directory to a json format",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"fs2json": "src/fs2json"},
    script_name="cli.py"
)
