import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
import json,os
from selenium import webdriver
from selenium.webdriver import ActionChains

class Lotame_Viz(tests.SeleniumTest):
    def test_create_advance_data_audiences(self):
        # project_name = self.configAB["Lotame_Viz"]["project_name"]
        # path = os.path.join('testdata', 'sidebar.json')
        # print("location:" + path)

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects("Test_US_Automation")
        sleep(10)
        # Audience Creation using Advanced Audience Data
        proj_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Advance_Audience')
        audience_page.add_dataSource('Advanced Audience Data')
        source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'Advanced Audience Data Criteria')]")
        target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
        mouse = ActionChains(self.webdriver)
        mouse.drag_and_drop(source, target).perform()
        audience_page.create_advanced_audience_data_criteria('Food', 'Diet', 'Vegan', '3 Average')
        audience_page.add_criteria_plusicon().click()
        audience_page.create_advanced_audience_data_criteria('Demographic', 'Education', 'Education - Head of Household', 'Completed College')
        sleep(5)
        self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()
        audience_page.save_and_create_button().click()
        sleep(10)

    def test_create_purchase_data_audiences(self):

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects("Test_US_Automation")
        sleep(10)
        # Audience Creation using Advanced Audience Data
        proj_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Purchase_Audience')
        audience_page.add_dataSource('Purchase Behavior')
        criteria_label = self.webdriver.find_element_by_xpath("//div[contains(@class, 'header-label ng-binding ui-draggable-handle')]").text
        print(criteria_label)
        source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'"+ criteria_label +"')]")
        target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
        mouse = ActionChains(self.webdriver)
        mouse.drag_and_drop(source, target).perform()
        audience_page.create_purchase_data_criteria('Category', 'AIR FRESHENERS')
        # audience_page.add_criteria_plusicon().click()
        # audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Beauty and Wellness', 'Personal Care', 'Hair Care')
        sleep(5)
        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
        # sleep(5)
        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()
        audience_page.save_and_create_button().click()
        sleep(10)

    def test_create_demographic_data_audiences(self):

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects("Test_US_Automation")
        sleep(10)
        # Audience Creation using Advanced Audience Data
        proj_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Demographic_Audience')
        audience_page.add_dataSource('Demographic Data')
        criteria_label = self.webdriver.find_element_by_xpath("//div[contains(@class, 'header-label ng-binding ui-draggable-handle')]").text
        print(criteria_label)
        source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'"+ criteria_label +"')]")
        target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
        mouse = ActionChains(self.webdriver)
        mouse.drag_and_drop(source, target).perform()
        audience_page.create_demographic_data_criteria('Age')
        sleep(5)
        # audience_page.save_and_create_button().click()
        sleep(10)

    def test_create_location_data_audiences(self):

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects("Test_US_Automation")
        sleep(10)
        # Audience Creation using Advanced Audience Data
        proj_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Location_Audience')
        audience_page.add_dataSource('Location Data')
        criteria_label = self.webdriver.find_element_by_xpath("//div[contains(@class, 'header-label ng-binding ui-draggable-handle')]").text
        print(criteria_label)
        source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'"+ criteria_label +"')]")
        target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
        mouse = ActionChains(self.webdriver)
        mouse.drag_and_drop(source, target).perform()
        audience_page.create_location_data_state('State', 'CA')
        # audience_page.add_criteria_plusicon().click()
        # audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Beauty and Wellness', 'Personal Care', 'Hair Care')
        sleep(5)
        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
        # sleep(5)
        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()
        audience_page.save_and_create_button().click()
        sleep(10)

    def test_create_TV_Viewer_data_audiences(self):

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects("Test_US_Automation")
        sleep(10)
        # Audience Creation using Advanced Audience Data
        proj_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('TV_Viewer_Audience')
        audience_page.add_dataSource('TV Viewership Data')
        criteria_label = self.webdriver.find_element_by_xpath("//div[contains(@class, 'header-label ng-binding ui-draggable-handle')]").text
        print(criteria_label)
        source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'"+ criteria_label +"')]")
        target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
        mouse = ActionChains(self.webdriver)
        mouse.drag_and_drop(source, target).perform()
        audience_page.create_TV_viewership_data_criteria('Network', 'AMC')
        # audience_page.add_criteria_plusicon().click()
        # audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Beauty and Wellness', 'Personal Care', 'Hair Care')
        sleep(5)
        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
        # sleep(5)
        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()
        audience_page.save_and_create_button().click()
        sleep(10)

    def test_create_combo_demo_purchase_audiences(self):

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects("Test_US_Automation")
        sleep(10)
        # Audience Creation using Advanced Audience Data
        proj_page.add_audience_button().click()
        sleep(5)
        audience_page.audience_name_textbox().send_keys('Comb_Pur_Demo_Audience')
        audience_page.add_dataSource('Purchase Behavior')
        criteria_label = self.webdriver.find_element_by_xpath("//div[contains(@class, 'header-label ng-binding ui-draggable-handle')]").text
        print(criteria_label)
        source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'"+ criteria_label +"')]")
        target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
        mouse = ActionChains(self.webdriver)
        mouse.drag_and_drop(source, target).perform()
        audience_page.create_purchase_data_criteria('Category', 'AIR FRESHENERS')
        # audience_page.add_criteria_plusicon().click()
        # audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Beauty and Wellness', 'Personal Care', 'Hair Care')
        sleep(5)

        audience_page.add_dataSource('Demographic Data')
        criteria_label = self.webdriver.find_element_by_xpath("//div[contains(@class, 'header-label ng-binding ui-draggable-handle')]").text
        print(criteria_label)
        source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'" + criteria_label + "')]")
        target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
        mouse = ActionChains(self.webdriver)
        mouse.drag_and_drop(source, target).perform()
        audience_page.create_demographic_data_criteria('Age')
        sleep(5)



        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
        # sleep(5)
        # self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()
        audience_page.save_and_create_button().click()
        sleep(10)