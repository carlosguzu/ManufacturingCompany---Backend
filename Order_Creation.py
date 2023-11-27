from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to store orders
orders = []

# Definition Class Order
class Order:
    def __init__(self, id, bottle_type, quantity, status):
        self.id = id
        self.bottle_type = bottle_type
        self.quantity = quantity
        self.status = status

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    # Assuming the JSON data has 'id', 'bottle_type', 'quantity', and 'status' fields
    new_order = Order(
        id=data['id'],
        bottle_type=data['bottle_type'],
        quantity=data['quantity'],
        status=data['status']
    )

    orders.append(new_order)
    return jsonify({'message': 'Order created successfully'}), 201

# Endpoint to get all orders
@app.route('/orders', methods=['GET'])
def get_orders():
    orders_data = []
    for order in orders:
        orders_data.append({
            'id': order.get_id(),
            'bottle_type': order.get_bottle_type(),
            'quantity': order.get_quantity(),
            'status': order.get_status()
        })
    return jsonify({'orders': orders_data})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
