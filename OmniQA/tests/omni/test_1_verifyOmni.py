import tests
from time import sleep
from an.test.omni.LoginPage import LoginPage
from an.test.omni.HomePage import HomePage


class Omni01(tests.OmniSeleniumTest):
    def test_login(self):
        home_page = HomePage(self.webdriver, self.config)
        home_page.verifyHomePageApplicationLinks()

    def test_logout(self):
        login_page = LoginPage(self.webdriver, self.config)
        login_page.logout()
        sleep(15)
        current_url = self.webdriver.current_url
        print(current_url)
        self.assertEqual(current_url, self.omni_url+"/login", "Logout unsucessful")

    def test_Client_Logo_verify(self):
        home_page = HomePage(self.webdriver, self.config)
        img_src= home_page.verifySideBarClients()
        img_id= img_src.split('.jpg')[0]
        print(img_id)

        self.assertEqual(img_id, "https://s3.amazonaws.com/ssowrapper.dev/images/client_img_83e954a0-78a4-11e8-a162-0a3a7fe15bce","Client logo source not matching")

    def test_HomePageApplicationLinks(self):
        home_page = HomePage(self.webdriver, self.config)
        home_page.verifyHomePageApplicationLinks()
