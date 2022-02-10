from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='For the February 2022 Tabular Playground Series competition, your task is to classify 10 different bacteria species using data from a genomic analysis technique that has some data compression and data loss. In this technique, 10-mer snippets of DNA are sampled and analyzed to give the histogram of base count. In other words, the DNA segment  becomes . Can you use this lossy information to accurately predict bacteria species?',
    author='antptv',
    license='',
)
