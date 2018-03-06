#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class SQLException(Exception):
    pass


class Db(object):
    """ Mock implementation of a database access object. """
    @staticmethod
    def get_transactions(account_number):
        try:
            return mock_transaction_data[account_number]
        except Exception:
            raise SQLException('the world is ending. probably.')


class TransactionRow(object):
    """ Mock implementation of a database row. """
    def __init__(self, **data):
        self.data = data

    def get_value_for_field(self, field):
        return self.data[field]


# Mock database contents
mock_transaction_data = {
    '11111': [
        TransactionRow(desc='a sweet watch', amt='59.99'),
        TransactionRow(desc='rad sunglasses', amt='9.99'),
    ],
    '22222': [
        TransactionRow(desc='the prettiest dress', amt='199.99'),
    ],
    '33333': [
        TransactionRow(desc='gaudy heels', amt='699.99'),
        TransactionRow(desc='ugly blouse', amt='134.99'),
        TransactionRow(desc='mickey mouse sweatshirt', amt='89.99'),
    ],
    '44444': [
    ],
}
