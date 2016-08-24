from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_it_later(self):
# Edith has heard about a cool new online to-do app. She goes
# to check out its homepage
        self.browser.get(self.server_url)
# She notices the page title and header mention to-do lists
        self.assertIn('360Studying', self.browser.title)
