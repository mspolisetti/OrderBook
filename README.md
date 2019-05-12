# OrderBook

Limit Order Book for high-frequency trading (HFT)

Based on WK Selph's Blogpost:

http://howtohft.wordpress.com/2011/02/15/how-to-build-a-fast-limit-order-book/

Available at Archive.org's WayBackMachine:

https://goo.gl/KF1SRm

"There are three main operations that a limit order book (LOB) has to
implement: add, cancel, and modify.  The goal is to implement these
operations in O(1) time while making it possible for the trading model to
efficiently ask questions like “what are the best bid and offer?”

The vast majority of the activity in a book is usually made up of add and
cancel operations as market makers jockey for position.  An add
operation places an order at the end of a list of orders to be executed at
a particular limit price, a cancel operation removes an order from anywhere
in the boo. Each
of these operations is keyed off an id number (Order.order_id in the
pseudo-code below), making a hash table a natural structure for tracking
them.

