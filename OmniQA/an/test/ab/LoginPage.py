from ..core.PageObject import PageObject, InvalidPageError
from ..core.Util import wait_until
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(PageObject):
    login_container = lambda self: self.webdriver.find_element_by_class_name("login-container")
    username_field  = lambda self: WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='User ID']")))
    password_field  = lambda self: self.webdriver.find_element_by_xpath("//input[@placeholder='Password']")
    login_button    = lambda self: self.webdriver.find_element_by_xpath("//span[text()='Sign In']")
    navigation_bar  = lambda self: self.webdriver.find_element_by_id("navbar-sso-user")

    # Run checks to make sure that we are on the login page
    def _validate_page(self, webdriver):
        try:
            # check URL of the page
            login_site = self.config["apps_url"]
            if not webdriver.current_url.startswith(login_site):
                raise Exception("We are not on the %s site" % login_site)
            # check that it has login container
            login_container = self.login_container()
        except Exception as e:
            error = e.message
            if not error and hasattr(e, "msg"):
                error = e.msg
            raise InvalidPageError("This is not login page: %s" % error)

    def login(self, username, password):
        # try to login with provided username/password
        self.username_field().send_keys(username)
        self.password_field().send_keys(password)
        self.login_button().click()

