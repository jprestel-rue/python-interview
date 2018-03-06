#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from collections import namedtuple


Transaction = namedtuple(
    'Transaction',
    (
        'description',
        'currency_amount_in_dollars'
    )
)
