from chainlink_web3.utils import ChainlinkUtils, types
from web3 import HTTPProvider, Web3
import pytest 

def test_missing_web3_instance():
    with pytest.raises(Exception) as excinfo:  
        ChainlinkUtils(w3=None) 
    assert str(excinfo.value) == 'Web3 instance not set'  

def test_get_price():
    providers = [
        'https://eth.public-rpc.com',
        'https://nodes.mewapi.io/rpc/eth',
        'https://ethereum.publicnode.com',
        'https://rpc.ankr.com/eth',
        'https://rpc.flashbots.net/',
    ]

    result=None
    for provider in providers:
        try:
            chainlink = ChainlinkUtils(
                w3=Web3(HTTPProvider(provider, request_kwargs={'timeout': 180}))
            )
            result = chainlink.get_price(
                price_feed_address=types.MAINNET_PRICE_FEEDS['LinkEth']
            )
            break
        except:
            pass

    if not result:
        raise Exception('It seems all Providers endpoints, used for the test, had issues')
    
    
    result_variables = dir(result)
    for keyword in [
        'roundId', 
        'answer', 
        'startedAt', 
        'updatedAt', 
        'answeredInRound'
    ]:
        assert keyword in result_variables

def test_invalid_feed_address():
    chainlink = ChainlinkUtils(
        w3=Web3(HTTPProvider('https://eth.public-rpc.com', request_kwargs={'timeout': 180}))
    )
    with pytest.raises(Exception) as excinfo:  
        chainlink.get_price(price_feed_address='INVALID_ADDRESS')
    assert str(excinfo.value) == \
        'Provided price_feed_address is not a valid address: INVALID_ADDRESS'

def test_missing_abi_function():
    chainlink = ChainlinkUtils(
        w3=Web3(HTTPProvider('https://eth.public-rpc.com', request_kwargs={'timeout': 180})),
        default_aggregator_interface_abi=[]
    )

    # Test custom abi passed to constructor
    with pytest.raises(Exception) as excinfo:  
        chainlink.get_price(
            price_feed_address=types.MAINNET_PRICE_FEEDS['LinkEth']
        )
    assert str(excinfo.value) == \
        'Unable to get price, provided aggregator_interface_abi is missing latestRoundData method'
    
    # Test custom abi passed to get_price function
    with pytest.raises(Exception) as excinfo:  
        chainlink.get_price(
            price_feed_address=types.MAINNET_PRICE_FEEDS['LinkEth'], 
            aggregator_interface_abi=[]
        )
    assert str(excinfo.value) == \
        'Unable to get price, provided aggregator_interface_abi is missing latestRoundData method'