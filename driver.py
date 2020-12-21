import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
driver.get("http://127.0.0.1:8000/")


def test_url(self):
        self.driver.get("http://127.0.0.1:8000/")
        self.assertTrue(self.driver.find_element_by_link_text('Contact'))