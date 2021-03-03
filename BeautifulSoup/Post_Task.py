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
'searchCriteria.reference':'',
'searchCriteria.planningPortalReference':'',
'searchCriteria.alternativeReference':'',
'searchCriteria.description':'',
'searchCriteria.applicantName':'',
'searchCriteria.caseType':'',
'searchCriteria.ward':'',
'searchCriteria.parish':'',
'searchCriteria.conservationArea':'',
'searchCriteria.agent':'',
'searchCriteria.caseStatus':'',
'searchCriteria.caseDecision':'',
'searchCriteria.appealStatus':'',
'searchCriteria.appealDecision':'',
'searchCriteria.developmentType':'',
'caseAddressType':'Application',
'searchCriteria.address':'',
'date(applicationReceivedStart)':'',
'date(applicationReceivedEnd)':'',
'date(applicationValidatedStart)': '01/01/2021',
'date(applicationValidatedEnd)': '15/01/2021',
'date(applicationCommitteeStart)': '',
'date(applicationCommitteeEnd)': '',
'date(applicationDecisionStart)': '',
'date(applicationDecisionEnd)': '',
'date(appealDecisionStart)': '',
'date(appealDecisionEnd)': '',
'searchType': 'Application'
}
url = 'https://publicaccess.wycombe.gov.uk/idoxpa-web/advancedSearchResults.do?action=firstPage'
# url='https://www.amazon.in/s?k=mobile&ref=nb_sb_noss'
s = requests.Session()
r = s.post(url, headers=headers,data=payload)
print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')
with open(r"C:\Users\Jayendra\Desktop\Pyt\Scrap1.html", "w", encoding='utf-8') as file1:
    file1.write(str(soup))

# r = s.get(url, headers=headers,proxies=proxies)
#
def getdata(url):
    r1 = ""
    r1 = s.get(url,headers=headers)
    # r = s.get(url, headers=headers, proxies=proxies)
    #     r.html.render(sleep=1)
    soup = BeautifulSoup(r1.content, 'html.parser')
    return soup

def getnextpage(soup):
    # this will return the next page URL
    try:
        pages = soup.find('a', {'class': 'next'}).text
        if pages=='Next':
            Next_url="https://publicaccess.wycombe.gov.uk"+str(soup.find('a', {'class': 'next'}).get('href'))
            print(Next_url)
            return Next_url
    except:
        return

#     if not soup.find('a', {'class': 'a-disabled a-last'}):
#         time.sleep(3)
#         url = 'https://www.amazon.co.in' + str(pages.find('li', {'class': 'a-last'}).find('a')['href'])
#         return url
#     else:
#         return
# #
#
#
#
#

def scraping(soup2,c):
    counter1=1
    for i in soup2.find_all("li", {"class": "searchresult"}):
        # print(i.find('a').get('href'))
        url2 = "https://publicaccess.wycombe.gov.uk" + str(i.find('a').get('href'))
        r2=''
        r2 = s.get(url2, headers=headers)
        # r = s.get(url, headers=headers, proxies=proxies)
        #     r.html.render(sleep=1)
        soup1=''
        soup1 = BeautifulSoup(r2.content, 'html.parser')
        with open(r"C:\Users\Jayendra\Desktop\Pyt\Scrap"+str(c)+"-"+str(counter1)+".html", "w", encoding='utf-8') as file2:
            file2.write(str(soup1))
        # Proposal=soup1.find("table",{"id": "simpleDetailsTable"}).find('tr')[6].find('td')[1].get_text(strip=True)
        Proposal = soup1.find("table", {"id": "simpleDetailsTable"}).find_all('tr')[5].find_all('td')[0].get_text(strip=True)
        print(Proposal)
        counter1=counter1+1

# scraping(soup)

l1 = []
counter=1
while True:

    if counter==1:
        scraping(soup,counter)
        url = getnextpage(soup)
    else:
        data = getdata(url)
        with open(r"C:\Users\Jayendra\Desktop\Pyt\Scrap" + str(counter) + ".html", "w", encoding='utf-8') as file1:
            file1.write(str(data))
        scraping(data,counter)
        url = getnextpage(data)

    if not url:
        break
    print(url)

    counter=counter+1

#
# conn = sqlite3.connect(r"C:\Users\Jayendra\Desktop\Pyt\example.db")
# c = conn.cursor()
# c.execute('''CREATE TABLE stocks
#                  (URl TEXT, trans TEXT)''')
# c.executemany('INSERT INTO stocks VALUES (?,?)', l1)
# conn.commit()
# conn.close()