from setuptools import find_packages, setup

setup(
    name='chainlink_web3',
    packages=find_packages(include=['chainlink_web3']),
    version='0.1.0',
    description='Chainlink Web3',
    author='Kalmia LTD',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.2', 'web3==6.11.0'],
    test_suite='tests',
)