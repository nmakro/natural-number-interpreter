import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="number-interpreter-pkg-nmakro",
    version="1",
    author="Nikolaos Makropoulos",
    author_email="nmakro@gmail.com",
    description="A natural number interpreter for greek telephone numbers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    scripts=['bin/interpreter'],

)
