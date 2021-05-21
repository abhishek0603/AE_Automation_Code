
from ..core.PageObject import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class LoginPage(PageObject):
    # Define required page elements

    username_field  = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH,"//*[@placeholder='User ID']")))
    password_field  = lambda self: self.webdriver.find_element_by_xpath("//*[@placeholder='Password']")
    login_button    = lambda self: self.webdriver.find_element_by_xpath("//span[text()=' Login']")
    profile_img     = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH,"//img[@class='profile-img']")))
    SignOutLink     = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='Sign Out']")))


    def login(self, username, password):
        # try to login with provided username/password
        self.username_field().send_keys(username)
        self.password_field().send_keys(password)
        self.login_button().click()

    def logout(self):
        self.profile_img().click()
        self.SignOutLink().click()




