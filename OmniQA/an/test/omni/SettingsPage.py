from ..core.PageObject import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class SettingsPage(PageObject):
    # Define required page elements

    save_button     = lambda self: self.webdriver.find_element_by_xpath("//button[text()='Save']")
    clear_button    = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//button[text()='Clear Saved Values']")))
    password_field  = lambda self: self.webdriver.find_element_by_xpath("//*[@placeholder='Password']")
    login_button    = lambda self: self.webdriver.find_element_by_xpath("//span[text()=' Login']")
    profile_img     = lambda self: WebDriverWait(self.webdriver, 500).until(EC.visibility_of_element_located((By.XPATH,"//img[@class='profile-img']")))
    SignOutLink     = lambda self: WebDriverWait(self.webdriver, 500).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Sign Out']")))


    def selectClient(self):
        sleep(10)
        self.webdriver.find_element_by_xpath("//option[text()='Nissan US']").click()
        sleep(10)
        self.webdriver.find_element_by_xpath("//option[text()='[ALL]']").click()
        sleep(10)
        self.save_button().click()

    def clickClearSavedValues(self):
        sleep(10)
        self.clear_button().click()


    def selectMultipleClient(self):
        self.webdriver.find_element_by_xpath("//option[text()='Intel EMEA']").click()
        sleep(10)
        self.webdriver.find_element_by_xpath("//option[text()='Nissan US']").click()
        sleep(10)
        self.webdriver.find_element_by_xpath("//option[text()='[ALL]']").click()
        sleep(10)
        self.save_button().click()

