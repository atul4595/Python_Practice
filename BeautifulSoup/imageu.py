import sys
from PyQt5.QtWidgets import QApplication
from  PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEnginePage
import requests

from bs4 import BeautifulSoup
import lxml
from pprint import pprint
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = "https://main.sci.gov.in/case-status#"
proxies={'http':'13.92.119.142:80'}


# url="https://singlelogin.org/"
response=requests.get(url,headers=headers)
soup = BeautifulSoup(response.content, features="html5lib")
with open(r'C:/Users/Jayendra/Desktop/Scrap/index.html',"w", encoding='utf-8') as file:
    file.write(str(soup))
paragraph=soup.find_all("p",attrs={"id":"cap"})
print(paragraph)