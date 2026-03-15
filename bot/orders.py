import logging
from bot.client import get_client

client = get_client()

def place_market_order(symbol, side, quantity):

    try:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        logging.info(f"Market order placed {order}")

        return order

    except Exception as e:

        logging.error(f"Market order failed {e}")

        raise


def place_limit_order(symbol, side, quantity, price):

    try:

        order = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logging.info(f"Limit order placed {order}")

        return order

    except Exception as e:

        logging.error(f"Limit order failed {e}")

        raise