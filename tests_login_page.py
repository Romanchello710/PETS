import time

import pytest
import requests

# в тесте обращаемся к логике

from pages.login_page import LoginPage


def test_login(browser):
    link = "http://34.141.58.52:8080/#/login"
    browser.get(link)
    page = LoginPage(browser,link)
    page.go_to_login()
    time.sleep(3)
    page.go_to_password()
    time.sleep(3)
    page.go_to_submit()
    time.sleep(3)
    page.go_to_pets()
    time.sleep(3)
    page.go_to_name()
    time.sleep(3)
    page.go_to_age()
    time.sleep(3)
    page.go_to_type()
    time.sleep(3)
    page.click_type()
    time.sleep(3)
    page.go_to_gender()
    time.sleep(3)
    page.click_gender()
    time.sleep(3)
    page.click_submit()
    time.sleep(3)

