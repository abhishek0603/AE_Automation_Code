import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from an.test.core.Util import my_random_string

class audience_compare(tests.SeleniumTest):
    # This is to verify if single audience are selected compare button is disable.
    def test_audience_comparebtn_disabled(self):
        section = self.__class__.__name__
        project_name   = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]

        home_page  = HomePage(self.webdriver,self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver,self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        check = "False"
        try:
            self.webdriver.find_element_by_xpath("//div[contains(@class,'compare-btn-disabled')]")
        except Exception as e:
            check = "True"

        print(check)
        self.assertEqual(check, "False", "Compare button is disabled")
        print("abc")

    # This is to verify if two audience are selected compare button is clickable and chart gets loaded.
    def test_audience_compare_button_enable(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        sleep(10)
        project_page.compare_button().click()
        sleep(10)

        # AQA-458: Check all the audiences selected for comparison appears at Viz Canvas
        aud_names = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='bar-chart-key-container ng-scope']")))).text
        audiences_selected = audience_name1 + " " + audience_name2
        self.assertEqual(aud_names, audiences_selected, "audiences selected for comparison didn't appear at Viz Canvas")

    # This is to verify if we are able to compare two audiences and then able to clear the selection
    def test_Clear_Selected_button(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        sleep(10)
        project_page.compare_button().click()
        sleep(10)

        check = self.webdriver.find_element_by_css_selector(".clear-button").is_displayed()
        project_page.ClearSelectedButton().click()

        check = self.webdriver.find_element_by_css_selector(".clear-button").is_displayed()
        self.assertEqual(check, False, "Clear button is disabled")

    #Check if compare icon is disabled if an audience & datasource are selected.
    def test_comparebtn_disabled2(self):
        section = self.__class__.__name__
        project_name     = self.configAB[section]["project_name"]
        audience_name    = self.configAB[section]["audience_name1"]
        data_source_name = self.configAB[section]["data_source_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        # project_page.DataSource(data_source_name).click()
        project_page.AudienceCheckbox(audience_name).click()
        check = "False"
        try:
            self.webdriver.find_element_by_xpath("//div[contains(@class,'compare-btn-disabled')]")
        except Exception as e:
            check = "True"
        self.assertEqual(check, "False", "Compare button is disabled")

    # This is to verify if more than two audiences are selected compare button is clickable and chart gets loaded.
    def test_multiple_audience_compare_button_enable(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]
        audience_name3 = self.configAB[section]["audience_name3"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        project_page.AudienceCheckbox(audience_name3).click()
        sleep(10)
        project_page.compare_button().click()
        sleep(10)
        # check = (WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//div[@class='chart-view']")))).is_displayed()
        # print(check)
        # self.assertEqual(check, True, "Compare button not working")

    def test_compare_chart_percent(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        sleep(10)
        project_page.compare_button().click()
        sleep(10)
        unit = self.webdriver.find_element_by_xpath("//div[@class='x-axis']/div[12]/span").text
        self.assertEqual(unit, "%", "X axis index values are inaccurate")

    def test_data_source_visualization(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        sleep(10)
        project_page.compare_button().click()
        sleep(10)
        project_page.view_filters_knob().click()
        try:
            project_page.select_datasource_visualization("Browsing Behavior")
            project_page.select_datasource_visualization("Purchase Behavior")
            project_page.select_datasource_visualization("Location Data")
        except:
            pass

    # This is to verify that more than three audiences are not allowed to compare
    def test_audience_checkbox_disable_after_selecting_third_audience(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]
        audience_name3 = self.configAB[section]["audience_name3"]
        audience_name4 = self.configAB[section]["audience_name4"]


        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        project_page.AudienceCheckbox(audience_name3).click()
        sleep(10)
        check = (self.webdriver.find_element_by_xpath("//div[contains(text(),'" + audience_name4 +"')]//parent::div//parent::div")).get_attribute('class')
        self.assertEqual(check, "audience-panel native-audience disabled", "Audience checkbox disable functionality not working.")

    def test_filters_single_audience(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.AudienceName(audience_name1).click()
        project_page.bubble_Chart_Icon().click()
        sleep(5)
        project_page.view_filters_knob().click()
        project_page.select_datasource_visualization("Purchase Behavior")
        project_page.select_category("AIR FRESHENERS")
        # project_page.select_subcategory("Resources")

        audience_name = self.webdriver.find_element_by_xpath("//div[@class='audience-name-label-normal']").text
        # print(audience_name)
        self.assertEqual(audience_name,audience_name1,"Comparison chart title incorrect or loading error")

    # def test_filters_subcatagories_reset_on_audience(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name1 = self.configAB[section]["audience_name1"]
    #
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.AudienceName(audience_name1).click()
    #     project_page.bubble_Chart_Icon().click()
    #     sleep(5)
    #     project_page.view_filters_knob().click()
    #     project_page.select_datasource_visualization("Advanced Audience Data")
    #     project_page.select_category("Auto")
    #     project_page.select_subcategory("Auto Club")
    #
    #     project_page.select_category("Children")
    #     list = self.webdriver.find_element_by_xpath("//form[@name='chartBase']/select[3]]").text
    #     print(list)
    #     newlist = "Select Subcategory"+ "\n"+ "Information"
    #
    #     self.assertEqual(list, newlist, "sub-category refresh not working.")

    def test_filters_on_audience_compare(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        sleep(5)
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        sleep(10)
        project_page.compare_button().click()
        sleep(10)
        project_page.view_filters_knob().click()
        project_page.select_datasource_visualization("Advanced Audience Data")
        project_page.select_category("Apparel")
        project_page.select_subcategory("Footwear")

        audiences_name = self.webdriver.find_element_by_css_selector(".bar-chart-key-container.ng-scope").text
        # print(audiences_name)
        chart_title = audience_name1 +" "+audience_name2

        self.assertEqual(audiences_name,chart_title,"Comparison chart title incorrect or loading error")

    # def test_filters_subcatagories_reset_on_audience_compare(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name1 = self.configAB[section]["audience_name1"]
    #     audience_name2 = self.configAB[section]["audience_name2"]
    #
    #     home_page = HomePage(self.webdriver, self.config)
    #     sleep(10)
    #     home_page.searchProjects(project_name)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.CompareTrigger().click()
    #     project_page.AudienceCheckbox(audience_name1).click()
    #     project_page.AudienceCheckbox(audience_name2).click()
    #     sleep(10)
    #     project_page.compare_button().click()
    #     sleep(10)
    #     project_page.view_filters_knob().click()
    #     project_page.select_datasource_visualization("Purchase Behavior")
    #     project_page.select_category("AIR FRESHNERS")
    #     # project_page.select_subcategory("Resources")
    #
    #     project_page.select_category("ASIAN FOOD")
    #     list = self.webdriver.find_element_by_xpath("//form[@name='chartBase']/select[3]").text
    #     # print(list)
    #     newlist = "Select Subcategory"+ "\n"+ "Information"
    #
    #     self.assertEqual(list, newlist, "sub catagory refresh not working.")

    def test_audience_compare_history_tab_disable(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name2 = self.configAB[section]["audience_name2"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        sleep(8)
        self.webdriver.find_element_by_xpath("//div[text()='Compare']").click()
        sleep(8)
        audiences_name = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR,".bar-chart-key-container.ng-scope")))).text
        sleep(5)
        try:
            project_page.HistoryTab().click()
            history_tab_not_found = False
        except:
            history_tab_not_found = True

        assert history_tab_not_found

    # This is to verify compare trigger is disable if there is no audience
    def test_compare_trigger_disabled(self):
        new_project_name = self.configAB["CreateProject"]["new_project_name"]
        data_env         = self.configAB["CreateProject"]["data_env"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(new_project_name)
        string = my_random_string(3)
        new_project_name = new_project_name + string

        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.createProject(new_project_name, data_env)

        element = WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".compare-trigger")))
        trigger = element.get_attribute("class")

        tooltip = WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//abbr"))).get_attribute("title")
        self.assertEqual(trigger, "compare-trigger disabled", "Compare trigger is not disabled")
        self.assertEqual(tooltip, "Compare feature available when you have at least two audiences.", "Compare trigger tooltip incorrect")
        proj_page.deleteProject(new_project_name)

    # This is to verify compare trigger is disable if there is single audience
    def test_compare_trigger_disabled_single_audience(self):
        new_project_name = self.configAB["CreateProject"]["new_project_name"]
        data_env = self.configAB["CreateProject"]["data_env"]

        home_page = HomePage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        proj_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(new_project_name)
        string = my_random_string(3)
        new_project_name = new_project_name + string
        proj_page.createProject(new_project_name, data_env)
        sleep(10)
        proj_page.add_audience_button().click()
        sleep(10)
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        sleep(5)
        audience_page.save_audience_button().click()
        element = WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".compare-trigger")))
        trigger = element.get_attribute("class")

        self.assertEqual(trigger, "compare-trigger disabled", "Compare trigger is not disabled")
        proj_page.deleteProject(new_project_name)

    def test_unable_to_compare_audiences_of_different_projects(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name1 = self.configAB[section]["audience_name1"]
        audience_name5 = self.configAB[section]["audience_name5"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        sleep(5)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        self.webdriver.find_element_by_xpath("//div[@class='dropdown-arrow']").click()
        self.webdriver.find_element_by_xpath("//*[@placeholder='Search for projects']").send_keys("DNT_Aud_Auto_Proj012")
        self.webdriver.find_element_by_xpath("//span[text()='DNT_Aud_Auto_Proj012']").click()
        sleep(15)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name5).click()
        compare = self.webdriver.find_element_by_xpath("//text()[contains(.,'Compare')]/ancestor::div[1]")
        if compare.is_selected():
            print("Compare text is enabled")
        else:
            print("Compare text is disabled")

    # def test_Clear_Select_button_onthefly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # 1st Audience Creation
    #     project_page.add_audience_button().click()
    #     sleep(5)
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Purchase Behavior')
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
    #     self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
    #     criteria_createButton = self.webdriver.find_element_by_xpath(
    #         "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
    #     self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
    #     # audience_page.criteria_createButton().click()
    #     sleep(5)
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 2nd Audience Creation
    #     project_page.add_audience_button().click()
    #     sleep(5)
    #     audience_page.audience_name_textbox().send_keys('Test Audience2')
    #     audience_page.add_dataSource('Purchase Behavior')
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
    #     self.webdriver.find_element_by_xpath("//li[contains(text(),'ADULT INCONTINENCE')]").click()
    #     criteria_createButton = self.webdriver.find_element_by_xpath(
    #         "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
    #     self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
    #     # audience_page.criteria_createButton().click()
    #     sleep(5)
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     project_page.CompareTrigger().click()
    #     project_page.AudienceCheckbox("Test Audience1").click()
    #     project_page.AudienceCheckbox("Test Audience2").click()
    #     sleep(10)
    #
    #     check = self.webdriver.find_element_by_css_selector(".clear-button").is_displayed()
    #     project_page.ClearSelectedButton().click()
    #     check = self.webdriver.find_element_by_css_selector(".clear-button").is_displayed()
    #     self.assertEqual(check, False, "Clear button is disabled")
    #     # Project Deletion
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_audience_checkbox_disable_after_selecting_third_audience_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # 1st Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 2nd Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience2')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('instagram.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 3rd Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience3')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('twitter.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 4th Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience4')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('linkedin.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     project_page.CompareTrigger().click()
    #     project_page.AudienceCheckbox("Test Audience1").click()
    #     project_page.AudienceCheckbox("Test Audience2").click()
    #     project_page.AudienceCheckbox("Test Audience3").click()
    #     sleep(10)
    #     check = (self.webdriver.find_element_by_xpath("//div[contains(text(),'Test Audience4')]//parent::div//parent::div")).get_attribute('class')
    #     self.assertEqual(check, "audience-panel disabled", "Audience checkbox disable functionality not working.")
    #     # Project Deletion
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_audience_compare_history_tab_disable_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # 1st Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 2nd Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience2')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('instagram.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     project_page.CompareTrigger().click()
    #     project_page.AudienceCheckbox("Test Audience1").click()
    #     project_page.AudienceCheckbox("Test Audience2").click()
    #     sleep(8)
    #     self.webdriver.find_element_by_xpath("//div[text()='Compare']").click()
    #     sleep(5)
    #     try:
    #         project_page.HistoryTab().click()
    #         history_tab_not_found = False
    #     except:
    #         history_tab_not_found = True
    #     assert history_tab_not_found
    #     # Project Deletion
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_multiple_audience_compare_button_enable_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # 1st Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 2nd Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience2')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('instagram.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 3rd Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience3')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('twitter.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     project_page.CompareTrigger().click()
    #     project_page.AudienceCheckbox("Test Audience1").click()
    #     project_page.AudienceCheckbox("Test Audience2").click()
    #     project_page.AudienceCheckbox("Test Audience3").click()
    #     sleep(10)
    #     project_page.compare_button().click()
    #     sleep(10)
    #     # check = (WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//div[@class='chart-view']")))).is_displayed()
    #     # print(check)
    #     # self.assertEqual(check, True, "Compare button not working")
    #     # Project Deletion
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_comparebtn_disabled2_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # 1st Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     # 2nd Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience2')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('instagram.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     project_page.CompareTrigger().click()
    #     self.webdriver.find_element_by_xpath("//div[text()='NA - United States']//preceding::input[1]").click()
    #     self.webdriver.find_element_by_xpath("//div[text()='Test Audience1']//preceding::input[1]").click()
    #     check = "False"
    #     try:
    #         self.webdriver.find_element_by_xpath("//div[contains(@class,'compare-btn-disabled')]")
    #     except Exception as e:
    #         check = "True"
    #     self.assertEqual(check, "False", "Compare button is disabled")
    #     # Project Deletion
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
