from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest

MAX_WAIT = 10

class LayoutAndStylingTest(FunctionalTest):
        
        def test_layout_and_styling(self):
            self.browser.get(self.live_server_url)
            self.browser.set_window_size(1024, 768)

            inputbox = self.get_item_input_box()
            self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
            )

            self.add_list_item('testing')
            self.wait_for_row_in_list_table('1: testing')
            inputbox = self.get_item_input_box()
            self.assertAlmostEqual(
                inputbox.location['x'] + inputbox.size['width'] / 2,
                512,
                delta=10
            )

