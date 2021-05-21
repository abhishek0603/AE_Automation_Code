import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage


class jumpshot_lotame(tests.SeleniumTest):
    def test_create_MSSA_FB_and(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource('Browsing Behavior')
        audience_page.create_browsing_behaviour_domain_names('facebook.com')

        sleep(5)
        audience_page.add_dataSource('Advanced Audience Data')
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media', 'Facebook')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " MSOA - FB - JS and Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_MSSA_IG_and(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource('Browsing Behavior')
        audience_page.create_browsing_behaviour_domain_names('instagram.com')
        sleep(5)
        audience_page.add_dataSource('Advanced Audience Data')
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media','Instagram')
        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " MSOA - IG - JS and Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_MSSA_FB_or(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource('Browsing Behavior')
        audience_page.create_browsing_behaviour_domain_names('facebook.com')
        sleep(5)
        audience_page.add_dataSource('Advanced Audience Data')
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media','Facebook')
        list = self.webdriver.find_elements_by_xpath("//div[contains(@class,'criteria-oper-groups')]/div[text()='AND']")
        list[1].click()
        self.webdriver.find_element_by_xpath("//div[text()='OR']").click()

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " MSSA - FB - JS or Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_MSAA_IG_or(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource('Browsing Behavior')
        audience_page.create_browsing_behaviour_domain_names('instagram.com')
        sleep(5)
        audience_page.add_dataSource('Advanced Audience Data')
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media','Instagram')
        list = self.webdriver.find_elements_by_xpath("//div[contains(@class,'criteria-oper-groups')]/div[text()='AND']")
        list[1].click()
        self.webdriver.find_element_by_xpath("//div[text()='OR']").click()

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " MSAA - IG - JS or Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

