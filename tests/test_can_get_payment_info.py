import pytest
from tests.utils.chain_model import Chain
from substrateinterface import SubstrateInterface, Keypair
from tests.data.setting_data import *

task_ids = [
    f'Test for {task.name}'
    for task in chains
]

@pytest.mark.parametrize("chain", chains, ids=task_ids)
class TestCanGetQueryInfo():

    def test_query_paiment_info(self, chain: Chain):
        substrate = chain.create_connection()
        test_keypair = Keypair.create_from_uri('//Alice')
        call = substrate.compose_call(
            call_module='Balances',
            call_function='transfer',
            call_params={
                'dest': test_keypair.ss58_address,
                'value': 0,
            }
        )
        query_info = substrate.get_payment_info(call=call, keypair=test_keypair)
        assert isinstance(query_info.partialFee, int)