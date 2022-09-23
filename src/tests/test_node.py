import time
from src.newrl import add_token_transaction, Node
from src.newrl import sign_transaction

WALLET = {"public": "09c191748cc60b43839b273083cc565811c26f5ce54b17ed4b4a17c61e7ad6b880fc7ac3081b9c0cf28756ea21ce501789b59e8f9103f3668ccf2c86108628ee", "private": "d63e7ca37bcd6b43a6bdf281b2f9b4de7e64f027c0f741ffe12a105bf3955ec7", "address": "0x667663f36ac08e78bbf259f1361f02dc7dad593b"}

def test_submit_transaction():
    token_trans = add_token_transaction(
        token_code='TST489347893',
        token_type=1,
        custodian_address='0x667663f36ac08e78bbf259f1361f02dc7dad593b',
        first_owner='0x667663f36ac08e78bbf259f1361f02dc7dad593b',
        amount=50
    )

    node = Node('http://devnet.newrl.net:8420')
    initial_balance = node.get_balance('TOKEN_IN_WALLET', '0x667663f36ac08e78bbf259f1361f02dc7dad593b', 'TST489347893')
    initial_balance = initial_balance if initial_balance is not None else 0
    assert token_trans is not None
    signed_transaction = sign_transaction(WALLET, token_trans)
    assert signed_transaction is not None
    response = node.submit_transaction(signed_transaction)
    time.sleep(15)
    new_balance = node.get_balance('TOKEN_IN_WALLET', '0x667663f36ac08e78bbf259f1361f02dc7dad593b', 'TST489347893')
    assert new_balance - initial_balance == 50
    assert response is not None

def test_submit_transactions():
    node = Node('http://devnet.newrl.net:8420')
    initial_balance = node.get_balance('TOKEN_IN_WALLET', '0x667663f36ac08e78bbf259f1361f02dc7dad593b', 'TST489347893')
    initial_balance = initial_balance if initial_balance is not None else 0

    transaction_list = []
    token_trans = add_token_transaction(
        token_code='TST489347893',
        token_type=1,
        custodian_address='0x667663f36ac08e78bbf259f1361f02dc7dad593b',
        first_owner='0x667663f36ac08e78bbf259f1361f02dc7dad593b',
        amount=50
    )
    signed_transaction = sign_transaction(WALLET, token_trans)
    transaction_list.append(signed_transaction)
    token_trans = add_token_transaction(
        token_code='TST489347893',
        token_type=1,
        custodian_address='0x667663f36ac08e78bbf259f1361f02dc7dad593b',
        first_owner='0x667663f36ac08e78bbf259f1361f02dc7dad593b',
        amount=50
    )
    
    signed_transaction = sign_transaction(WALLET, token_trans)
    transaction_list.append(signed_transaction)

    
    response = node.submit_transactions(transaction_list)
    time.sleep(15)
    new_balance = node.get_balance('TOKEN_IN_WALLET', '0x667663f36ac08e78bbf259f1361f02dc7dad593b', 'TST489347893')
    assert new_balance - initial_balance == 100
    assert response is not None
