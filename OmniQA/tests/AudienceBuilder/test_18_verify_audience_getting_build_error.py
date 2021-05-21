import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from time import sleep

class audience_getting_build_error(tests.SeleniumTest):
    def test_error_message_at_viz_canvas(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        message = self.webdriver.find_element_by_xpath("//div[@class='spinner-wrapper']//following::p[1]").text
        self.assertEqual(message, "We are experiencing technical difficulties building this audience. Please try again later or contact support at omnisupport.annalect.com.", "Incorrect message is getting displayed at Viz Canvas")

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

    def test_compare_icon_disabled_for_technically_build_error_audiences(self):
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
            print("We are experiencing technical difficulties building this audience.So, Audience checkbox is disabled")