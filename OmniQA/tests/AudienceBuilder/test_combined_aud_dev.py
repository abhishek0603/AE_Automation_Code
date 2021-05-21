import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage


class combined_aud(tests.SeleniumTest):
    def test_all(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Advanced Audience Data"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()
        audience_page = AudiencePage(self.webdriver, self.config)
        try:
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('In-Market Audiences','Automotive & Vehicles','Car Classifications',value=['Luxury SUV','Luxury Sedan'])

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSOA-Lux Auto In Market-Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSOA-Lux Auto In Market-Lotm")
            audience_page.aud_back_arrow().click()
            ###############################################
        try:
            proj_page.add_audience_button().click()

            audience_page.add_dataSource(ds_type)
            # audience_page.create_advanced_audience_data_criteria('Demographics', 'Age', '18-24', 'TRUE')
            audience_page.create_advanced_audience_data_criteria('Demographics', 'Age', 'Age Group', '18-24')


            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " Population " + '18-24')
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " Population 18-24")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource('Browsing Behavior')
            audience_page.create_browsing_behaviour_domain_categories_multiple_sub_category('Social Media',sub_category=['Blogs','Social Networking'])

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA - Any Social - JS")
            sleep(10)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e,country + " SSA - Any Social - JS")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource('Browsing Behavior')
            audience_page.create_browsing_behaviour_domain_names('instagram.com')
            sleep(5)
            audience_page.add_dataSource('Advanced Audience Data')
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Instagram')
            list = self.webdriver.find_elements_by_xpath("//div[contains(@class,'criteria-oper-groups')]/div[text()='AND']")
            list[1].click()
            self.webdriver.find_element_by_xpath("//div[text()='OR']").click()

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " MSOA - IG - JS or Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " MSOA - IG - JS or Lotm")
            audience_page.aud_back_arrow().click()



