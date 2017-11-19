import requests
import xml.etree.ElementTree as ET
from textblob import TextBlob

reqdoc = requests.get("https://finance.google.com/finance/company_news?q=NASDAQ:GOOGL&ei=E_0QWon_No6besrVqJgN&output=rss")
positivity=0
opinion=0
noOfnews=0
root = ET.fromstring(reqdoc.text)
for n in root.iter('title'):
    print(n.text)
    noOfnews+=1
    text = TextBlob(n.text)
    factor = TextBlob(n.text).sentiment
    opinion += factor.subjectivity
    positivity += factor.polarity
finalfactor = (opinion / noOfnews) * (positivity / noOfnews)
print ("Final factor",finalfactor)