import os
import sys
from setuptools import setup, find_packages


setup(
    name="tensorboard_aggregator",
    version=0.1,
    description="Description here",
    license="Apache 2.0",
    packages=find_packages(),
    package_data={},
    scripts=[],
    install_requires=["pandas", "numpy", "tensorflow", "tensorboard"],
    extras_require={"test": ["pytest", "pylint!=2.5.0"],},
    entry_points={'console_scripts': [
            'tf2csv = tensorboard_aggregator.tensorboard_aggregator:console_entry_point',
        ],},
    classifiers=[],
    tests_require=["pytest"],
    setup_requires=["pytest-runner"],
    keywords=["tensorflow", "tensorboard"],
)
