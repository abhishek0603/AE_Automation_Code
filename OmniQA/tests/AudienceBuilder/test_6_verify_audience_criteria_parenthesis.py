import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from an.test.core.Util import my_random_string

class audience_criteria_parenthesis(tests.SeleniumTest):
    def test_apply_parenthesis_on_single_datasource(self):
        section = self.__class__.__name__
        project_name  = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)

        audience_page = AudiencePage(self.webdriver, self.config)
        WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Age between 18, 36']"))).click()
        self.webdriver.find_element_by_xpath("//div[text()='Income Level in Greater than $124,999']").click()
        audience_page.click_parenthesis_icon()
        self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope paren-criteria']").click()
        sleep(10)
        self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope paren-criteria selected']/img").click()

    def test_apply_parenthesis_on_multiple_datasources(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        sleep(15)
        audience_page = AudiencePage(self.webdriver, self.config)
        WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Demographic Data']"))).click()
        WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//div[text()='Location Data']"))).click()
        audience_page.click_parenthesis_icon()
        self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope']").click()
        sleep(10)
        self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope selected']/img").click()

    # def test_apply_parenthesis_on_single_datasource_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Adding Criteria
    #     project_page.add_audience_button().click()
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Purchase Behavior')
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
    #     self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
    #     criteria_createButton = self.webdriver.find_element_by_xpath(
    #         "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
    #     self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
    #     # audience_page.criteria_createButton().click()
    #     sleep(5)
    #     # Selecting Criteria
    #     WebDriverWait(self.webdriver, 50).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[text()='Category in AIR FRESHENERS']"))).click()
    #     # Clicking on parenthesis icon
    #     parenthesis_icon = self.webdriver.find_element_by_xpath("//div[@title='To apply, click to multi-select the criteria or source groups you want to parenthesize. Then click this icon.']")
    #     self.webdriver.execute_script("arguments[0].click();", parenthesis_icon)
    #     # Deleting Parenthesis, Criteria and Project
    #     self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope paren-criteria']").click()
    #     sleep(10)
    #     self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope paren-criteria selected']/img").click()
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()

    # def test_apply_parenthesis_on_multiple_datasources_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Adding Criteria
    #     project_page.add_audience_button().click()
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.add_dataSource('Location Data')
    #     audience_page.create_location_data_state('AL')
    #     sleep(5)
    #     # Selecting Criteria
    #     WebDriverWait(self.webdriver, 50).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[text()='Browsing Behavior']"))).click()
    #     sleep(5)
    #     WebDriverWait(self.webdriver, 50).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[text()='Location Data']"))).click()
    #     sleep(5)
    #     # Clicking on parenthesis icon
    #     parenthesis_icon = self.webdriver.find_element_by_xpath(
    #         "//div[@title='To apply, click to multi-select the criteria or source groups you want to parenthesize. Then click this icon.']")
    #     self.webdriver.execute_script("arguments[0].click();", parenthesis_icon)
    #     # Deleting Parenthesis, Criteria and Project
    #     self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope']").click()
    #     sleep(10)
    #     self.webdriver.find_element_by_xpath("//div[@class='paren ng-scope selected']/img").click()
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
