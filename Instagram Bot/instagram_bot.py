from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
import xlrd




class InstagramBot:
    # initializing
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()
        self.base_url = "https://www.instagram.com"
        self.login()
     #login function
    def login(self):
        self.driver.get("{}/accounts/login".format(self.base_url))
        self.driver.implicitly_wait(10)
        login_element = self.driver.find_element_by_name("username").send_keys(self.username)
        password_element = self.driver.find_element_by_name("password").send_keys(self.password)
        button_element = self.driver.find_element_by_xpath("//div[contains(text(),'Log In')]").click()
        time.sleep(2)
        
     #go to specific profile
    def nav_user(self,user):
        self.driver.get('{}/{}/'.format(self.base_url,user))
        
        
     #follow specific user
    def follow_user(self,user):
        self.nav_user(user)
        follow_element = self.driver.find_element_by_xpath("//button[contains(text(),'Follow')]").click()
        
    #follow suggested user list
    def follow_suggested_user(self):
        self.driver.get('{}/explore/people/suggested/'.format(self.base_url))
        follow_element = self.driver.find_elements_by_xpath("//button[contains(text(),'Follow')]")
        for x in follow_element:
            self.driver.implicitly_wait(5)
            x.click()



if __name__ == '__main__':
    loc = (r"absolute_path")
    wb = xlrd.open_workbook(loc)
    sheet = wb.sheet_by_index(0)
    ig_bot = InstagramBot('your_username','your_password')
    time.sleep(1)

    ig_bot.nav_user("your_username")
    
    for i in range(sheet.nrows):
        ig_bot.follow_user(sheet.cell_value(i, 0))

    ig_bot.follow_suggested_user()
