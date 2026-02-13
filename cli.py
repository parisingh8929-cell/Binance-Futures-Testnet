import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import validate_side, validate_type, validate_price
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        # Validate inputs
        validate_side(args.side)
        validate_type(args.type)
        validate_price(args.type, args.price)

        client = get_client()

        print("\n Order Summary:")
        print(vars(args))

        # Place Order
        response = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\n  SUCCESS")

        # Print Full Response
        print("\n  Full API Response:")
        print(response)

        # Safe Order Details Extraction
        print("\nOrd er Details:")

        if response and isinstance(response, dict):
            print("Order ID:", response.get("orderId", "Not returned"))
            print("Status:", response.get("status", "Not returned"))
            print("Executed Qty:", response.get("executedQty", "Not returned"))
            print("Avg Price:", response.get("avgPrice", "Not returned"))
        else:
            print("No valid response received from API")

    except Exception as e:
        print("\n FAILED:", str(e))


if __name__ == "__main__":
    main()
