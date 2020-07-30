# -*- coding: utf-8 -*-
import scrapy
from ..items import MyjobspiderItem

class JobspidersSpider(scrapy.Spider):
    name = 'jobspiders'
    # allowed_domains = ['www.51job.com']
    # 指定需要爬取的网站网页，AJAX
    # start_urls = ['https://search.51job.com/list/010000,000000,0000,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='] # 访问的URL

    def __init__(self,start_url,jobType,*args,**kw):
        super(JobspidersSpider,self).__init__(*args,kw)
        self.start_urls.append(start_url)
        self.jobType=jobType

    def parse(self, response):
        jobItems = response.xpath("//div[@class='el']") # 返回的是选择器列表
        # 采集下一页
        # 如何进入下一页，需要分析网站实现分页的机制 多数分页是使用a
        nextURL = ''
        count = 0  # 保序
        nextPageURL = response.xpath("//li[@class='bk']/a[contains(text(),'下一页')]/@href")
        if nextPageURL:
            nextURL = nextPageURL.extract()[0]

        pageTotals = len(jobItems)
        for jobItem in jobItems:
            count += 1
            myJobItem = MyjobspiderItem()
            myJobItem['jobType']=self.jobType
            # 职位工作
            jobName = jobItem.xpath("./p/span/a/text()") # jobItem -- div class='el'
            jobCompany = jobItem.xpath("./span[@class='t2']/a/text()")
            jobAdress = jobItem.xpath("./span[@class='t3']/text()")
            jobSalary = jobItem.xpath("./span[@class='t4']/text()")
            jobDate = jobItem.xpath("./span[@class='t5']/text()")
            jobURL = jobItem.xpath('./p/span/a/@href')
            # 自己取出其他的信息： C+V大法
            if jobName and jobCompany and jobAdress and jobSalary and jobDate and jobURL: # 可以过滤掉异常数据
                myJobItem['jobName'] = jobName.extract()[0].strip()
                myJobItem['jobURL'] = jobURL.extract()[0].strip()
                myJobItem['jobCompany'] = jobCompany.extract()[0].strip()
                myJobItem['jobAdress'] = jobAdress.extract()[0].strip()
                myJobItem['jobSalary'] = jobSalary.extract()[0].strip()
                myJobItem['jobDate'] = jobDate.extract()[0].strip()
                level2URL = jobURL.extract()[0].strip()

                yield scrapy.Request(url=level2URL, callback=self.parseLevel2, dont_filter=False,
                               meta={'nextURL': nextURL, 'pageTotals':pageTotals, 'count': count, 'myJobItem':myJobItem})
            if pageTotals==count and nextPageURL:
                yield scrapy.Request(url=nextURL, callback=self.parse, dont_filter=False)

            pass

        pass


    def parseLevel2(self, response):
        nextURL = response.meta['nextURL']
        pageTotals = response.meta['pageTotals']
        myJobItem =  response.meta['myJobItem']
        count = response.meta['count']

        # 编写二级页面内容提取的规则
        content1 = response.xpath("//div[@class='cn']/p[@class='msg ltype']")
        content2 = response.xpath("//div[@class='cn']/div[@class='jtag']/div[@class='t1']")
        content3 = response.xpath("//div[@class='bmsg job_msg inbox']")
        if content1 and content2 and content3:
            content=""
            for i in content1.extract():
                content+=i
            for i in content2.extract():
                content += i
            for i in content3.extract():
                content += i
            myJobItem['jobContext'] = content
            print(content)
            yield myJobItem   # 向管道输出数据
            pass
        else:
            print('wu')
        # 采集完成二级页面之后才采集下一页
        # if nextURL and count == pageTotals:
        #     print(nextURL)
        #     yield scrapy.Request(url=nextURL, callback=self.parse, dont_filter=False)
        #     pass
        # pass
