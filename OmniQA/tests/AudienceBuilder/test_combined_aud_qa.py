import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage


class combined_aud(tests.SeleniumTest):
    def test_all(self):
        country = self.configAB["Conceptual"]["country"]
        project_name = self.configAB["Conceptual"]["project_name"]
        ds_type = "Browsing Behavior"

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()
        audience_page = AudiencePage(self.webdriver, self.config)
        try:
            audience_page.add_dataSource(ds_type)
            # audience_page.create_browsing_behaviour_domain_categories_multiple_sub_category('Social Media',sub_category=['Blogs','Social Networking'])
            audience_page.create_browsing_behaviour_domain_categories_single_sub_category('Social Media', 'Blogs')
            audience_page.add_dataSource(ds_type)
            audience_page.create_browsing_behaviour_domain_categories_single_sub_category('Social Media', 'Social Networking')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA - Any Social - JS")
            sleep(10)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e,country + " SSA - Any Social - JS")
            audience_page.aud_back_arrow().click()


        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_browsing_behaviour_domain_names('facebook.com')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA - FB - JS")
            sleep(10)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSA - FB - JS")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_browsing_behaviour_domain_names('instagram.com')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA - IG - JS")
            sleep(10)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSA - IG - JS")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
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
        except Exception as e:
            print(e, country + " SSOA - FB,IG - JS")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_browsing_behaviour_domain_names('facebook.com')

            audience_page.add_dataSource(ds_type)
            audience_page.create_browsing_behaviour_domain_names('instagram.com')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSAA - FB & IG - JS")
            sleep(10)
            audience_page.save_and_create_button().click()

        except Exception as e:
            print(e, country + " SSAA - FB & IG - JS")
            audience_page.aud_back_arrow().click()

        ######################Lotame#######################


        ###################################################

        ds_type = "Advanced Audience Data"
        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('In-Market Audiences', 'Automotive & Vehicles', 'Cars','TRUE')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA-Auto In Market-Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
            ###############################################
        except Exception as e:
            print(e, country + " SSA-Auto In Market-Lotm")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('In-Market Audiences',
                                                                                          'Automotive & Vehicles',
                                                                                          'Car Classifications',
                                                                                          value=['Luxury SUV',
                                                                                                 'Luxury Sedan'])

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
            audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('In-Market Audiences',
                                                                                          'Automotive & Vehicles',
                                                                                          'Car Classifications',
                                                                                          value=['Luxury SUV',
                                                                                                 'Luxury Sedan'])
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria_multiple_attribute_value('Purchase History',
                                                                                          'Automotive & Vehicles',
                                                                                          'Car Classifications',
                                                                                          value=['Luxury SUV',
                                                                                                 'Luxury Sedan'])

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSAA-Lux Auto InMarket & Own-Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSAA-Lux Auto InMarket & Own-Lotm")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Any Social Media')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA Any Social - Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSA Any Social - Lotm")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Demographics', 'Gender', 'Male', 'TRUE')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " Population Male")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " Population Male")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Demographics', 'Gender', 'Female', 'TRUE')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " Population Female")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " Population Female")
            audience_page.aud_back_arrow().click()

        ######################################

        for age_range in ['18-24', '25-34', '35-44', '45-54', '55-64', '65+']:
            try:
                proj_page = ProjectPage(self.webdriver, self.config)
                proj_page.add_audience_button().click()

                audience_page.add_dataSource(ds_type)
                # audience_page.create_advanced_audience_data_criteria('Demographics', 'Age', age_range, 'TRUE')
                audience_page.create_advanced_audience_data_criteria('Demographics', 'Age', 'Age Group', age_range)

                audience_page.audience_name_textbox().clear()
                audience_page.audience_name_textbox().send_keys(country + " Population " + age_range)
                sleep(5)
                audience_page.save_and_create_button().click()
            except Exception as e:
                print(e, country +" Population " + age_range)
                audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Facebook')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA - FB - Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSA - FB - Lotm")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Instagram')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSA - IG - Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSA - IG - Lotm")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Facebook')
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Instagram')

            list = self.webdriver.find_elements_by_xpath("//div[contains(@class,'criteria-oper')]/div[text()='AND']")
            list[1].click()
            self.webdriver.find_element_by_xpath("//div[text()='OR']").click()

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSOA - FB,IG - Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSOA - FB,IG - Lotm")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Facebook')
            audience_page.add_dataSource(ds_type)
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Instagram')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " SSAA - FB & IG - Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " SSAA - FB & IG - Lotm")
            audience_page.aud_back_arrow().click()

        #################################################

        ##################jumpshot-lotame################

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource('Browsing Behavior')
            audience_page.create_browsing_behaviour_domain_names('facebook.com')

            sleep(5)
            audience_page.add_dataSource('Advanced Audience Data')
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Facebook')

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " MSSA - FB - JS and Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " MSSA - FB - JS and Lotm")
            audience_page.aud_back_arrow().click()


        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource('Browsing Behavior')
            audience_page.create_browsing_behaviour_domain_names('instagram.com')
            sleep(5)
            audience_page.add_dataSource('Advanced Audience Data')
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Instagram')
            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " MSAA - IG - JS and Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " MSAA - IG - JS and Lotm")
            audience_page.aud_back_arrow().click()

        try:
            proj_page.add_audience_button().click()
            audience_page.add_dataSource('Browsing Behavior')
            audience_page.create_browsing_behaviour_domain_names('facebook.com')
            sleep(5)
            audience_page.add_dataSource('Advanced Audience Data')
            audience_page.create_advanced_audience_data_criteria('Affinity Audiences', 'Digital Engagement', 'Social Media',
                                                                 'Facebook')
            list = self.webdriver.find_elements_by_xpath("//div[contains(@class,'criteria-oper-groups')]/div[text()='AND']")
            list[1].click()
            self.webdriver.find_element_by_xpath("//div[text()='OR']").click()

            audience_page.audience_name_textbox().clear()
            audience_page.audience_name_textbox().send_keys(country + " MSOA - FB - JS or Lotm")
            sleep(5)
            audience_page.save_and_create_button().click()
        except Exception as e:
            print(e, country + " MSOA - FB - JS or Lotm")
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