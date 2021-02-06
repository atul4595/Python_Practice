import bs4
import requests
from pprint import pprint
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
url = 'https://www.amazon.in/s?k=watches&ref=nb_sb_noss_2'
proxies={'http':'13.92.119.142:80'}
username="atul4595@gmail.com"
password="@Tul1989"
# url="https://singlelogin.org/"

with requests.session() as session:
    response=session.get(url,headers=headers,proxies=proxies)
    print(response.text)

    with open(r'C:/Users/Jayendra/Desktop/Scrap/index.html',"w", encoding='utf-8') as f:
        f.write(response.text)

    # with open(str(filename) + ".html", "w", encoding='utf-8') as file1:
    #     file1.write(str(soup1))


# data=requests.get(url)
# soup=bs4.BeautifulSoup(data.text,"html.parser")
# print(soup.prettify())