import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class capstone(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/home/pavan/Desktop/chromedriver")

    def test_url(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_link_text('Login Here!').click()
        self.assertTrue(self.driver.find_element_by_css_selector('#contact-section > div > div.row.justify-content-center > div > form > div:nth-child(2) > div > input'))
    

    def test_login(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.driver.find_element_by_link_text('Login Here!').click()
        self.driver.find_element_by_name('email').send_keys('kalyan@gmail.com')
        self.driver.find_element_by_name('password').send_keys('9542519889')
        self.driver.find_element_by_xpath('//*[@id="contact-section"]/div/div[2]/div/form/div[2]/div/input').click()
        self.assertTrue(self.driver.find_elements_by_css_selector('#sticky-wrapper > header > div > div > div.col-12.col-md-10.d-none.d-xl-block > nav > ul > li > a'))




    

        



if __name__ == "__main__":
    unittest.main()
    

    
     













    