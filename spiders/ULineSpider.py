#Simple Spider to Scrape ULine site for pricing. Takes a csv of URL's as input, outputs a csv of needed data.

#System imports
import pathlib 
import logging
import array
import os
import csv
from tkinter import filedialog

#Scrapy imports for spider
import scrapy 
from scrapy.http import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
logging.getLogger('scrapy').setLevel(logging.WARNING)

class ulinespider(scrapy.Spider):
    global ulineaddress
    global boxpartneraddress
    name = "spideruline"
    #Init to get params from mainprogram
    #def __init__(self, output = None, uline= None, boxpartner=None):
    def __init__(self, output = None):
            self.output = output  # output file name
            #ulineaddress = uline
            #boxpartneraddress = boxpartner
    
    # starting urls
    #start_urls = [
    #    ulineaddress
    #]
    
    def parse(self, response):
        for link in response.xpath('//*[@id="tblChartBody"]/tbody/tr[1]/td[1]/div/span/a'):
            print(link)
