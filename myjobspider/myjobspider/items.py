# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

# 管道数据封装实体类 定义数据键
class MyjobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    jobURL = scrapy.Field()
    jobCompany = scrapy.Field()
    jobAdress = scrapy.Field()
    jobSalary = scrapy.Field()
    jobDate = scrapy.Field()
    jobContext = scrapy.Field()
    jobType = scrapy.Field()
    pass
