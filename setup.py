from setuptools import setup

setup(
    name='which_block',
    url='https://github.com/cbrooks42/which_block',
    author='Chris Brooks',
    author_email='madbury@gmail.com',
    install_requires=['web3'],
    version='0.1',
    license='GPL-3.0',
    py_modules=['which_block'],
    description='Accepts a contract address and a web3 host, quickly traverses the block chain, and returns the block hash and transaction hash in which the contract was deployed.',
    entry_points = {
        'console_scripts': [
            'which-block=which_block:main',
        ],
    },
)
