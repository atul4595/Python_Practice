import sqlite3
# import lxml
import re
import time
import requests
from bs4 import BeautifulSoup
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

proxies = {
 "http": "117.241.98.1:45229",
 "https": "117.241.98.1:45229"
}

payload = {
    'k': 'TV',
    'ref': 'nb_sb_noss_1'
    # 'k': 'watch for man',
    # 'crid': '4HATIKHROIVH',
    # 'sprefix': "watch f,aps,285",
    # 'ref': 'nb_sb_ss_i_1_7'
}
url = 'https://www.amazon.in/'
# url='https://www.amazon.in/s?k=mobile&ref=nb_sb_noss'
s = requests.Session()
r = s.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')
with open(r"C:\Users\Jayendra\Desktop\Pyt\Scrap.html", "w", encoding='utf-8') as file1:
    file1.write(str(soup))
# r = s.get(url, headers=headers,proxies=proxies)

def getdata(url,c):
    if c==1:
        r1=""
        time.sleep(2)
        r1=s.get(url + "s", params=payload, headers=headers)
        # r = s.get(url + "s", params=payload, headers=headers, proxies=proxies)
#         r = s.get(url,params=payload,headers=headers)
    else:
        r1 = ""
        r1 = s.get(url,headers=headers)
        # r = s.get(url, headers=headers, proxies=proxies)
#     r.html.render(sleep=1)
    soup = BeautifulSoup(r1.content, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    pages = soup.find('ul', {'class': 'a-pagination'})
    if not pages.find('li', {'class': 'a-disabled a-last'}):
        time.sleep(3)
        url = 'https://www.amazon.co.in' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
        return url
    else:
        return






def scraping(soup2):


    for i in soup2.find_all("a", {"class": "a-link-normal a-text-normal"}):
        l2 = []
        url2 = ""
        response2 = ""
        soup3 = ""
        Title = ""
        a = ""
        file3 = ""
        filename = ""
        url2 = "https://www.amazon.in" + str(i.get('href'))
        # print(url2)
        # response2 = requests.get(url2, headers=headers,proxies=proxies)
        response2 = requests.get(url2, headers=headers)
        soup3 = BeautifulSoup(response2.content, features="lxml")
        l2.append(url2)
        # print(soup3.title)
        if soup3.find(id="productTitle") is None:
            continue
        Title = soup3.find(id="productTitle").text.replace('\n', '')
        # print(Title)
        l2.append(Title)
        # print(Title)
        filename = re.sub('[^A-Za-z0-9]+', '', str(Title))
        print(l2)
        l1.append(l2)
        print(l1)
        with open("C:\\Users\\Jayendra\\Desktop\\Pyt\\" + str(filename) + ".html", "w", encoding='utf-8') as file3:
            file3.write(str(soup3))




l1 = []
counter=1
while True:
    data = getdata(url,counter)

    with open(r"C:\Users\Jayendra\Desktop\Pyt\Scrap" + str(counter) + ".html", "w", encoding='utf-8') as file1:
        file1.write(str(data))
    scraping(data)
    url = getnextpage(data)
    if not url:
        break
    print(url)

    counter=counter+1


conn = sqlite3.connect(r"C:\Users\Jayendra\Desktop\Pyt\example.db")
c = conn.cursor()
c.execute('''CREATE TABLE stocks
                 (URl TEXT, trans TEXT)''')
c.executemany('INSERT INTO stocks VALUES (?,?)', l1)
conn.commit()
conn.close()
