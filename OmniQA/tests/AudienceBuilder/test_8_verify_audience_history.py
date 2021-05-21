import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from an.test.core.Util import my_random_string
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import datetime

class audience_history(tests.SeleniumTest):

    def test_audience_history_tag_title(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        home_page.createProject('Test Proj' + rand, 'NA - United States')
        sleep(10)
        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page.add_audience_button().click()
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        # audience_page.criteria_createButton().click()
        sleep(5)
        audience_page.save_audience_button().click()
        sleep(10)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.AudienceName('Test Audience').click()
        project_page.HistoryTab().click()
        project_page.close_history().click()
        sleep(5)
        project_page.HistoryTab().click()

        list= self.webdriver.find_elements_by_xpath("//audience-history-list/ul/li/audience-history-item/ul/li[1]")

        for item in list:
            assert item.text == 'Test Audience'
        project_page.project_menu_icon('Test Proj' + rand).click()
        project_page.project_delete_icon('Test Proj' + rand).click()
        project_page.AlertOkButton().click()

    def test_audience_rename_tag(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        home_page.createProject('Test Rename'+rand,'NA - United States')
        sleep(10)
        project_page = ProjectPage(self.webdriver, self.config)
        project_page.add_audience_button().click()
        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.audience_name_textbox().send_keys('Audience rename test')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)

        audience_page.save_audience_button().click()
        sleep(10)
        project_page.audience_menu_icon('Audience rename test').click()
        project_page.audienceEditIcon('Audience rename test')
        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys('Audience rename test edited')
        audience_page.save_audience_button().click()
        sleep(10)

        project_page.AudienceName('Audience rename test edited').click()
        project_page.HistoryTab().click()
        sleep(10)
        tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text

        now = datetime.datetime.now()
        todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
        date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text

        # Verify today's time with log time
        time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
        tag_time_value = int(time[:-3].replace(":", ""))
        curr_time_value = int(now.strftime("%I") + now.strftime("%M"))

        assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
        self.assertEqual(date, todays_date, "created tag date incorrect")
        self.assertEqual(tag, "Edited", "Edited or rename tag incorrect")

        project_page.project_menu_icon('Test Rename'+rand).click()
        project_page.project_delete_icon('Test Rename'+rand).click()
        project_page.AlertOkButton().click()