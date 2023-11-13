from setuptools import find_packages, setup

def read_file(file):
   with open(file) as f:
        return f.read()
    
long_description = read_file("README.md")

setup(
    name='chainlink_web3',
    packages=find_packages(include=['chainlink_web3']),
    version='0.1.2',
    url="https://github.com/kalmiallc/chainlink-web3",
    description='Library for interacting with Chainlink Ethereum contracts.',
    long_description_content_type="text/markdown",
    long_description=long_description,
    author='Kalmia LTD',
    author_email = 'itkalmia@kalmia.si',
    license = "MIT license",
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==7.4.2', 'web3==6.11.0'],
    test_suite='tests',
)