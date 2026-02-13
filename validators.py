def validate_side(side):
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_type(order_type):
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Type must be MARKET or LIMIT")

def validate_price(order_type, price):
    if order_type == "LIMIT" and price is None:
        raise ValueError("LIMIT order needs price")
