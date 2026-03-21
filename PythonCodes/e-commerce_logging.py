import logging


logging.basicConfig(filename="PythonCodes/order_processing.log",
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG,
                    filemode='a')

logger = logging.getLogger()

def process_order(order):
    logger.info(f"Order {order['order_id']} received from {order['customer_name']}")

    for item in order['items']:
        if item["quantity"] > 3:
            logger.warning(f"Item {item["item_name"]} (ID:{item["item_id"]}) is out of stock.")
    
    logger.error(f"Payment processing failed for Order {order['order_id']}. Infsufficient funds.")

    logger.info(f"Order {order['order_id']} successfully completed.")


order = {
    "order_id": 101,
    "customer_name": "John Doe",
    "address": "123 Main St, Springfield",
    "items": [
        {"item_id": 1, "item_name": "Laptop", "quantity": 1, "price": 1000},
        {"item_id": 2, "item_name": "Mouse", "quantity": 2, "price": 25},
        {"item_id": 3, "item_name": "Keyboard", "quantity": 5, "price": 50}
    ],
    "total_amount": 1250
}

process_order(order)

