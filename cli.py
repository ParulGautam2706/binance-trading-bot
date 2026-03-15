import argparse
from bot.orders import place_market_order, place_limit_order
from bot.validators import validate_side, validate_order_type, validate_quantity
from bot.logging_config import setup_logging

def main():

    setup_logging()

    parser = argparse.ArgumentParser(description="Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--qty", required=True)
    parser.add_argument("--price")

    args = parser.parse_args()

    try:

        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.qty)

        print("\nOrder Summary")
        print("------------------")
        print("Symbol:", args.symbol)
        print("Side:", args.side)
        print("Type:", args.type)
        print("Quantity:", args.qty)

        if args.type == "MARKET":

            order = place_market_order(
                args.symbol,
                args.side,
                args.qty
            )

        elif args.type == "LIMIT":

            if not args.price:
                raise ValueError("Price required for LIMIT order")

            order = place_limit_order(
                args.symbol,
                args.side,
                args.qty,
                args.price
            )

        print("\nOrder Response")
        print("------------------")
        print("Order ID:", order["orderId"])
        print("Status:", order["status"])
        print("Executed Qty:", order["executedQty"])

    except Exception as e:

        print("Error:", e)

if __name__ == "__main__":
    main()