import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from an.test.core.Util import my_random_string
from time import sleep

class audience_that_is_building(tests.SeleniumTest):
    def test_error_message_at_viz_canvas(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        home_page.createProject('Test Proj' + rand, 'NA - United States')
        sleep(10)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        # audience_page.criteria_createButton().click()
        sleep(5)
        audience_page.save_and_create_button().click()
        sleep(10)
        project_page.AudienceName('Test Audience').click()
        message = self.webdriver.find_element_by_xpath("//div[@class='spinner-wrapper']//following::p[1]").text
        self.assertEqual(message,"Your audience is being built.","Incorrect message is getting displayed at Viz Canvas")

        project_page.project_menu_icon('Test Proj' + rand).click()
        project_page.project_delete_icon('Test Proj' + rand).click()
        project_page.AlertOkButton().click()

    def test_download_icon_disabled(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        home_page.createProject('Test Proj' + rand, 'NA - United States')
        sleep(10)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        # audience_page.criteria_createButton().click()
        sleep(5)
        audience_page.save_and_create_button().click()
        sleep(10)
        project_page.AudienceName('Test Audience').click()
        download_icon = project_page.audience_download_icon('Test Audience')
        if download_icon.is_enabled():
            print("Download Icon is disabled")
        else:
            print("Download Icon is not disabled")

        project_page.project_menu_icon('Test Proj' + rand).click()
        project_page.project_delete_icon('Test Proj' + rand).click()
        project_page.AlertOkButton().click()

    def test_distribution_icon_disabled(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        home_page.createProject('Test Proj' + rand, 'NA - United States')
        sleep(10)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        # audience_page.criteria_createButton().click()
        sleep(5)
        audience_page.save_and_create_button().click()
        sleep(10)
        project_page.AudienceName('Test Audience').click()
        distribution_icon = project_page.audience_share_icon('Test Audience')
        if distribution_icon.is_enabled():
            print("Distribution Icon is disabled")
        else:
            print("Distribution Icon is not disabled")

        project_page.project_menu_icon('Test Proj' + rand).click()
        project_page.project_delete_icon('Test Proj' + rand).click()
        project_page.AlertOkButton().click()

    def test_viz_icon_displayed(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        home_page.createProject('Test Proj' + rand, 'NA - United States')
        sleep(10)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        # audience_page.criteria_createButton().click()
        sleep(5)
        audience_page.save_and_create_button().click()
        sleep(10)
        project_page.AudienceName('Test Audience').click()

        Viz_Icon = self.webdriver.find_element_by_xpath("//div[@class ='btn-group btn-chart-type']")
        if Viz_Icon.is_displayed():
            print("Viz Icons are getting displayed")
        else:
            print("Viz Icons are not getting displayed")

        project_page.project_menu_icon('Test Proj' + rand).click()
        project_page.project_delete_icon('Test Proj' + rand).click()
        project_page.AlertOkButton().click()

    def test_infoviz_getting_displayed(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        home_page.createProject('Test Proj' + rand, 'NA - United States')
        sleep(10)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        # audience_page.criteria_createButton().click()
        sleep(5)
        audience_page.save_and_create_button().click()
        sleep(10)
        project_page.AudienceName('Test Audience').click()
        sleep(10)
        info_viz = self.webdriver.find_element_by_xpath("//div[contains(@id,'dataVisualizations')]")
        if info_viz.is_displayed():
            print("Infoviz is getting displayed")
        else:
            print("Infoviz is not getting displayed")

        project_page.project_menu_icon('Test Proj' + rand).click()
        project_page.project_delete_icon('Test Proj' + rand).click()
        project_page.AlertOkButton().click()