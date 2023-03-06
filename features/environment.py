from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def before_all(context):
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    context.browser = webdriver.Firefox(executable_path=r'C:\users\alaunoy\Documents\python-tdd-book\geckodriver.exe', options=options)

def after_all(context):
    context.browser.quit()

def before_feature(context, feature):
    pass