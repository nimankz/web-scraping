#required libraries
import requests
from bs4 import BeautifulSoup
from json import loads as json_loads
import csv

URL = "https://www.zoomit.ir/"
page = requests.get(URL)
soup = BeautifulSoup(page.text)

#getting info from website
results = soup.find(id="__NEXT_DATA__")
myResults=json_loads(results.string)

#gathering the information which we needed.
myResults2=myResults["props"]['pageProps']['editorialModules']['leftSection'][0]['chips'][0]["items"]
finalInfo=[["number","title","IMG preview","publish date","author"]]
i=1
for content in myResults2:
    finalInfo.append({"number":i,"title":content["title"],"IMG preview":content['coverImageLink']['preview'],
                      "publish date":content['publishedDate'],"author":content['author']['fullName']})
    i+=1

#transfaring these information from short term memory to long term memory.
myfile=open(r"finalResults.csv","w",encoding='UTF8')
writer = csv.DictWriter(myfile, fieldnames=finalInfo[0])
writer.writeheader()
writer.writerows(finalInfo[1:])
myfile.close()