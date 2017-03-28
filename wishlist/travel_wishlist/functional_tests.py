import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from django.test import LiveServerTestCase
class HomePageTest(LiveServerTestCase):
    fixtures = ['test_places']
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)


    def tearDown(self):
        self.browser.quit()


    def test_get_home_page_list_of_places(self):
        self.browser.get(self.live_server_url)

        assert 'Tokyo' in self.browser.page_source
        assert 'New York' in self.browser.page_source
        assert 'San Francisco' in self.browser.page_source
        assert 'Moab' in self.browser.page_source


    def test_get_list_of_visited_places(self):
        self.browser.get(self.live_server_url + '/city/1/edit')
        assert 'Wishlist' in self.browser.header
        assert 'Tokyo' in self.browser.page_source
        assert 'New York' not in self.browser.page_source
        assert 'San Francisco' not in self.browser.page_source
        assert 'Moab' not in self.browser.page_source

        self.browser.get(self.live_server_url + '/city/2/edit')
        assert 'Wishlist' in self.browser.header
        assert 'Tokyo' not in self.browser.page_source
        assert 'New York' in self.browser.page_source
        assert 'San Francisco' not in self.browser.page_source
        assert 'Moab' not in self.browser.page_source

        self.browser.get(self.live_server_url + '/city/3')
        assert 'Wishlist' in self.browser.header
        assert 'Tokyo' not in self.browser.page_source
        assert 'New York' not in self.browser.page_source
        assert 'San Francisco' in self.browser.page_source
        assert 'Moab' not in self.browser.page_source

        self.browser.get(self.live_server_url + '/city/4')
        assert 'Wishlist' in self.browser.header
        assert 'Tokyo' not in self.browser.page_source
        assert 'New York' not in self.browser.page_source
        assert 'San Francisco' not in self.browser.page_source
        assert 'Moab' in self.browser.page_source
