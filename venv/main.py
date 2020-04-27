from selenium import webdriver
from time import sleep
from secrets import pw
from secrets import username
from datetime import datetime
import os

class GitBot:

    def __init__(self, username, pw):        
        self.username = username
        self.driver = webdriver.Chrome(os.path.abspath(os.getcwd())+"/util/chromedriver")
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
        #repo = '' #for test purposes define here.
        if repo == '':
            print('Qual o nome do repositório?')
            repo = input()
        self.driver.find_element_by_xpath('//*[@title="' + repo + '"]').click()     

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

