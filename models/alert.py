import uuid
from typing import Dict,List
from models.item import Item
from models.model import Model
from dataclasses import dataclass,field


@dataclass(eq=False)
class Alert(Model):
    collection: str= field(init=False,default ="alerts")
    name: str
    item_id : str
    price_limit:float
    _id:str = field(default_factory=lambda: uuid.uuid4().hex)
    
    def __post_init__(self): 
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

