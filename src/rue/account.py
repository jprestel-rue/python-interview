#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from rue.db import Db, SQLException
from rue.transaction import Transaction


class Account:
    def __init__(self, account_number):
        # constructor
        self.account_number = account_number
        # self.name = name

    def get_account_number(self):
        return self.account_number  # return the account number

    # def get_name(self):
    #     return self.name

    def get_transactions(self):
        try:
            db_transaction_list = Db.get_transactions(
                self.account_number.strip())
            # Get the list of transactions
            transaction_list = list()
            i = 0
            while i < len(db_transaction_list):
                db_row = db_transaction_list[i]
                trans = self.make_transaction_from_db_row(db_row)
                transaction_list.append(trans)
                i += 1
            return transaction_list
        except SQLException:
            # There was a database error
            raise Exception('Can\'t retrieve transactions from the database')

    def get_last_transactions(self, n):
        all_transactions = self.get_transactions()
        last_n_transactions = []
        count = 0
        while count < n:
            last_n_transactions.append(
                all_transactions[len(all_transactions)-n+count])
            count = count + 1
        return last_n_transactions

    def make_transaction_from_db_row(self, row):
        currency_amount_in_dollars = float(row.get_value_for_field('amt'))
        description = row.get_value_for_field('desc')
        return Transaction(
            description=description,
            currency_amount_in_dollars=currency_amount_in_dollars)
        # return the new Transaction object

    # Override the equals method
    def __eq__(self, other):
        return other.get_account_number() == self.get_account_number()
        # check account numbers are the same
