from selenium import webdriver
from time import sleep
from secrets import pw
from secrets import username
from datetime import datetime
import os

class GitBot:

    def __init__(self, username, pw):
        #Tentativa de usar caminho relativo no webdriver para evitar futuros problemas.
        #path = "util/chromedriver" 
        #relpath = os.path.relpath("/home/akaua/Documentos/CodeProjects/CodeTracker/util/chromedriver")
        self.username = username
        self.driver = webdriver.Chrome("/home/akaua/Documentos/CodeProjects/CodeTracker/util/chromedriver")
        self.driver.get("https://github.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(pw)
        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
        sleep(1)


    def _select_project(self):
        
        self.driver.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/ul/li[1]/div/a/span[1]').click()


    def _get_datetime(self):
        
        dates = self.driver.find_elements_by_tag_name('time-ago')
        datetime_commit = [dates[i].get_attribute('datetime') for i in range(len(dates))]
        return datetime_commit
    
    def _datetime_converter(self):

        datetime_converted = datetime.strptime(datetime, '%d/%m/%y %H:%M:%S')
        print(datetime_converted)
        return datetime_converted



#sleep(120)


my_bot = GitBot(username, pw)

my_bot._select_project()
my_bot._get_datetime()

