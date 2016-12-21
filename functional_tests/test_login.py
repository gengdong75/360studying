from .base import FunctionalTest

class LoginTest(FunctionalTest):

    def test_login_with_persona(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_login').click()

        self.switch_to_new_window('Mozilla Persona')

        self.browser.find_element_by_id('authentication_email').send_keys('edith@mockmyid.com')
        self.browser.find_element_by_tag_name('button').click()

        self.switch_to_new_window('360Studying')

        self.wait_for_element_with_id('id_logout')
        navbar = self.browser.find_element_by_css_selector('.navbar')
        self.assertIn('edit@mockmyid.com',navbar.text)


