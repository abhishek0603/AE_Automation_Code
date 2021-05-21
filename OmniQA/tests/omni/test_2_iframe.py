import tests
from time import sleep
from an.test.omni.LoginPage import LoginPage
from an.test.omni.HomePage import HomePage
from an.test.omni.AIP_ClientLandingPage import ClientLandingPage


class IFrameTest(tests.OmniSeleniumTest):
    def test_iframe_caching(self):
        home_page = HomePage(self.webdriver, self.config)
        home_page.verifySideBarClients()
        home_page.getOptimizationPage()
        home_page.getDataExplorerPage()

        landing_page = ClientLandingPage(self.webdriver,self.config)

        landing_page.dataToolTab()
        landing_page.getLibraryPage()

        home_page = HomePage(self.webdriver, self.config)
        home_page.cachingTest()

        sleep(15)
        iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        self.webdriver.switch_to_frame(iframe)
        sleep(10)
        flag = self.webdriver.find_element_by_xpath("//*[text()='Data Catalogs']").is_displayed()
        print(flag)
        self.assertEqual(flag,'True','IFrame cache not working')
