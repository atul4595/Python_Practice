import urllib.request
import urllib.parse
# url="https://pythonprogramming.net/search/"
# headers={}
# headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
# values={'s':'basic'}
# data=urllib.parse.urlencode(values)
# data=data.encode('utf-8')
# req=urllib.request.Request(url,data,headers=headers)
# print(req.data)
# resp=urllib.request.urlopen(req)
# respData=resp.read()
# print(respData)


url='https://www.google.com/search?q=test'
headers={}
headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
req=urllib.request.Request(url,headers=headers)
resp=urllib.request.urlopen(req)
respdata=resp.read()
print(respdata)
# print(x.read())