from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.common.exceptions import WebDriverException
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY
from django.contrib.sessions.backends.db import SessionStore
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

MAX_WAIT = 10

def wait(fn):
    def modified_fn(*args, **kwargs):
        start_time = time.time()
        while True:
            try:
                return fn(*args, **kwargs)
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)
    return modified_fn

class FunctionalTest(StaticLiveServerTestCase):
    
    def setUp(self):
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            self.browser = webdriver.Firefox(executable_path=r'C:\users\alaunoy\Documents\python-tdd-book\geckodriver.exe', options=options)
            #staging_server = os.environ.get('STAGING_SERVER')
            #if staging_server:
            #    self.live_server_url = 'http://' + staging_server
    
    def tearDown(self):
        self.browser.quit()

    def get_item_input_box(self):
        return self.browser.find_element_by_id('id_text')

    @wait
    def wait_for(self, fn):
        return fn()

    @wait
    def wait_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    
    @wait
    def wait_to_be_logged_in(self, email):
        lambda: self.browser.find_element_by_link_text('Log out')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn(email, navbar.text)

    @wait
    def wait_to_be_logged_out(self, email):
        lambda: self.browser.find_element_by_name('email')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertNotIn(email, navbar.text)
    
    def add_list_item(self, item_text):
        num_rows = len(self.browser.find_elements_by_css_selector('#id_list_table tr'))
        self.get_item_input_box().send_keys(item_text)
        self.get_item_input_box().send_keys(Keys.ENTER)
        item_number = num_rows + 1
        self.wait_for_row_in_list_table(f'{item_number}: {item_text}')
    
    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY]=user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()

        self.browser.get(self.live_server_url + '/404_no_such_url/')
        self.browser.add_cookie(dict(
            name=settings.SESSION_COOKIE_NAME,
            value=session.session_key,
            path='/'
        ))