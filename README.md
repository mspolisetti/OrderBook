# OrderBook

Limit Order Book for high-frequency trading (HFT)

Based on WK Selph's Blogpost:

http://howtohft.wordpress.com/2011/02/15/how-to-build-a-fast-limit-order-book/

Available at Archive.org's WayBackMachine:

https://goo.gl/KF1SRm

An orderbook is an important part of any trading system. It represents a collection of orders/quotes being placed by traders where bids are the prices at which traders are willing to buy goods and offers/asks are the prices at which traders are willing to sell.

To replicate and exchange orderbook, a trader requires a constant stream of bids and offers. The exchange facilitates this by sending via multi-cast orders and trades that occur in the market. There are a number of protocols exchanges use to structure and send messages; A few are provided here:

FIX
FIX Protocol
Web FIX Parser
Python FIX Parser
FAST

FAST Protocol
There are many different types of orderbooks. We have the order-driven and the quote-driven orderbook. (https://www.investopedia.com/ask/answers/06/quoteorderdrivenmarket.asp). You can read about the differences here. Then there are differences in order priority, that is the order in which traders queue up to make purchases or offers. It is universal that price takes number one priority, but size, timestamp, and others, maybe secondary, tertiary, etc. e.g. In a price-timestamp priority, the trader with the earliest bid at the highest price takes priority in execution over a trader with the second earliest bid at the highest price. There is also price-size-time priority.

Overview
This project has our own orderbook implementation 

Speed at which you can query, add, remove, orders in the orderbook is of importance. We strive for O(1) complexity, but sometimes that's just not possible.  

You will be provided a .txt file that contains a number of trade simulations using the DONADIO Protocol.
This information will be in the following format:

"[B,A,T,C]|order_id|symbol|exchange|quantity|price|timestamp"
where [<B,A,T,C>] represents an optional field that, if present, will contain one of B, A, T, or C for bid, ask, trade, or cancel, respectively.

for example, a buy limit order might look like this:

"B|103|AAPL|NYSE|230|345.67|1555985032.036956"
and a modification to the order might look like this:

"103|AAPL|NYSE|130|345.67|1555985032.036956"
and, finally, a trade might look like this:

"T|103|AAPL|NYSE|130|400|1555985032.036956"

The way in which these orders make it in to the orderbook is through the "process_order" method. This methods does the job of parsing the order string and dispatching it the correct method add_order, modify_order, or remove_order. These functions alter the state of the orderbook. The others allow read access to the orderbook so a traders can have ways to "view" the book.
