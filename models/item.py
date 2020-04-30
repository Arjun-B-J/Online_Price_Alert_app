import requests
from bs4 import BeautifulSoup
import re
from typing import Dict
import uuid
from models.model import Model
from dataclasses import dataclass,field

@dataclass
class Item(Model):
    collection: str = field(init=False,default="Items")
    url:str
    tag_name: str
    query:Dict
    price:float = field(default=0)
    _id:str = field(default_factory=lambda: uuid.uuid4().hex)

    def load_price(self):
        reponse = requests.get(self.url)
        content = reponse.content
        soup = BeautifulSoup(content,"html.parser")
        element = soup.find(self.tag_name,self.query)
        price = element.text.strip()

        #using regular expression to match pattern
        pattern = re.compile(r"(\d+,?\d*\.\d\d)")
        match = pattern.search(price)
        temp = match.group(1)
        without_commas = temp.replace(",","")
        self.price = float(without_commas)
        return self.price

    def json(self) -> Dict:
        return{
            "_id":self._id,
            "url":self.url,
            "tag_name":self.tag_name,
            "price":self.price,
            "query":self.query
        }




