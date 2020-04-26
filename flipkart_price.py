import requests
from bs4 import BeautifulSoup
import re

URL="https://www.flipkart.com/lipton-honey-lemon-green-tea-bags-box/p/itmewjx9atpdgjm4?pid=TEAETC92QZFTY8RR&lid=LSTTEAETC92QZFTY8RR9WEBPK&marketplace=FLIPKART&srno=b_1_1&otracker=hp_creative_card_1_7.creativeCard.CREATIVE_CARD_PW3YILG1WBEP&fm=neo%2Fmerchandising&iid=deaab80c-33e3-46cc-910b-8657543d7a81.TEAETC92QZFTY8RR.SEARCH&ppt=browse&ppn=browse&ssid=sqgkt2cu7o356ku81587853103696"
TAG_NAME = "div"
QUERY = {"class":"_1vC4OE _3qQ9m1"}
reponse = requests.get(URL)

content = reponse.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find(TAG_NAME,QUERY)
price = element.text.strip()
print(price)

#using regular expression to match patter
pattern = re.compile(r"(\d+)")
match = pattern.search(price)
temp = match.group(1)
without_commas = temp.replace(",","")
price = float(without_commas)

print(price)