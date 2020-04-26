import requests
from bs4 import BeautifulSoup
import re
from typing import Dict
import uuid
from models.model import Model
class Item(Model):
    collection = "Items"
    def __init__(self,url:str ,tag_name: str,query: Dict,_id: str =None):
        super().__init__()
        self.url = url
        self.tag_name = tag_name
        self.query = query
        self.price = None
        self._id = _id or uuid.uuid4().hex

    def __repr__(self):
        return f"<Item {self.url}>"

    def load_price(self):
        reponse = requests.get(self.url)
        content = reponse.content
        soup = BeautifulSoup(content,"html.parser")
        element = soup.find(self.tag_name,self.query)
        price = element.text.strip()

        #using regular expression to match patter
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
            "query":self.query
        }




