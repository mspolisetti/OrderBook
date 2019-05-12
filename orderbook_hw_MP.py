import sys
import math
#from collections import deque  # a faster insert/pop queue
#from six.moves import cStringIO as StringIO
from decimal import Decimal

from OrderTree import OrderTree

class OrderBook(object):
    def __init__(self, tick_size=0.0001):
        #self.tape = deque(maxlen=None)  # Index[0] is most recent trade
        self.bids = OrderTree()
        self.asks = OrderTree()
        self.time = 0
        self.empty = True

    def update_time(self):
        self.time += 1

    def process_order(self, oline, verbos=None ):
        self.empty = False
        fld = oline.split('|')
        o = dict(side=fld[0], order_id=fld[1], symbol=fld[2], exchange=fld[3]
                 , quantity=int(fld[4]), price=fld[5], timestamp=fld[6])

        if o['quantity'] <= 0:
            sys.exit('process_order() given order of quantity <= 0')

        o['price'] = Decimal(o['price'])
        self._add_order(o)

    def get_order(self, order_id):
        if self.bids.order_exists(order_id):
            return self.bids.get_order(order_id)
        elif self.asks.order_exists(order_id):
            return self.asks.get_order(order_id)

    def _add_order(self, o):
        if o["side"] == 'B':
            self.bids.insert_order(o)
        elif o["side"] == 'A':
            self.asks.insert_order(o)
        elif o["side"] == 'M':
            self._modify_order(int(o["order_id"]), o)
        elif o["side"] == 'T':
            pass
        elif o["side"] == 'C':
            self._remove_order(int(o["order_id"]))
        else:
            sys.exit('add_order() given neither "bid" nor "ask"')

    def _remove_order(self, order_id, time=None):
        if time:
            self.time = time
        else:
            self.update_time()
            if self.bids.order_exists(order_id):
                self.bids.remove_order_by_id(order_id)
            elif self.asks.order_exists(order_id):
                self.asks.remove_order_by_id(order_id)
            else:
                sys.exit('Order NOT FOUND to Cancel')

    def _modify_order(self, order_id, order_update, time=None):
        if time:
            self.time = time
        else:
            self.update_time()
        order_update['order_id'] = order_id
        order_update['timestamp'] = self.time
        if self.bids.order_exists(order_update['order_id']):
            self.bids.update_order(order_update)
        elif self.asks.order_exists(order_update['order_id']):
            self.asks.update_order(order_update)
        else:
            sys.exit('Order not found to modify')

    def clear_book(self):
        self.bids = OrderTree()
        self.asks = OrderTree()
        self.empty = True

    def refresh_book(self):
        self.clear_book()
        return "refresh book"

    def get_top_of_book(self):
        return dict(bid=float(self.get_best_bid()), ask=float(self.get_best_ask()))

    def get_volume_at_price(self, side, price):
        price = Decimal(price)
        if side == 'bid':
            volume = 0
            if self.bids.price_exists(price):
                volume = self.bids.get_price(price).volume
            return volume
        elif side == 'ask':
            volume = 0
            if self.asks.price_exists(price):
                volume = self.asks.get_price(price).volumoe
            return volume
        else:
            sys.exit('get_volume_at_price() given neither "bid" nr "ask"')

    def get_best_bid(self):
        return self.bids.max_price()

    def get_worst_bid(self):
        return self.bids.min_price()

    def get_best_ask(self):
        return self.asks.min_price()

    def get_worst_ask(self):
        return self.asks.max_price()

