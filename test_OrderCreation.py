from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data to store orders and order executions
orders = []
order_executions = []

# Definition Class Order
class Order:
    def __init__(self, id, bottle_type, quantity, status):
        self.id = id
        self.bottle_type = bottle_type
        self.quantity = quantity
        self.status = status

# Definition Class OrderExecution
class OrderExecution:
    def __init__(self, number, bottle_type, quantity, status):
        self.number = number
        self.bottle_type = bottle_type
        self.quantity = quantity
        self.status = status

# Endpoint to create a new order
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()

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
            'id': order.id,
            'bottle_type': order.bottle_type,
            'quantity': order.quantity,
            'status': order.status
        })
    return jsonify({'orders': orders_data})

# Endpoint to create a new order execution
@app.route('/order-executions', methods=['POST'])
def create_order_execution():
    data = request.get_json()

    new_execution = OrderExecution(
        number=data['number'],
        bottle_type=data['bottle_type'],
        quantity=data['quantity'],
        status=data['status']
    )

    order_executions.append(new_execution)
    return jsonify({'message': 'Order execution created successfully'}), 201

# Endpoint to get all order executions
@app.route('/order-executions', methods=['GET'])
def get_order_executions():
    executions_data = []
    for execution in order_executions:
        executions_data.append({
            'number': execution.number,
            'bottle_type': execution.bottle_type,
            'quantity': execution.quantity,
            'status': execution.status
        })
    return jsonify({'order_executions': executions_data})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
