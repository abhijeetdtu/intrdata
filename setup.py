import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt" , "r") as req:
    requirements = req.read().split("\n")

setuptools.setup(
    name="intrdata", # Replace with your own username
    version="0.0.1",
    author="abhijeetdtu",
    author_email="abhijeetdtu@gmail.com",
    description="Create 2d Datasets- interactively",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
