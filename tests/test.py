from newrl import get_file_hash

print(get_file_hash('/Users/kousthub/Documents/US Visa.jpg'))

from newrl import sign_transaction


unsigned_transaction = {
    "timestamp": "2021-12-31 19:22:57.171918",
    "trans_code": "927e891a69ae861fa0991e403c6f29a1c43b8e55",
    "type": 2,
    "currency": "INR",
    "fee": 0,
    "descr": "New token creation",
    "valid": 1,
    "specific_data": {
    "tokenname": "NEWTOKEN",
    "tokentype": "string",
    "tokenattributes": {},
    "first_owner": "0x762485963e99f6a6548729f11d610dd37ffd3b73",
    "custodian": "0x762485963e99f6a6548729f11d610dd37ffd3b73",
    "legaldochash": "686f72957d4da564e405923d5ce8311b6567cedca434d252888cb566a5b4c401",
    "amount_created": 1000000,
    "value_created": 10000,
    "disallowed": [],
    "sc_flag": False
    }
}

wallet = {"address": "0xc29193dbab0fe018d878e258c93064f01210ec1a", "public": "sB8/+o32Q7tRTjB2XcG65QS94XOj9nP+mI7S6RIHuXzKLRlbpnu95Zw0MxJ2VGacF4TY5rdrIB8VNweKzEqGzg==", "private": "xXqOItcwz9JnjCt3WmQpOSnpCYLMcxTKOvBZyj9IDIY="}
signed_transaction = sign_transaction(wallet_data=wallet, transaction_data=unsigned_transaction)

print(signed_transaction)

from newrl import generate_wallet_address, get_address_from_public_key

wallet = generate_wallet_address()

address = get_address_from_public_key(wallet['public'])

assert wallet['address'] == address

from newrl import Node

node = Node()

balance = node.get_balance(
    'TOKEN_IN_WALLET', '0x16031ef543619a8569f0d7c3e73feb66114bf6a0', 10)
print(balance)

wallet = generate_wallet_address()

wallet_add_transaction = node.add_wallet(
    wallet['address'], '910', wallet['public'], 1)

print(wallet_add_transaction)

signed_wallet_add_transaction = sign_transaction(
    wallet, wallet_add_transaction)
print(signed_wallet_add_transaction)

token_add_transaction = node.add_token(
    'my_new_token',
    '1',
    '0x16031ef543619a8569f0d7c3e73feb66114bf6a0',
    '0x16031ef543619a8569f0d7c3e73feb66114bf6a0',
    'fhdkfhldkhf',
    10000,
    10000,
)

signed_token_add_transaction = sign_transaction(
    wallet, token_add_transaction)
print(signed_token_add_transaction)

transfer_transaction = node.add_transfer(
    9, 10, '0x16031ef543619a8569f0d7c3e73feb66114bf6a0', '0x16031ef543619a8569f0d7c3e73feb66114bf6a0', 10, 10, 4)
signed_transfer = sign_transaction(wallet, transfer_transaction)
print(signed_transfer)

validate_result = node.validate_transaction(signed_transfer)
print(validate_result)

print(node.run_updater())
