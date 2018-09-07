import pandas as pd
import decimal
import requests
from bs4 import BeautifulSoup

page3 = requests.get('http://www.netstate.com/states/tables/st_governors.htm')

soup3 = BeautifulSoup(page3.text, "html.parser")
for body in soup3("body"):
    body.unwrap()

tables3 = pd.read_html(str(soup3), flavor="bs4")

pd.set_option('display.max_rows', len(tables3))

for i in range(4, len(tables3[0][3])):
	print(tables3[0][3][i])
