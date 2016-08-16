from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_firstPage(self):
        #打开首页
        self.browser.get(self.live_server_url)
        self.assertIn('360Studying',self.browser.title)
        self.fail("finish the test!")
