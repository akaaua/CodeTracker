from selenium import webdriver
from time import sleep
from util.definevariables import defineusername
from util.definevariables import definepassword
from util.definevariables import definerepository
import datetime as dt
import os
from sqlite_functions import _create_database, _insert_project, _insert_date, _get_projectid, _get_projects



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
        _create_database()
        sleep(1)


    def _select_project(self):
        
        project = definerepository()
        self.driver.find_element_by_xpath('//*[@title="' + project + '"]').click()
        
        if _get_projects(project) == None:
           result = _insert_project(project)
           print(result)
        elif _get_projects(project)[0] != project:
           result = _insert_project(project)
           print(result)
        else:   
            print('Projeto existente')
        
        print(project)
        return project
        


    def _get_datetime(self):
        
        dates = self.driver.find_elements_by_tag_name('time-ago')
        datetime_commit = [dates[i].get_attribute('datetime') for i in range(len(dates))]
        print(datetime_commit)
        return datetime_commit
    
    def _datetime_converter(self, datetime_commit):

        dates_list = [dt.datetime.strptime(date, '%Y-%m-%dT%H:%M:%SZ').date() for date in datetime_commit]
        date_formatted = [dt.datetime.strptime(str(i), '%Y-%m-%d').strftime('%d-%m-%Y') for i in dates_list]
        datetime_type = [dt.datetime.strptime(date, '%d-%m-%Y').date() for date in date_formatted]
        projectdb = int(_get_projectid(project)[0])
        for i in range(len(datetime_type)):
            _insert_date(datetime_type[i].day, datetime_type[i].month, datetime_type[i].year, projectdb)
        print(date_formatted)
        print(datetime_type)
        return datetime_type




my_bot = GitBot()
project = my_bot._select_project()
datetime_commit = my_bot._get_datetime()
my_bot._datetime_converter(datetime_commit)
