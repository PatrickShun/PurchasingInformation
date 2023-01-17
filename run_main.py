import os
import requests
import configparser
import random
from lxml import etree


class PurchasingInfo:

    def __init__(self):
        CONFIG_FILE = os.path.join(os.getcwd(), 'change.ini')
        self.conf = configparser.ConfigParser()
        self.conf.read(CONFIG_FILE, encoding='utf-8')
        self.baseURL = self.conf['baseURL']['Hebei_zfcgyx']


    def randomHeader(self):
        headerList = [
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
            'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
            'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
            'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'
        ]
        RHeader = random.choice(headerList)
        return RHeader

    def getPage(self,baseurl):
        print(baseurl)
        # headers = {'User-Agent':self.randomHeader()}
        # res = requests.get(baseurl,headers=headers)
        # res.encoding = 'utf-8'
        # html = res.text
        f = open('myFile.html', 'r')  # 离线debug
        html = f.read()               # 离线debug
        parseHTML = etree.HTML(html)
        result = parseHTML.xpath('//*[@id="moredingannctable"]/tr/td[2]/a/@href')
        for i in result:
            print(i)


    def getHomeLinks(self, html):
        parseHtml = etree.HTML(html)
        print(self.conf['position']['HomeLinks'])
        homeLinks = parseHtml.xpath(self.conf['position']['HomeLinks'])
        return homeLinks


    def irun(self):
        self.getPage(self.conf['baseURL']['Hebei_zfcgyx'])



if __name__ == "__main__":
    running = PurchasingInfo()
    running.irun()

