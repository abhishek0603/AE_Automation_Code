import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage


class lotame(tests.SeleniumTest):
    def test_ssa(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Automotive & Vehicles', 'Cars', 'TRUE')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSA-Auto In Market-Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()
        ###############################################
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('In-Market Audiences', 'Automotive & Vehicles', 'Car Classifications',value=['Luxury SUV','Luxury Sedan'])

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSOA-Lux Auto In Market-Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()
        ###############################################
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('In-Market Audiences', 'Automotive & Vehicles', 'Car Classifications',value=['Luxury SUV','Luxury Sedan'])
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('Purchase History', 'Automotive & Vehicles', 'Car Classifications',value=['Luxury SUV','Luxury Sedan'])

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSAA-Lux Auto InMarket & Own-Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()
        ###############################################

    def test_MSOA_MSAA(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        # proj_page.add_audience_button().click()
        #
        # audience_page = AudiencePage(self.webdriver, self.config)
        # audience_page.add_dataSource(ds_type)
        # audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('In-Market Audiences', 'Automotive & Vehicles', 'Car Classifications', value=['Luxury SUV', 'Luxury Sedan'])
        # audience_page.add_dataSource(ds_type)
        # audience_page.create_browsing_behaviour_domain_names_multiple(name=['acura.com', 'lexus.com', 'bmw.com'])
        # audience_page.add_dataSource(ds_type)
        # audience_page.create_browsing_behaviour_domain_names_multiple(name=['acura.com', 'lexus.com', 'bmw.com'])
        # audience_page.audience_name_textbox().clear()
        # audience_page.audience_name_textbox().send_keys(country + " MSOA-Lux Auto-JS or Lotm")
        # sleep(5)
        # audience_page.save_and_create_button().click()
        # ###############################################
        sleep(5)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Demographics', 'Number of Children', '1 OR MORE', 'TRUE')
        audience_page.add_dataSource('Browsing Behavior')
        audience_page.create_browsing_behaviour_domain_names_multiple(name=['acura.com', 'lexus.com', 'bmw.com'])
        # audience_page.add_dataSource(ds_type)
        # audience_page.create_browsing_behaviour_domain_names_multiple(name=['acura.com', 'lexus.com', 'bmw.com'])
        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " MSAA-Lux Auto w  Kids-JS or Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_ssa_any_social(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences','Digital Engagement','Social Media','Any Social Media')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSA Any Social - Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_population_male(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver,  self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Demographics', 'Gender', 'Male', 'TRUE')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " Population Male")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_population_female(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver,  self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Demographics', 'Gender', 'Female', 'TRUE')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " Population Female")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_audience_population(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type      = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        for age_range in ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']:
            proj_page = ProjectPage(self.webdriver, self.config)
            proj_page.add_audience_button().click()

            audience_page = AudiencePage(self.webdriver, self.config)
            audience_page.add_dataSource(ds_type)
            # audience_page.create_advanced_audience_data_criteria('Demographics', 'Age', age_range, 'TRUE')
            audience_page.create_advanced_audience_data_criteria('Demographics', 'Age', 'Age Group', age_range)


            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country +" Population " + age_range)
            sleep(5)
            audience_page.save_and_create_button().click()

    def test_create_SSA_FB_Lotm(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences','Digital Engagement','Social Media','Facebook')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSA - FB - Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_SSA_IG_Lotm(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences','Digital Engagement','Social Media','Instagram')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSA - IG - Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_SSOA_FB_or_IG_Lotm(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media','Facebook')
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media','Instagram')

        list = self.webdriver.find_elements_by_xpath("//div[contains(@class,'criteria-oper')]/div[text()='AND']")
        list[1].click()
        self.webdriver.find_element_by_xpath("//div[text()='OR']").click()

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSOA - FB,IG - Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()

    def test_create_SSOA_FB_and_IG_Lotm(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences','Digital Engagement','Social Media','Facebook')
        audience_page.add_dataSource(ds_type)
        audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media','Instagram')

        audience_page.audience_name_textbox().clear()
        audience_page.audience_name_textbox().send_keys(country + " SSAA - FB & IG - Lotm")
        sleep(5)
        audience_page.save_and_create_button().click()
