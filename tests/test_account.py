#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from rue.account import Account
from rue.transaction import Transaction


class TestAccount:
    def test_get_account_number(self):
        a = Account('11111')
        assert a.get_account_number() == '11111'

    def test_get_transactions(self):
        a = Account('11111')
        expected = [
            Transaction(
                description='a sweet watch',
                currency_amount_in_dollars=59.99),
            Transaction(
                description='rad sunglasses',
                currency_amount_in_dollars=9.99),
        ]
        assert a.get_transactions() == expected

    def test_get_last_transactions(self):
        a = Account('33333')
        expected = [
            Transaction(
                description='ugly blouse',
                currency_amount_in_dollars=134.99),
            Transaction(
                description='mickey mouse sweatshirt',
                currency_amount_in_dollars=89.99),
        ]
        assert a.get_last_transactions(2) == expected

    def test_eq(self):
        a1 = Account('11111')
        a2 = Account('11111')
        assert a1 == a2
