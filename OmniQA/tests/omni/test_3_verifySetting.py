import tests
from time import sleep
from an.test.omni.LoginPage import LoginPage
from an.test.omni.HomePage import HomePage
from an.test.omni.SettingsPage import SettingsPage


class SettingsTest(tests.OmniSeleniumTest):
    def test_setting_single_client_selection(self):
        home_page = HomePage(self.webdriver, self.config)
        home_page.verifySettingsLink()

        settings_page = SettingsPage(self.webdriver, self.config)
        settings_page.clickClearSavedValues()
        home_page.verifySettingsLink()
        settings_page.selectClient()
        client_list = home_page.getClientList()
        print(client_list)
        self.assertEqual(client_list, "", "Client list not updated")

    def test_setting_multiple_client_selection(self):
        home_page = HomePage(self.webdriver, self.config)
        home_page.verifySettingsLink()

        settings_page = SettingsPage(self.webdriver, self.config)
        settings_page.clickClearSavedValues()
        home_page.verifySettingsLink()
        settings_page.selectMultipleClient()

        client_list = home_page.getClientList()
        print(client_list)
        self.assertEqual(client_list, "Intel EMEANissan US", "Client list not updated")