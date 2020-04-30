import uuid
from typing import Dict,List
from models.item import Item
from models.model import Model
from dataclasses import dataclass,field



class Alert(Model):
    collection="alerts"
    def __init__(self,name,item_id,price_limit,_id=None):
        self.name=name
        self.item_id=item_id
        self.price_limit=price_limit
        self._id = _id or uuid.uuid4().hex
        self.item = Item.get_by_id(item_id)
    
    def json(self) ->Dict:
        return{
            "_id":self._id,
            "name":self.name,
            "item_id":self.item_id,
            "price_limit":self.price_limit
        }

    def load_item_price(self):
        self.item.load_price()
        return self.item.price

    def notify_if_price_reached(self):
        if float(self.item.price) < float(self.price_limit):
            print(f"Item{self.item} has reached a price under {self.price_limit}. Latest price: {self.item.price}.")

