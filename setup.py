import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyrealpro",
    version="0.0.1",
    author="Nicholas Gower",
    author_email="nicholasgower01@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/splendidtoad/pyrealpro",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Software Development :: Libraries"
    ],
    python_requires='>=3.10',
)
