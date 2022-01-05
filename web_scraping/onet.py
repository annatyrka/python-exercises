import requests
import random

onet = requests.get("http://onet.pl")
print(onet.raise_for_status())
onet_txt = onet.text  # it will return html code
