from setuptools import setup
from Cython.Build import cythonize

kwargs="build_ext --inplace"
setup(
    name="ABC to Ireal",
    ext_modules=cythonize("ABCTune.pyx")
)