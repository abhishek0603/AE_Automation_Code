import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
import json,os
from selenium import webdriver
from selenium.webdriver import ActionChains

class Lotame_Viz(tests.SeleniumTest):
    def test_create_audience(self):
        project_name = self.configAB["Lotame_Viz"]["project_name"]
        path = os.path.join('testdata', 'sidebar.json')
        print("location:" + path)

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)

        with open(path) as file:
            data = json.load(file)
        for item in range(len(data)):
            link = data[item]["link"]
            #Project Creation
            new_project_name = project_name + '_' + link
            print(new_project_name)
            proj_page.createProject(new_project_name, link)
            sleep(10)
            #Audience Creation
            proj_page.add_audience_button().click()
            sleep(5)
            audience_page.audience_name_textbox().send_keys('Any Travel')
            audience_page.add_dataSource('Advanced Audience Data')
            source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'Advanced Audience Data Criteria')]")
            target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
            mouse = ActionChains(self.webdriver)
            mouse.drag_and_drop(source,target).perform()
            audience_page.create_advanced_audience_data_criteria('Purchase History', 'Travel', 'Travel', 'Any  Air Travel')
            audience_page.add_criteria_plusicon().click()
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Travel', 'Travel', 'Any Travel')
            sleep(5)
            self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
            sleep(5)
            self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()

            audience_page.save_and_create_button().click()
            sleep(10)
            # Navigating to home screen
            self.webdriver.switch_to_default_content()
            home_page.lbl_Audience_Explorer_omni().click()
            sleep(10)
            iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
            self.webdriver.switch_to.frame(iframe)
            new_project_name = project_name

    def test_create_other_audiences(self):
        project_name = self.configAB["Lotame_Viz"]["project_name"]
        path = os.path.join('testdata', 'sidebar.json')
        print("location:" + path)

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)

        with open(path) as file:
            data = json.load(file)
        for item in range(len(data)):
            link = data[item]["link"]
            #Project selection
            new_project_name = project_name + '_' + link
            print(new_project_name)
            sleep(5)
            home_page.searchProjects(new_project_name)
            sleep(10)
            #Audience Creation
            proj_page.add_audience_button().click()
            sleep(5)
            audience_page.audience_name_textbox().send_keys('Beauty')
            audience_page.add_dataSource('Advanced Audience Data')
            source = self.webdriver.find_element_by_xpath("//div[contains(@class,'header-label ng-binding ui-draggable-handle') and contains(text(),'Advanced Audience Data Criteria')]")
            target = self.webdriver.find_element_by_xpath("//div[contains(@class, 'criteria-panel-header') and contains(text(),'Define Your Audience')]")
            mouse = ActionChains(self.webdriver)
            mouse.drag_and_drop(source,target).perform()
            audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Beauty and Wellness', 'Personal Care', 'Cosmetics')
            audience_page.add_criteria_plusicon().click()
            audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Beauty and Wellness', 'Personal Care', 'Hair Care')
            # audience_page.add_criteria_plusicon().click()
            # audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Lifestyle and Hobbies', 'Literature', 'Family Literature (Fiction)')
            # audience_page.add_criteria_plusicon().click()
            # audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Lifestyle and Hobbies', 'Literature', 'Family Literature (Non-Fiction)')

            sleep(5)
            self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
            sleep(5)
            self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()

            # If you have 3 audience criteria's
            # sleep(5)
            # self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]//following::div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
            # sleep(5)
            # self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()

            # If you have 4 audience criteria's
            # sleep(5)
            # self.webdriver.find_element_by_xpath("//div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]//following::div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]//following::div[contains(@class ,'text ng-binding') and contains(@ng-bind,'i.value')]").click()
            # sleep(5)
            # # self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]").click()
            # third_drp_value = self.webdriver.find_element_by_xpath("//div[contains(@class ,'ng-binding ng-scope') and contains(text(),'OR')]")
            # self.webdriver.execute_script("arguments[0].click();", third_drp_value)

            audience_page.save_and_create_button().click()
            sleep(10)
            # Navigating to home screen
            self.webdriver.switch_to_default_content()
            home_page.lbl_Audience_Explorer_omni().click()
            sleep(10)
            iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
            self.webdriver.switch_to.frame(iframe)
            new_project_name = project_name





