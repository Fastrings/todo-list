from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
        self.browser = webdriver.Firefox(executable_path=r'C:\users\alaunoy\Documents\python-tdd-book\geckodriver.exe', options=options)
    
    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        self.fail('Finish the Test !')

if __name__ == '__main__':
    unittest.main()