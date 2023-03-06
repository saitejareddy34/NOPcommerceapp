import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage

class Test_001_Login:

    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"

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