from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import json
from matplotlib import pyplot as plt
import numpy as np 


ZCASH_BASE="http://zcash.flypool.org/miners"
ZCASH_WALLET="xxxxxxx"
WALLET="xxxxxxx"
#response=requests.get("https://ethermine.org/miners/%s"%WALLET)
response=requests.get("%s/%s"%(ZCASH_BASE,ZCASH_WALLET))
bsObj=BeautifulSoup(response.text,"html5lib")

script_list=bsObj.findAll("script",{"type":"text/javascript"})

for s in script_list:
    print(s)
    pass

dataset=script_list[-2].get_text()
dataset=dataset.split("var workersChartData = ")[1]
dataset=json.loads(dataset)

average_hash_rate=[data['HR_M_LONG'] for data in dataset]
current_hash_rate=[data['HR_M_SHORT'] for data in dataset]

print(average_hash_rate)
print(current_hash_rate)

fig,ax=plt.subplots()
ax.plot(np.array(average_hash_rate).astype(np.float64))
ax.plot(np.array(current_hash_rate).astype(np.float64))

plt.show()