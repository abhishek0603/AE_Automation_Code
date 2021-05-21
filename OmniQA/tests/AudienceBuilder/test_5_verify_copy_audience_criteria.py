from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from selenium.webdriver.support import expected_conditions as EC
from an.test.core.Util import my_random_string

class audience_copy_criteria(tests.SeleniumTest):
    def test_copy_audience_single_criteria(self):
        section = self.__class__.__name__
        project_name                 = self.configAB[section]["project_name"]
        audience_name_single  = self.configAB[section]["audience_name_single_source"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.audience_menu_icon(audience_name_single).click()
        project_page.audienceEditIcon(audience_name_single)

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.copy_audience_criteria_within_self("Demographic Data")
        self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']").click()
        audience_page.delete_audience_criteria("Demographic Data")

    def test_copy_audience_multiple_criteria(self):
        section = self.__class__.__name__
        project_name                 = self.configAB[section]["project_name"]
        audience_name_multiple_source  = self.configAB[section]["audience_name_multiple_source"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name_multiple_source).click()
        project_page.audienceEditIcon(audience_name_multiple_source)

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.copy_multiple_audience_criteria_within_self()
        self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']").click()
        audience_page.delete_audience_criteria("Demographic Data")
        audience_page.delete_audience_criteria("Location Data")

    def test_copy_audience_single_criteria_to_other_audience(self):
        section = self.__class__.__name__
        project_name                 = self.configAB[section]["project_name"]
        audience_name_single         = self.configAB[section]["audience_name_single_source"]
        audience_name_single_dest    = self.configAB[section]["audience_name_single_dest"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name_single).click()
        project_page.audienceEditIcon(audience_name_single)

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.copy_audience_criteria_within_self("Demographic Data")
        self.webdriver.find_element_by_xpath("//div[@class='sources-panel']/div[1]").click()

        project_page.audience_menu_icon(audience_name_single_dest).click()
        project_page.audienceEditIcon(audience_name_single_dest)
        sleep(10)
        self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']").click()
        audience_page.delete_audience_criteria("Demographic Data")

    def test_copy_audience_multiple_criteria_to_other_audience(self):
        section                         = self.__class__.__name__
        project_name                    = self.configAB[section]["project_name"]
        audience_name_multiple_source   = self.configAB[section]["audience_name_multiple_source"]
        audience_name_multiple_dest     = self.configAB[section]["audience_name_multiple_dest"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name_multiple_source).click()
        project_page.audienceEditIcon(audience_name_multiple_source)

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.copy_multiple_audience_criteria_within_self()

        self.webdriver.find_element_by_xpath("//div[@class='sources-panel']/div[1]").click()

        project_page.audience_menu_icon(audience_name_multiple_dest).click()
        project_page.audienceEditIcon(audience_name_multiple_dest)
        sleep(5)

        self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']").click()
        audience_page.delete_audience_criteria("Demographic Data")
        audience_page.delete_audience_criteria("Location Data")

    # def test_browsing_behavior(self):
    #     project_name = self.configAB["browsing_behavior"]["project_name"]
    #     ds_type      = self.configAB["browsing_behavior"]["ds_type"]
    #
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #     sleep(10)
    #     proj_page = ProjectPage(self.webdriver, self.config)
    #     proj_page.AddAudienceButton().click()
    #     sleep(5)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.add_dataSource(ds_type)
    #     # self.webdriver.find_element_by_xpath("//div[@class='plus']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Categories']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'control.value')]").click()
    #     #Adding category with no subcategory
    #     self.webdriver.find_element_by_xpath("//option[text()='Government']").click()
    #     audience_page.criteria_createButton().click()
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//input[@placeholder='Name Your Audience']").clear()
    #
    #     audience_page.add_dataSource(ds_type)
    #     #Adding category with subcategory
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Categories']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'control.value')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Education']").click()
    #     audience_page.criteria_createButton().click()
    #     try:
    #         WebDriverWait(self.webdriver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[@class='red-btn an-primary-button ng-binding']"))).click()
    #         print("Alert popup came ")
    #     except TimeoutException:
    #         print("no alert")

    # def test_copy_audience_multiple_criteria_on_the_fly(self):
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
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('instagram.com')
    #     copy_multiple_criteria_button = self.webdriver.find_element_by_xpath("//img[@src='/static/img/copy-white.png']")
    #     self.webdriver.execute_script("arguments[0].click();", copy_multiple_criteria_button)
    #     self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']").click()
    #     #Pasted Criteria Verification
    #     list = self.webdriver.find_elements_by_xpath("//div[@class='criteria ng-scope']/div[1]")
    #     for x in range(len(list)):
    #         print(list[x].text)
    #     pasted_criteria = list[2].text
    #     self.assertEqual(pasted_criteria, 'Domain Names in facebook.com', "Criteria copied is not pasted correctly")
    #     pasted_criteria = list[3].text
    #     self.assertEqual(pasted_criteria, 'Domain Names in instagram.com', "Criteria copied is not pasted correctly")
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_copy_audience_multiple_criteria_to_other_audience_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #
    #     project_page.add_audience_button().click()
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('instagram.com')
    #     copy_multiple_criteria_button = self.webdriver.find_element_by_xpath("//img[@src='/static/img/copy-white.png']")
    #     self.webdriver.execute_script("arguments[0].click();", copy_multiple_criteria_button)
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # Inserting in Other Audience
    #     project_page.add_audience_button().click()
    #     insert_copied_criteria_button =self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']")
    #     self.webdriver.execute_script("arguments[0].click();", insert_copied_criteria_button)
    #     # Pasted Criteria Verification
    #     list = self.webdriver.find_elements_by_xpath("//div[@class='criteria ng-scope']/div[1]")
    #     for x in range(len(list)):
    #         print(list[x].text)
    #     pasted_criteria = list[0].text
    #     self.assertEqual(pasted_criteria, 'Domain Names in facebook.com', "Criteria copied is not pasted correctly")
    #     pasted_criteria = list[1].text
    #     self.assertEqual(pasted_criteria, 'Domain Names in instagram.com', "Criteria copied is not pasted correctly")
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_browsing_behavior_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     project_page.add_audience_button().click()
    #     sleep(10)
    #     audience_page.add_dataSource('Browsing Behavior')
    #     # self.webdriver.find_element_by_xpath("//div[@class='plus']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Categories']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'control.value')]").click()
    #     #Adding category with no subcategory
    #     self.webdriver.find_element_by_xpath("//option[text()='Government']").click()
    #     audience_page.criteria_createButton().click()
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//input[@placeholder='Name Your Audience']").clear()
    #
    #     audience_page.add_dataSource('Browsing Behavior')
    #     #Adding category with subcategory
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Categories']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'control.value')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Education']").click()
    #     audience_page.criteria_createButton().click()
    #     try:
    #         WebDriverWait(self.webdriver, 3).until(EC.presence_of_element_located((By.XPATH, "//button[@class='red-btn an-primary-button ng-binding']"))).click()
    #         print("Alert popup came ")
    #     except TimeoutException:
    #         print("no alert")
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
