from setuptools import setup

setup(
    name='which_block',
    url='https://github.com/cbrooks42/which_block',
    author='Chris Brooks',
    author_email='madbury@gmail.com',
    packages=['which_block'],
    install_requires=['web3'],
    version='0.1',
    license='GPL-3.0',
    description='Accepts a contract address and a web3 host, quickly traverses the block chain, and returns the block hash and transaction hash in which the contract was deployed.',
    long_description=readfile('README.md'),
)