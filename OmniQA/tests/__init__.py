
import unittest, os,sys
from selenium import webdriver
from an.test.core.config import Config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from an.test.ab.LoginPage import LoginPage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

SELENIUM_HUB = 'http://devel.annalect.com:4444/wd/hub'
DESIRED_CAPABILITIES = DesiredCapabilities.CHROME


class SeleniumTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        cls.config = Config().get_config()
        cls.configAB = Config().get_config_ab()
        cls.omni_url = cls.config["omni_url"]
        cls.workspace = os.getcwd()
        omni_username = cls.configAB["AELogin"]["username"]
        omni_password = cls.configAB["AELogin"]["password"]

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('w3c', False)
        prefs = {'download.default_directory': cls.workspace + '\original', 'profile.content_settings.exceptions.automatic_downloads.*.setting': 1, "safebrowing.enabled": "false"}
        # print(cls.workspace + '\original' + " this is the workspace")
        options.add_experimental_option('prefs', prefs)
        # prefs = {'download.default_directory': cls.workspace}
        # options.add_experimental_option('prefs', prefs)
        options.add_argument('disable-infobars')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        options.add_argument('--start-maximized')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-extensions")

        # Uncheck to run on docker
        # options.add_argument("user-data-dir=/home/seluser/.config/google-chrome/chrome_profile")
        # cls.webdriver = webdriver.Remote(command_executor=SELENIUM_HUB, desired_capabilities=options.to_capabilities())

        cls.webdriver = webdriver.Chrome(chrome_options=options)
        cls.webdriver.get("https://qaomni.annalect.com")
        cls.webdriver.delete_all_cookies()
        cls.webdriver.maximize_window()
        cls.webdriver.get(cls.omni_url)
        login_page = LoginPage(cls.webdriver, cls.config)
        try:
            login_page.login(omni_username, omni_password)
        except:
            pass
        sleep(10)

        try:
            # WebDriverWait(cls.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//div[@class ='side-tool settings']"))).click()
            WebDriverWait(cls.webdriver, 1000).until(EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#main>div.content.omni-ring-nav-content>div.side-tools"))).click()
            sleep(10)
            # cls.webdriver.find_element_by_xpath("//button[text()='Clear Saved Values']").click()
            # sleep(5)
            ClientVisible = WebDriverWait(cls.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@ng-model,'clientsVisible')]")))
            sleep(2)
            # Select(ClientVisible).deselect_by_visible_text('Omni QA Client')
            Select(ClientVisible).select_by_visible_text('Omni Demo')
            sleep(9)
            WebDriverWait(cls.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save']"))).click()
            sleep(8)
        except:
            print('Selected Client may not be available')
        WebDriverWait(cls.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@ng-click,'sidebarShow()') and (@class='header_nav_btn')]"))).click()
        # WebDriverWait(cls.webdriver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#an_header>button.header_nav_btn"))).click()
        sleep(5)
        WebDriverWait(cls.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
        sleep(5)

    def setUp(cls):
        try:
            cls.webdriver.switch_to.default_content()
        except:
            cls.setUpClass()
            iframe = cls.webdriver.find_elements_by_tag_name('iframe')[0]
            cls.webdriver.switch_to.frame(iframe)
        else:
            WebDriverWait(cls.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Audience Explorer (Omni)']"))).click()
            iframe = cls.webdriver.find_elements_by_tag_name('iframe')[0]
            cls.webdriver.switch_to.frame(iframe)

    def tearDown(cls):
        pass

    # @classmethod
    # def tearDownClass(cls):
    #     try:
    #         cls.webdriver.quit()
    #     except:
    #         pass


class OmniSeleniumTest(unittest.TestCase):

    def setUp(self):
        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")
        self.config = Config().get_config()
        self.configAB = Config().get_config_ab()
        self.omni_url = self.config["omni_url"]
        self.workspace = os.getcwd()
        omni_username = self.configAB["AELogin"]["username"]
        omni_password = self.configAB["AELogin"]["password"]

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_experimental_option('w3c', False)
        # prefs = {'download.default_directory': cls.workspace}
        # options.add_experimental_option('prefs', prefs)
        options.add_argument('disable-infobars')
        options.add_experimental_option('useAutomationExtension', False)
        options.add_experimental_option('excludeSwitches', ['enable-automation'])

        # # Uncheck to run on docker
        # options.add_argument("user-data-dir=/home/seluser/.config/google-chrome/chrome_profile")
        # self.webdriver = webdriver.Remote(command_executor=SELENIUM_HUB, desired_capabilities=options.to_capabilities())

        self.webdriver = webdriver.Chrome(chrome_options=options)
        self.webdriver.delete_all_cookies()
        self.webdriver.maximize_window()
        self.webdriver.get(self.omni_url)
        login_page = LoginPage(self.webdriver, self.config)
        try:
            login_page.login(omni_username, omni_password)
        except:
            pass
        sleep(5)

    def tearDown(self):
        pass
        self.webdriver.quit()

