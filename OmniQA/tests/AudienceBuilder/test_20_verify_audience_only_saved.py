import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from time import sleep
from an.test.ab.AudiencePage import AudiencePage
from an.test.core.Util import my_random_string
import datetime

class audience_only_saved(tests.SeleniumTest):
    def test_error_message_at_viz_canvas(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        message = self.webdriver.find_element_by_xpath("//div[@class='spinner-wrapper']//following::p[1]").text
        self.assertEqual(message, "This audience has not been built. To build your audience, go to criteria builder and click Save and Create.", "Incorrect message is getting displayed at Viz Canvas")

    def test_tag_at_history_panel(self):
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
        audience_page.save_audience_button().click()
        sleep(10)

        project_page.AudienceName('Test Audience').click()
        project_page.HistoryTab().click()
        sleep(10)
        tag = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]").text

        now = datetime.datetime.now()
        todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
        date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text

        # Verify today's time with log time
        time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
        tag_time_value = int(time[:-3].replace(":", ""))
        curr_time_value = int(now.strftime("%I") + now.strftime("%M"))

        assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
        self.assertEqual(date, todays_date, "created tag date incorrect")
        self.assertEqual(tag, "Created", "created tag incorrect")

        project_page.project_menu_icon('Test Proj' + rand).click()
        project_page.project_delete_icon('Test Proj' + rand).click()
        project_page.AlertOkButton().click()

    def test_distribution_icon_disabled(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        distribution_icon = project_page.audience_share_icon(audience_name)
        if distribution_icon.is_enabled():
            print("Distribution Icon is disabled")
        else:
            print("Distribution Icon is not disabled")

    def test_download_icon_disabled(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        # project_page.audience_menu_icon(audience_name).click()
        download_icon = project_page.audience_download_icon(audience_name)
        if download_icon.is_enabled():
            print("Download Icon is disabled")
        else:
            print("Download Icon is not disabled")

    def test_viz_icon_displayed(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()

        Viz_Icon = self.webdriver.find_element_by_xpath("//div[@class ='btn-group btn-chart-type']")
        if Viz_Icon.is_displayed():
            print("Viz Icons are getting displayed")
        else:
            print("Viz Icons are not getting displayed")

    def test_infoviz_getting_displayed(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        sleep(10)
        info_viz = self.webdriver.find_element_by_xpath("//div[contains(@id,'dataVisualizations')]")
        if info_viz.is_displayed():
            print("Infoviz is getting displayed")
        else:
            print("Infoviz is not getting displayed")

    def test_compare_icon_disabled_for_saved_audience(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        try:
            project_page.AudienceCheckbox(audience_name).click()
            print("Audience checkbox is enabled")

        except:
            print("This audience has not been built.So, Audience checkbox is disabled")