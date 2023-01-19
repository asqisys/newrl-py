from src.newrl.signer import *
from src.newrl.node import Node

node = Node('http://15.207.116.168:8421')


def test_sign_transaction():
    pass


def test_addresschecker():
    pass


def test_getvalidadds():
    pass


def test_verify_sign():
    data = {
        "timestamp": 1673748285000,
        "trans_code": "e35b0195b03656d0c2ca533235c96d1468c9ce40",
        "type": 4,
        "currency": "NWRL",
        "fee": 1000000,
        "descr": "",
        "valid": 1,
        "block_index": 0,
        "specific_data": {
                    "transfer_type": 4,
                    "asset1_code": "NWRL",
                    "asset2_code": "NUSDCTEST",
                    "wallet1": "0x97125800645cdb144f7d5c92adabd4a04c12042a",
                    "wallet2": None,
                    "asset1_number": 1000000000,
                    "asset2_number": 50000000,
                    "additional_data": {}
        },
        "is_child_txn": False,
        "fee_payer": "0x1342e0ae1664734cbbe522030c7399d6003a07a8"
    }
    signature = 'db422482e8a22ddb0ecbd7dd883e0a7d86bb85d8b4cab71ab0c705535144ffb677a12e83839c21afea546aff8f59eaa73a17fd0fc0b97227fd92d54ae9f5ebba'
    public_key = '1ebb4e373a50a8c05f1501a95f05fdf0aa60f6e4f7dd9081100d87712471da797e91c2d7efcec62193019e221dcd85c2250d3826a42750b54663ceb80ab99804'
    assert verify_sign(data, signature, public_key)
