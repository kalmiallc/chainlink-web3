# Web3.py Chainlink Library

The **Web3.py Chainlink Library** is a Chainlink Python library designed to simplify the interaction with Chainlink Ethereum contracts. It provides an easy and streamlined way to retrieve real-time prices using the Chainlink price oracle. The library is dependent on [Web3.py](https://pypi.org/project/web3), so you'll need to provide an active instance during initialization.

Once initialized, you can make use of the `get_price` function. This function essentially invokes the `latestRoundData` function on the Chainlink price feed contract. As a result, the `get_price` function returns a `Price` object containing all the data retrieved from the blockchain call.

This library empowers Python developers by eliminating the need to write complex blockchain calls directly. Instead, it enables them to leverage the Chainlink price feed in a more familiar and simple manner.

## Table of content

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using this library](#using-this-library)
  - [Installing web3.py](#installing-web3py)
  - [Usage example](#usage-example)
  - [Plugin Methods](#plugin-methods)
    - [Price Feed Addresses](#price-feed-addresses)
    - [`get_price`](#get_price)
- [Found an issue or have a question or suggestion](#found-an-issue-or-have-a-question-or-suggestion)
- [Build & install locally](#build--install-locally)
  - [Build with docker](#build-with-docker)
- [Useful links](#useful-links)


## Prerequisites

- [Python 3.7.2+](https://www.python.org/)
- [pip](https://pip.pypa.io/en/stable/)
- [web3.py 6.0.0+](https://pypi.org/project/web3)

## Installation

```bash
pip3 install chainlink-web3
```

## Using this library

### Installing web3.py

```
pip3 install web3
```

### Usage example

```py
from web3 import Web3, HTTPProvider
from chainlink_web3.utils import ChainlinkUtils, types

w3 = Web3(HTTPProvider('https://rpc.ankr.com/eth', request_kwargs={'timeout': 180}))

chainlink = ChainlinkUtils(w3=w3)
result = chainlink.get_price(types.MAINNET_PRICE_FEEDS['LinkEth'])

print(result)
```

### Plugin Methods

#### Price Feed Addresses

Included in this library are two dicts that contain the Ethereum contract addresses for specific token pairs: [MAINNET_PRICE_FEEDS](https://github.com/kalmiallc/chainlink-web3/blob/master/chainlink_web3/types.py#L12) and [SEPOLIA_PRICE_FEEDS](https://github.com/kalmiallc/chainlink-web3/blob/master/chainlink_web3/types.py#L263). If you cannot find your desired price feed within these dicts, please check [here](https://docs.chain.link/docs/data-feeds/price-feeds/addresses) to make sure it's supported, and if it is, please open an issue or a pull request for the missing price feed so that it can be added to the appropriate dict.

#### `get_price`

```py
def get_price(
    self, 
    price_feed_address: str, 
    aggregator_interface_abi:list = None
    ) -> types.Price:

# class Price:
#     roundId: str
#     answer: str
#     startedAt: str
#     updatedAt: str
#     answeredInRound: str
```

`aggregator_interface_abi` can be found [here](https://github.com/kalmiallc/chainlink-web3/blob/master/chainlink_web3/abis.py).

The `get_price` method, accepts evm address for it's first parameter, and an optional second parameter for specifying the Chainlink Aggregator Interface ABI of the Ethereum smart contract you'd like to interact with (the parameter is defaulted to [aggregator_interface_abi](https://github.com/kalmiallc/chainlink-web3/blob/master/chainlink_web3/abis.py)).

Under the hood, this method is calling the `latestRoundData` for the specified price feed, more information about it can be found [here](https://docs.chain.link/data-feeds/price-feeds/api-reference#latestrounddata).

```py
from web3 import Web3, HTTPProvider
from chainlink_web3.utils import ChainlinkUtils, types

w3 = Web3(HTTPProvider('https://rpc.ankr.com/eth', request_kwargs={'timeout': 180}))

chainlink = ChainlinkUtils(w3=w3)
result = chainlink.get_price(types.MAINNET_PRICE_FEEDS['LinkEth'])
# Price(
#     roundId=36893488147419106338, 
#     answer=164576918062797, 
#     startedAt=1697700215, 
#     updatedAt=1697700215, 
#     answeredInRound=36893488147419106338
# )
```

## Found an issue or have a question or suggestion

- If you found an issue or have a question or suggestion [submit an issue]() or join us on [Discord](https://discord.gg/yjyvFRP)
  ![Discord](https://img.shields.io/discord/593655374469660673.svg?label=Discord&logo=discord)

## Build & install locally

1. Clone repo
2. Install dependencies

```bash
pip3 install wheel
pip3 install setuptools
pip3 install twine
```

3. Run the tests
```bash
python3 setup.py pytest
```

4. Generate .whl file for external use
```bash
python3 setup.py bdist_wheel
```

This creates a `./dist` folder that contains a `.whl` file.

Use the bellow command to install the lib on your local environment:

```bash
pip3 install /path/to/wheelfile.whl
```
### Build with docker

1. Clone repo

2. Create docker image
```bash
chmod +x ./run-docker.sh
./run-docker.sh install
```

3. Test lib
```bash
./run-docker.sh test
```

4. Generate .whl file for external use
```bash
./run-docker.sh build
```

This creates a `./dist` folder that contains a `.whl` file.

Use the bellow command to install the lib on your local environment:

```bash
pip3 install /path/to/wheelfile.whl
```

## Useful links

- [web3.py Documentation](https://web3py.readthedocs.io/en/latest/index.html)
- [Chainlink Documentation](https://docs.chain.link/docs)
