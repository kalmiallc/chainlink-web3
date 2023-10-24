from . import abis
from . import types

class ChainlinkUtils:
    def __init__(self, w3, default_aggregator_interface_abi:list = None):
        if not w3:
            raise Exception('Web3 instance not set')
        
        self.w3 = w3
        self.default_aggregator_interface_abi = \
            abis.AGGREGATOR_V3_INTERFACE_ABI if default_aggregator_interface_abi is None else default_aggregator_interface_abi

    """
	Calls the `latestRoundData` method on a deployed `aggregator_interface_abi` contract.
	More information about `latestRoundData` could be found at https://docs.chain.link/docs/data-feeds/price-feeds/api-reference/#latestrounddata
	
	@returns A `Price` object from deployed `aggregator_interface_abi` contract.
	"""
    def get_price(self, price_feed_address: str, aggregator_interface_abi:list = None) -> types.Price:
        price_feed_address = price_feed_address.upper()
        if not self.w3.is_address(price_feed_address):
            raise Exception(f'Provided price_feed_address is not a valid address: {price_feed_address}')
        
        price_feed_address = self.w3.to_checksum_address(price_feed_address)

        feed_contract = self.w3.eth.contract(
            address=price_feed_address,
            abi=self.default_aggregator_interface_abi \
                if aggregator_interface_abi is None else aggregator_interface_abi
        )

        if not feed_contract.find_functions_by_name('latestRoundData'):
            raise Exception('Unable to get price, provided aggregator_interface_abi is missing latestRoundData method')

        result = feed_contract.functions.latestRoundData().call()

        return types.Price(
            roundId=result[0],
            answer=result[1],
            startedAt=result[2],
            updatedAt=result[3],
            answeredInRound=result[4]
        )