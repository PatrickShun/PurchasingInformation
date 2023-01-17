import os
from lxml import etree
from datetime import datetime
import requests
import configparser
import random
import EditExcel



class PurchasingInfo:

    def __init__(self):
        self.timeNow = datetime.now()
        self.timeNow = '20' + self.timeNow.strftime('%y-%m-%d')
        CONFIG_FILE = os.path.join(os.getcwd(), 'change.ini')
        self.conf = configparser.ConfigParser()
        self.conf.read(CONFIG_FILE, encoding='utf-8')
        self.baseURL = self.conf['baseURL']['demoURL']
        self.cityName = []
        self.home_links = []
        self.release_date = []
        self.page_title = []
        self.publisher = []
        print(self.timeNow)


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


    def getHTML(self,icity):
        fendtime = self.timeNow
        searchWord = '应急'
        city = icity
        runURL = 'http://search.hebcz.cn:8080/was5/web/search?fstarttime=&fendtime={}&searchword1={}&' \
                 'channelid=218195&searchword=&sydoctitle=&lanmu=zfcgyx&city={}'.format(fendtime, searchWord, city)
        headers = {'User-Agent':self.randomHeader()}
        res = requests.get(runURL, headers=headers)
        res.encoding = 'utf-8'
        html = res.text
        # f = open('myFile.html', 'r')  # 离线debug
        # html = f.read()               # 离线debug
        print(res.url)
        return html


    def getHomeLinks(self, html):
        parseHtml = etree.HTML(html)
        self.home_links = parseHtml.xpath(self.conf['position']['HomeLinks'])
        self.release_date = parseHtml.xpath(self.conf['position']['ReleaseDate'])
        self.page_title = parseHtml.xpath(self.conf['position']['PageTitle'])
        self.publisher = parseHtml.xpath(self.conf['position']['Publisher'])


    def writeData(self,icity):
        print(len(self.home_links))
        print(len(self.release_date))
        print(len(self.page_title))
        print(len(self.publisher))
        if len(self.home_links) == len(self.page_title):
            wb = EditExcel.runExcel(icity)
            wb.writeExcel(self.cityName, 1)
            wb.writeExcel(self.release_date, 2)
            wb.writeExcel(self.page_title, 3)
            wb.writeExcel(self.publisher, 4)
            wb.writeExcel(self.home_links, 5)


    def irun(self):
        # 1.获取主页的第一页的所有子URL，也就是50个详细URL；
        self.getHomeLinks(self.getHTML('ts'))

        # 2.判断获取到的四个元素都完整，就可以准备写入excel；
        self.writeData('ts')





if __name__ == "__main__":
    running = PurchasingInfo()
    running.irun()

