#System imports
import pathlib 
import logging
import array
import os
import csv
from tkinter import filedialog

#Scrapy Imports
import scrapy 
from scrapy.crawler import CrawlerProcess
from scrapy.http import Request
from scrapy.utils.project import get_project_settings

#tkinter import for GUI
from tkinter import *

class ulinespider(scrapy.Spider):
    global ulineaddress
    global boxpartneraddress
    name = "spideruline"

    def __init__(self, output, start_urls):
            self.output = output  # output file name
            self.start_urls = start_urls
    
    def parse(self, response):
        for model in response.xpath('//*[@id="tblChartBody"]/tbody/tr[*]/td[*]/*/*/text()'):
            print(model)
        for link in response.xpath('//*[@id="tblChartBody"]/tbody/tr[*]/td[*]/*/*/@href'):
            print(link)
        print(self.output)


#Function definition for input file browser
def browseFilesInput():

    #init variables for urls
    global ulineurl
    global boxpartnerurl
    global start_url_list
    inputfilename = filedialog.askopenfilename(initialdir = "/",
                                               title= "Select a file")
    # Change label contents
    label_file_explorer_input.configure(text="File Opened: "+inputfilename)
    with open(inputfilename, newline='') as inputcsvfile:
        inputreader = csv.reader(inputcsvfile, delimiter=',', quotechar='|')
        step = 0
        for row in inputreader:
            if step == 0:
                ulineurl = row[1]
                step += 1
                start_url_list = ulineurl # + ',' + boxpartnerurl
                print(start_url_list)
            if step == 1:
                boxpartnerurl = row[1]
                


#Function definition for output file browser
def browseFilesOutput():
    global outputfilename
    outputfilename = filedialog.askopenfilename(initialdir = "/",
                                               title= "Select a file")
    # Change label contents
    label_file_explorer_output.configure(text="File Opened: "+outputfilename)

# Function definition for scrape button
def scrape():
    process = CrawlerProcess(
        settings={
            "BOT_NAME": "ULineSpider",
            #"SPIDER_MODULES": "['ULineSpider.spiders']",
            "NEWSPIDER_MODULE": "ULineSpider.spiders",
            "ROBOTSTXT_OBEY": "false",
            "CONCURRENT_REQUESTS": "6",
            "REQUEST_FINGERPRINTER_IMPLEMENTATION": "2.7",
            "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
            "FEED_EXPORT_ENCODING": "utf-8",
            #"start_urls" : start_url_list
            })
    process.crawl(ulinespider, output=outputfilename, start_urls=[
        start_url_list
    ])
    process.start()

# Create the root window
window = Tk()

# Set window title
window.title('ULine Data Scraper')

# set window size
window.geometry("500x500")

# set window bg color
window.config(background = "white")

# Create a File Explorer label for choosing input
label_file_explorer_input = Label(window, 
                            text = "Select input csv file containing url's",
                            width = 100, height = 4, 
                            fg = "blue")
  
      
button_input_explore = Button(window, 
                        text = "Choose Input",
                        command = browseFilesInput) 

# Create a File Explorer label for choosing output
label_file_explorer_output = Label(window,
                            text = "Select output csv file for scraped data",
                            width = 100, height = 4, 
                            fg = "blue")
  
      
button_output_explore = Button(window, 
                        text = "Choose Output",
                        command = browseFilesOutput) 

# Exit button
button_exit = Button(window,
                     text="Exit",
                     command= exit)
  
# Scrape button
button_scrape = Button(window, 
                     text = "Scrape",
                     command = scrape) 

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer_input.grid(column = 1, row = 1)
  
button_input_explore.grid(column = 1, row = 2)

label_file_explorer_output.grid(column = 1, row = 3)
  
button_output_explore.grid(column = 1, row = 4)

button_scrape.grid(column = 1, row = 5)

button_exit.grid(column = 1,row = 6)
  
# Let the window wait for any events
window.mainloop()