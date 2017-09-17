# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    url = scrapy.Field()
    # Clean url without tracking codes
    clean_url = scrapy.Field()
    domain = scrapy.Field()
    company = scrapy.Field()
    company_url = scrapy.Field()
    company_url_chooseyourboss = scrapy.Field()
    title = scrapy.Field()
    location = scrapy.Field()
    type = scrapy.Field()
    role = scrapy.Field()
    tags = scrapy.Field()
    #start_date = scrapy.Field()
    #education = scrapy.Field()
    description_html = scrapy.Field()
    description_job = scrapy.Field()
    description_profile = scrapy.Field()
    description_company = scrapy.Field()
    experience = scrapy.Field()
    education = scrapy.Field()
    salary = scrapy.Field()
