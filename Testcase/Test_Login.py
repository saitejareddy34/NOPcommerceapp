import pytest
from selenium import webdriver
from pageobjects.loginpage import LoginPage
from utilities.readproperties import ReadConfig

class Test_001_Login:

    baseURL = ReadConfig.getApplicationURL
    username = ReadConfig.getUseremail
    password = ReadConfig.getpassword

    def test_homepageTitle(self,setup):
       self.driver= setup
       self.driver.get(self.baseURL)
       act_title=self.driver.title
       if act_title == "Your store. Login123":
            assert True
            self.driver.close()
       else:
           self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
           assert False

    def test_login(self,setup):
        self.driver= setup
        self.driver.get(self.baseURL)
        self.lp= LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setpassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title
        self.driver.close()