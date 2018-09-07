import collections
import pyperclip
import requests
from bs4 import BeautifulSoup
import xlsxwriter
import pandas as pd
import pprint

url = "http://icleiusa.org/membership/"
page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")
for body in soup("body"):
    body.unwrap()

#tables = pd.read_html(str(soup), flavor="bs4")

#pd.set_option('display.max_rows', len(tables))

pprint(str(soup).encode("utf-8"))