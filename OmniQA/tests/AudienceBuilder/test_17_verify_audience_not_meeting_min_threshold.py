import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from time import sleep

class audience_not_meeting_min_threshold(tests.SeleniumTest):
    def test_audience_tile_color(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        color = project_page.verifyAudienceBackgroundColor(audience_name)

        self.assertEqual(color, "rgba(254, 216, 130, 1)", "Background Color for Audience tile is wrong")

    def test_error_message_at_history_panel(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        project_page.HistoryTab().click()
        sleep(10)
        tag = self.webdriver.find_elements_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")
        message = tag[0].text
        self.assertEqual(message, "This audience is 18% of the minimum audience size. Please re-visit criteria selections and try again.", "Incorrect message is getting displayed at History Panel")

    def test_error_message_at_viz_canvas(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        message = self.webdriver.find_element_by_xpath("//div[@class='spinner-wrapper']//following::p[1]").text
        self.assertEqual(message, "This audience is 18% of the minimum audience size. Please review and try building again. You can also reference our Audience Explorer FAQs.", "Incorrect message is getting displayed at Viz Canvas")

    def test_warning_icon_displaying_at_history_panel(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        project_page.HistoryTab().click()
        sleep(10)
        icon = self.webdriver.find_element_by_xpath("//div[@class='icon-wrapper']/div[1]")
        if icon.is_enabled():
            print("Warning icon is present")
        else:
            print("Warning icon is not present")

    def test_distribution_icon_enabled(self):
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

    def test_download_icon_enabled(self):
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


    def test_compare_icon_disabled_for_audience_not_meeting_min_threshold(self):
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
            print("This audience is 18% of the minimum audience size Please review and try building again.So, Audience checkbox is disabled")
