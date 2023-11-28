from typing import List

import requests
import json
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Order:
    def __init__(self, id, type, quantity, status):
        self._id = id
        self._type = type
        self._quantity = quantity
        self._status = status

    @property
    def id(self):
        return self._id

    @property
    def type(self):
        return self._type

    @property
    def quantity(self):
        return self._quantity

    @property
    def status(self):
        return self._status

response = requests.get('https://65663055eb8bb4b70ef3043d.mockapi.io/api/v1/liquors')

# Asegúrate de que la solicitud fue exitosa
response.raise_for_status()

data = response.json()

orders_db = data
# In-memory database to store orders
# for order in orders_db:
#    order_id = order['id']
#    order_type = order['type']
#    quantity = order['quantity']
#    status = order['status']


# orders_db = {}

class OrderCreate(BaseModel):
    type: str
    quantity: int
    status: str

class OrderUpdate(BaseModel):
    type: str
    quantity: int
    status: str

class OrderResponse(BaseModel):
    id: int
    type: str
    quantity: int
    status: str

@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    order_id = len(orders_db) + 1
    order_obj = Order(id=order_id, type=order.type, quantity=order.quantity, status=order.status)
    orders_db.append(order_obj)
    return {"id": order_id, "type": order.type, "quantity": order.quantity, "status": order.status}

@app.get("/orders/{order_id}", response_model=OrderResponse)
def read_order(order_id: int):
    order = orders_db.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return {"id": order.id, "type": order.type, "quantity": order.quantity, "status": order.status}

@app.get("/orders/", response_model=List[OrderResponse])
def read_orders(skip: int = 0, limit: int = 10):
    return [{"id": order.id, "type": order.type, "quantity": order.quantity, "status": order.status} for order in orders]

@app.put("/orders/{order_id}", response_model=OrderResponse)
def update_order(order_id: int, order_update: OrderUpdate):
    order = orders_db.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    order.type = order_update.type
    order.quantity = order_update.quantity
    order.status = order_update.status

    return {"id": order.id, "type": order.type, "quantity": order.quantity, "status": order.status}

@app.delete("/orders/{order_id}", response_model=dict)
def delete_order(order_id: int):
    order = orders_db.pop(order_id, None)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    
    return {"message": "Order deleted successfully"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
