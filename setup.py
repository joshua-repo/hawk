from pybind11.setup_helpers import Pybind11Extension, build_ext
from setuptools import setup, find_packages
import pybind11

ext_modules = [
    Pybind11Extension(
        "hawk_core",
        [
            "src/cpp/bindings/python_bindings.cpp",
            "src/cpp/lib/portfolio.cpp", 
            "src/cpp/lib/trade.cpp",
            "src/cpp/lib/core.cpp",
        ],
        include_dirs=["src/cpp/include", pybind11.get_cmake_dir()],
        cxx_std=14,
    ),
]

setup(
    name="hawk",
    version="1.0.0",
    package_dir={"": "src/python"},
    packages=find_packages(where="src/python"),
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
    python_requires=">=3.10",
)