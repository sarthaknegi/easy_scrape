from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
import requests
import time
from . import body_data

class scrape_table(object):

    def __init__(self, path):
        try:
            headless = webdriver.ChromeOptions()
            headless.add_argument('--headless')
            headless.add_argument('--disable-gpu')
            self.headless_browser = webdriver.Chrome(path, options=headless)
        except Exception as e:
            print(e)

    def table(self,url=None, class_name=None, id_name=None, div = None):
        """

        :param url: URL for the desired webpage where table exists
        :param class_name: table tags class name
        :param id_name: if class name is not available, then id name
        :param div: a {key,value} pari where key defines the class or id keyword and value defines the class or id name. This should be used only if the given table tag does not have any class
        :return dataframe

        """
        headers_list = []
        #flag = 0
        #Put testing code here
        self.headless_browser.get(url)
        time.sleep(3)
        source_data = self.headless_browser.page_source
        pretty_source_data = BeautifulSoup(source_data, "lxml")

        if class_name:
            key	= 'class'
            value = class_name
            pretty_table = pretty_source_data.find_all('table', attrs={key: value})
        elif id_name:
            key	= 'id'
            value = id_name
            pretty_table = pretty_source_data.find_all('table', attrs={key: value})
        elif div:
            key = list(div.keys())[0]
            value = list(div.values())[0]
            pretty_div = pretty_source_data.find_all('div', attrs={key: value})
            if len(pretty_div) > 1:
                choice = int(input('I found {} Divs !! Which one are you looking for. Enter the div number: '.format(len(pretty_div))))
                pretty_table = pretty_div[choice - 1].find_all('table')
                pretty_table = pretty_source_data.find_all('table', attrs={key : value})

        if len(pretty_table) > 1:
            choice = int(input('I found {} tables!! Which one are you looking for. Enter the table number: '.format(len(pretty_table))))
            choice -= 1
        else:
            choice = 0

        thead_tag = pretty_table[choice].find_all('thead')

        if thead_tag: #assumption is that only one header tags exist in a single table
            for th in thead_tag[0].find_all('th'):
                headers_list.append(th.text)
            main_dataframe = pd.DataFrame(columns=headers_list)
            main_dataframe = body_data.tbody_data(pretty_table, main_dataframe, 0, choice)

        else:
            main_dataframe = pd.DataFrame()
            main_dataframe = body_data.tbody_data(pretty_table, main_dataframe, 1, choice)

        return main_dataframe
#
# if __name__ == '__main__':
#     obj = easy_scrape(r'C:/Users/sarthak_negi_/Downloads/chromedriver_win32/chromedriver.exe')
#     df = obj.table(url = 'https://en.wikipedia.org/wiki/List_of_NBA_champions', class_name = 'wikitable sortable jquery-tablesorter')
#     print(df)
