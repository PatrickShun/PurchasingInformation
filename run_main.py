import os
from time import sleep
from lxml import etree
from datetime import datetime
import requests
import configparser
import random
import EditExcel
import json


class PurchasingInfo:

    def __init__(self):
        self.timeNow = datetime.now()
        self.timeNow = '20' + self.timeNow.strftime('%y-%m-%d')
        CONFIG_FILE = os.path.join(os.getcwd(), 'change.ini')
        self.conf = configparser.ConfigParser()
        self.conf.read(CONFIG_FILE, encoding='utf-8')
        self.baseURL = self.conf['baseURL']['demoURL']
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


    def getHTML(self,cityCode):
        fendtime = self.timeNow
        searchWord = '应急'
        # runURL = 'http://search.hebcz.cn:8080/was5/web/search?fstarttime=&fendtime={}&searchword1={}&' \
        #          'channelid=218195&searchword=&sydoctitle=&lanmu=zfcgyx&city={}'.format(fendtime, searchWord, cityCode)
        # headers = {'User-Agent':self.randomHeader()}
        # res = requests.get(runURL, headers=headers)
        # res.encoding = 'utf-8'
        # html = res.text
        f = open('ipage.html', 'r')  # 离线debug
        html = f.read()               # 离线debug
        # print(res.url)
        return html


    def getHomeLinks(self, html):
        parseHtml = etree.HTML(html)
        self.cityName, self.home_links, self.release_date, self.page_title, self.publisher = [],[],[],[],[]
        self.home_links = parseHtml.xpath(self.conf['position']['HomeLinks'])
        self.release_date = parseHtml.xpath(self.conf['position']['ReleaseDate'])
        self.page_title = parseHtml.xpath(self.conf['position']['PageTitle'])
        self.publisher = parseHtml.xpath(self.conf['position']['Publisher'])


    def writeData(self,cityName):
        [self.cityName.append(cityName) for cy in range(len(self.page_title))]
        if len(self.home_links) == len(self.page_title):
            wb = EditExcel.runExcel(cityName)
            wb.writeExcel(self.cityName, 1)
            print("25%...")
            wb.writeExcel(self.release_date, 2)
            print("50%...")
            wb.writeExcel(self.page_title, 3)
            print("75%...")
            wb.writeExcel(self.publisher, 4)
            print("99%...")
            wb.writeExcel(self.home_links, 5)
            print('100%...')

    def readData(self,cityName,col):
        wb_r = EditExcel.runExcel(cityName)
        dataList = []
        [dataList.append(i.value) for i in wb_r.readExcel(col)]
        return dataList





    def irun(self):
        # 1.获取json的所有城市;
        # with open('cityName.json','r') as load_js:
        #     self.load_dict = json.load(load_js)

        # 2.遍历字典中的所有城市；
        # for cityName in self.load_dict.keys():
        #     print('-' * 20)
        #     print(cityName + '...')

            # 3.Get页面之前需要保存历史数据（当前get的城市）
        rawData_time = set(self.readData('石家庄','B'))
        rawData_title = set(self.readData('石家庄','C'))

            # 4.获取主页的第一页的所有子URL，也就是50个详细URL结果；
            # self.getHomeLinks(self.getHTML(self.load_dict[cityName]))
        self.getHomeLinks(self.getHTML('石家庄'))

            # 5.使用历史数据与最新数据作并集（|），并集后保存到需要写入的列表中；

            # 6.使用历史数据与最新数据作求差值（-），用于提醒与标记新增的内容；

            # 7.判断获取到的四个元素都完整，就可以准备写入excel；
            # self.writeData(cityName)

            # 8.针对新增内容执行提醒与标记；

        print(rawData_time)
        print(rawData_title)
        l1 = set(self.release_date)
        print(l1)
        # l1 = rawData_time - rawData_title





        print("Done!")




if __name__ == "__main__":
    running = PurchasingInfo()
    running.irun()

