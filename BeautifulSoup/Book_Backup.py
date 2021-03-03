import requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}

login_data = {
    'name': 'atul4598',
    'pass': '@Tul1989',
    'form_id': 'new_login_form',
    'op': 'Login'
}

with requests.Session() as s:
    url = 'https://www.codechef.com/'
    r = s.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html5lib')
    with open(r"C:\Users\Jayendra\Desktop\Scrap\Scrap.html", "w", encoding='utf-8') as file1:
        file1.write(str(soup))
    login_data['csrfToken'] = soup.find('input', attrs={'name': 'csrfToken'})['value']
    login_data['form_build_id'] = soup.find('input', attrs={'name': 'form_build_id'})['value']
    r2 = s.post(url, data=login_data, headers=headers)
    # print(r2.content)
    soup2 = BeautifulSoup(r2.content, 'html5lib')
    with open(r"C:\Users\Jayendra\Desktop\Scrap\Scrap1.html", "w", encoding='utf-8') as file2:
        file2.write(str(soup2))

