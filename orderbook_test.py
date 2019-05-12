#!/usr/bin/env python
# -*- coding: utf-8 -*-

# orderbook_test.py

import unittest
from unittest import skip
import inspect
from datetime import datetime

from orderbook_hw_MP import OrderBook


def orderbook_test_fixture(orderbook):
    """
    reads in a txt file from current directory.
    sends order to orderbook order by order.
    """
    with open('sample_trades.txt', 'r') as f:
        while True:
            order = f.readline()
            data = order.split('|')
            if order == '':
                break

            orderbook.process_order(order)


class TestOrderBookMethods(unittest.TestCase):

    def test_has_init_method(self):
        self.assertTrue(inspect.isfunction(OrderBook.__init__))

    def test_has_process_order_string_method(self):
        self.assertTrue(inspect.isfunction(OrderBook.process_order))

    def test_has_add_oder_method(self):
        self.assertTrue(inspect.isfunction(OrderBook._add_order))

    def test_has_modify_order_method(self):
        self.assertTrue(inspect.isfunction(OrderBook._modify_order))

    def test_has_remove_order_method(self):
        self.assertTrue(inspect.isfunction(OrderBook._remove_order))

    def test_has_get_order_method(self):
        self.assertTrue(inspect.isfunction(OrderBook.get_order))

    def test_has_get_top_of_book_method(self):
        self.assertTrue(inspect.isfunction(OrderBook.get_top_of_book))

    def test_has_clear_book_method(self):
        self.assertTrue(inspect.isfunction(OrderBook.clear_book))

    def test_has_refresh_book_method(self):
        self.assertTrue(inspect.isfunction(OrderBook.refresh_book))


class TestOrderBookAttributes(unittest.TestCase):

    def test_has_empty_attribute(self):
        ob = OrderBook()
        # since you have the freedom to design your orderbook class the way
        # you wish, I need an attribute that tells me whether or not
        # your book is empty which I will use in the tests below.
        self.assertTrue(hasattr(ob, "empty"))


class TestOrderBookInterface(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.orderbook = OrderBook()
        orderbook_test_fixture(cls.orderbook)

    def test_book_not_empty(self):
        self.assertFalse(self.orderbook.empty)

    def test_get_top_of_book(self):
        tob = self.orderbook.get_top_of_book()
        expected_tob = {"bid": 25.4, "ask": 25.9}
        self.assertEqual(tob, expected_tob)

    def test_get_order(self):
        order = self.orderbook.get_order(86)
        self.assertEqual(order.order_id, 86)

    def test_clear_book(self):
        self.orderbook.clear_book()
        self.assertTrue(self.orderbook.empty)

    def test_refresh_book(self):
        # This is just a dummy function which should return a string
        # The idea for this function is to make a call back to the exchange
        # to send over a fresh orderbook
        refresh_return = self.orderbook.refresh_book()
        self.assertEqual(refresh_return, "refresh book")
        self.assertTrue(self.orderbook.empty)


class TestOrderBookPerformance(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.orderbook = OrderBook()
        orderbook_test_fixture(cls.orderbook)

    def test_new_order(self):
        new_order = "B|95|AAPL|NYSE|100|19.6|1557342590.08421"
        ts = datetime.now()
        self.orderbook.process_order(new_order)
        te = datetime.now()
        tt = te - ts
        print(f"test_new_order took {tt.seconds} seconds and  {tt.microseconds} microseconds")

    def test_modify_order(self):
        mod_order = "M|87|AAPL|NYSE|200|17.1|1557342590.08421"
        ts = datetime.now()
        self.orderbook.process_order(mod_order)
        te = datetime.now()
        tt = te - ts
        print(f"test_modify_order took {tt.seconds} seconds and  {tt.microseconds} microseconds")

    def test_cancel_order(self):
        can_order = "C|87|AAPL|NYSE|75|23.3||1557342590.08421"
        ts = datetime.now()
        self.orderbook.process_order(can_order)
        te = datetime.now()
        tt = te - ts
        print(f"test_cancel_order took {tt.seconds} seconds and  {tt.microseconds} microseconds")


if __name__ == '__main__':
    unittest.main(verbosity=2, failfast=True)