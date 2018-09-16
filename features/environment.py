from selenium import webdriver
from features.pages.sign_up_page import Locators

def before_all(context):
    context.locators = Locators()
    context.browser = webdriver.Chrome()
    context.browser.set_page_load_timeout(10)
    context.browser.implicitly_wait(10)
    
def after_all(context):
    context.browser.quit()