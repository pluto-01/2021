import requests
url='https://item.jd.com/100008705025.html'
try:
    r = requests.get(url)
    r.raise_for_status()
    r.encoding='utf-8'
    '''
    r.encoding = r.apparent_encoding
    '''
    print(r.text)
    
except:
    print('爬取失败')
