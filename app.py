""" from models.item import Item

url = "https://www.johnlewis.com/house-by-john-lewis-bonn-upholstered-bed-frame-double-saga-grey/p3711105"
tag_name = "p"
query = {"class":"price price--large"}

 got_thing = Item(url,tag_name,query)
got_thing.save_to_mongo()
 
items_loaded = Item.all()

print(items_loaded[0].load_price())
 """

from models.alert import Alert

alert = Alert("1f3fde0b990a4641a304c09535abb1c0",2000)
alert.save_to_mongo()