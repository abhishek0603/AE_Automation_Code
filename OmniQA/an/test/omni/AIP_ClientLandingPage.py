from ..core.PageObject import PageObject, InvalidPageError
from ..core.Util import wait_until
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class ClientLandingPage(PageObject):
    # Define required page elements
    DataToolTab           = lambda self: WebDriverWait(self.webdriver, 200).until(EC.presence_of_element_located((By.XPATH,"//*[text()='Data Tools']")))
    LibraryTab            = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Library']")
    LoaderTab             = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Loader']")
    # Run checks to make sure that we are on the login page

    def dataToolTab(self):
        sleep(30)
        iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        self.webdriver.switch_to_frame(iframe)
        self.DataToolTab().click()
        sleep(10)

    def getLibraryPage(self):
        sleep(10)
        self.LibraryTab().click()
        sleep(10)

    def getExplorerIngestHomePage(self):
        # try to login with provided username/password
        sleep(5)
        self.LoaderTab().click()
        sleep(10)

