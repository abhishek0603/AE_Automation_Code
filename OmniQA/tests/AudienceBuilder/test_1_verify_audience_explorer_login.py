import tests
from time import sleep

class audience_explorer_login(tests.SeleniumTest):
    def test_login(self):
        sleep(30)
        title = self.webdriver.find_element_by_xpath("//*[@class='search-title']").text
        self.assertEqual(title,"AUDIENCE EXPLORER","login Failed")




