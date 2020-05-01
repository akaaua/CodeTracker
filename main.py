from selenium import webdriver
from time import sleep
from util.definevariables import defineusername
from util.definevariables import definepassword
from util.definevariables import definerepository
import datetime as dt
import os


class GitBot:

    def __init__(self):
                
        self.driver = webdriver.Chrome(os.path.abspath(os.getcwd())+"/util/chromedriver")
        self.driver.get("https://github.com/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(1)
        self.driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
        self.driver.implicitly_wait(1)        
        self.driver.find_element_by_xpath('//*[@id="login_field"]').send_keys(defineusername())
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(definepassword())
        self.driver.find_element_by_xpath('//*[@id="login"]/form/div[4]/input[9]').click()
        sleep(1)


    def _select_project(self):
        
        self.driver.find_element_by_xpath('//*[@title="' + definerepository() + '"]').click()     

    def _get_datetime(self):
        
        dates = self.driver.find_elements_by_tag_name('time-ago')
        datetime_commit = [dates[i].get_attribute('datetime') for i in range(len(dates))]
        print(datetime_commit)
        return datetime_commit
    
    def _datetime_converter(self, datetime_commit):

        dates_list = [dt.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').date() for date in datetime_commit]
        date_formatted = [dt.datetime.strptime(str(i), '%Y-%m-%d').strftime('%d-%m-%Y') for i in dates_list]
        print(date_formatted)
        return date_formatted




my_bot = GitBot()
my_bot._select_project()
datetime_commit = my_bot._get_datetime()
my_bot._datetime_converter(datetime_commit)

