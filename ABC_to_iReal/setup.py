from setuptools import setup
from Cython.Build import cythonize


setup(
    name="ABC to Ireal",
    ext_modules=cythonize("src/*.pyx",force=True,annotate=True)
)