import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage


class jumpshot(tests.SeleniumTest):
    def test_create_ssa_any_social_js(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Browsing Behavior"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        # audience_page.create_browsing_behaviour_domain_categories_multiple_sub_category('Social Media',sub_category=['Blogs','Social Networking'])
        audience_page.create_browsing_behaviour_domain_categories_single_sub_category('Social Media', 'Blogs')
        audience_page.add_dataSource(ds_type)
        audience_page.create_browsing_behaviour_domain_categories_single_sub_category('Social Media', 'Social Networking')
        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSA - Any Social - JS")
        sleep(10)
        audience_page.save_and_create_button().click()

    def test_create_SSA_FB_JS(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Browsing Behavior"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        sleep(10)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_browsing_behaviour_domain_names('facebook.com')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSA - FB - JS")
        sleep(10)
        audience_page.save_and_create_button().click()

    def test_create_SSA_IG_JS(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Browsing Behavior"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_browsing_behaviour_domain_names('instagram.com')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSA - IG - JS")
        sleep(10)
        audience_page.save_and_create_button().click()

    def test_create_SSA_FB_or_IG_JS(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Browsing Behavior"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_browsing_behaviour_domain_names('facebook.com')

        audience_page.inner_criteria_plusIcon().click()
        audience_page.create_browsing_behaviour_domain_names('instagram.com')
        list = self.webdriver.find_elements_by_xpath("//div[contains(@class,'criteria-oper')]/div[text()='AND']")
        list[1].click()
        self.webdriver.find_element_by_xpath("//div[text()='OR']").click()

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSOA - FB,IG - JS")
        sleep(10)
        audience_page.save_and_create_button().click()

    def test_create_SSA_FB_and_IG_JS(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Browsing Behavior"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_browsing_behaviour_domain_names('facebook.com')

        audience_page.add_dataSource(ds_type)
        audience_page.create_browsing_behaviour_domain_names('instagram.com')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSAA - FB & IG - JS")
        sleep(10)
        audience_page.save_and_create_button().click()