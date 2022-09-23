from src.newrl import add_token_transaction, add_wallet_transaction
from src.newrl import sign_transaction, generate_wallet_address
from src.newrl.wallet import generate_contract_address
from src.newrl.transaction import add_smart_contract_transaction, call_smart_contract_transaction

def test_token_creation():
    token_trans = add_token_transaction(
        'TKTST01',
        1,
        '0x001',
        '0x002',
        1000
    )

    assert token_trans is not None
    wallet = generate_wallet_address()
    signed_transaction = sign_transaction(wallet, token_trans)
    assert signed_transaction is not None


def test_add_wallet():
    wallet_transaction = add_wallet_transaction(
        '09c191748cc60b43839b273083cc565811c26f5ce54b17ed4b4a17c61e7ad6b880fc7ac3081b9c0df28756ea21ce501789b59e8f9103f3668ccf2c86108628ee',
        '0x001'
    )

    assert wallet_transaction is not None
    wallet = generate_wallet_address()
    signed_transaction = sign_transaction(wallet, wallet_transaction)
    assert signed_transaction is not None


def test_add_sc():
    contract_address = generate_contract_address()
    sc_transaction = add_smart_contract_transaction(
        contract_address,
        'test',
        '1.0',
        '0x001',
        {},
        {'someSpec': 'something'},
    )
    assert sc_transaction is not None

    sc_call_transaction = call_smart_contract_transaction(
        contract_address,
        'test',
        [],
        {}
    )
    assert sc_call_transaction is not None
