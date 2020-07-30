# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .dao.jobdao import JobDao

class MyjobspiderPipeline(object):
    def process_item(self, item, spider):
        # 提取的数据，输出到管道，然后加工处理，并且写入MySQL数据库
        print(item['jobName'], end="\t")
        print(item['jobCompany'], end="\t")
        print(item['jobAdress'], end="\t")
        print(item['jobSalary'], end="\t")
        print(item['jobDate'], end="\t")
        print(item['jobURL'], end="\t")
        print(item['jobContext'])
        jobCity=""
        jobAddress=item['jobAdress']
        if jobAddress.find('-')!=-1:
            jobCity=jobAddress.split('-')[0]
        else:
            jobCity=jobAddress

        minSalary=0
        maxSalary=0
        meanSalary=0
        salary=item['jobSalary']
        if salary.find('万/月')!=-1:
            salary=salary.split('万/月')[0]
            if salary.find('-'):
                salaryArray=salary.split('-')
                minSalary=float(salaryArray[0])*10000
                maxSalary=float(salaryArray[1])*10000
            else:
                minSalary=maxSalary=float(salary)
            meanSalary=(minSalary+maxSalary)/2

        if salary.find('元/天')!=-1:
            salary=salary.split('元/天')[0]
            if salary.find('-'):
                salaryArray=salary.split('-')
                minSalary=float(salaryArray[0])*22
                maxSalary=float(salaryArray[1])*22
            else:
                minSalary=maxSalary=float(salary)
            meanSalary=(minSalary+maxSalary)/2

        if salary.find('万/年')!=-1:
            salary=salary.split('万/年')[0]
            if salary.find('-'):
                salaryArray=salary.split('-')
                minSalary=float(salaryArray[0])*10000/12
                maxSalary=float(salaryArray[1])*10000/12
            else:
                minSalary=maxSalary=float(salary)
            meanSalary=(minSalary+maxSalary)/2

        if salary.find('千/月') != -1:
            salary = salary.split('千/月')[0]
            if salary.find('-'):
                salaryArray = salary.split('-')
                print(salaryArray)
                minSalary = float(salaryArray[0]) * 1000
                maxSalary = float(salaryArray[1]) * 1000
            else:
                minSalary = maxSalary = float(salary)
            meanSalary = (minSalary + maxSalary) / 2

        # 定义dao
        jobdao=JobDao()
        result=jobdao.createJobInfo(params=[item['jobType'],item['jobName'],item['jobCompany'],
                                     item['jobAdress'],item['jobSalary'],item['jobDate'],
                                     item['jobURL'],item['jobContext'],jobCity,minSalary,maxSalary,meanSalary])
        if result>0:
            print("输入成功")
        return item
