import requests

iurl = 'http://search.hebcz.cn:8080/was5/web/search?fstarttime=&fendtime=2023-01-18&searchword1=%E5%BA%94%E6%80%A5&channelid=218195&searchword=&sydoctitle=&lanmu=zfcgyx&city=sjz'
headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)'}

res = requests.get(url=iurl, headers=headers)
res.encoding = 'utf-8'
html = res.text




with open(r'ipage.html', 'w') as f:
    f.write(html)
    f.close()