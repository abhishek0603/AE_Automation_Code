from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.LoginPage import LoginPage
from an.test.ab.AudiencePage import AudiencePage
from an.test.core.Util import my_random_string
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from an.test.core.Util import my_random_string

class criteria_builder_functionalities(tests.SeleniumTest):
    def test_verify_agerange_starts_from_eighteen(self):
        project_name = self.configAB["CreateAudience"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()
        sleep(10)
        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource("Demographic Data")
        sleep(5)
        audience_page.filter_col_dropdown().click()
        audience_page.webdriver.find_element_by_xpath("//option[text()='Age']").click()
        age_range = self.webdriver.find_element_by_xpath("//div[@class='criteria-edit-label slider-value-label']").text
        self.assertEqual(age_range, "Between 18 and 100", "Age range incorrect for demographic data")

    def test_verify_agerange_starts_from_eighteen_advance_audience(self):
        project_name    = self.configAB["CreateAudience"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()
        sleep(10)
        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource("Advanced Audience Data")
        showing_age_list = audience_page.check_advance_age()
        print(showing_age_list)
        str =showing_age_list.replace("\n", "\t").replace("Age Range in Household - ","").replace("Age - Head of Household","")\
            .replace("Age - Input Individual","").replace("18-24","").replace("25-34","").replace("35-44","").replace("45-54","").replace("55-64","").replace("65-74","")\
            .replace("75+","").replace(" - Male","").replace(" - Female","").replace(" - Unknown Gender","").replace("-","").strip()

        self.assertEqual(str, "", "Age attributes are not correct")

    def test_audience_timestamp(self):
        project_name = self.configAB["audience_timestamp"]["project_name"]
        audience_name = self.configAB["audience_timestamp"]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        sleep(10)
        timestamp = self.webdriver.find_element_by_xpath("//*[@class='criteria-panel']/div[5]").text
        # print(timestamp)
        assert timestamp.startswith("Last Created")

    def test_save_and_create_disable(self):
        project_name = self.configAB["CreateAudience"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()
        audience_name = 'Test Aud'+my_random_string(3)
        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.audience_name_textbox().send_keys(audience_name)
        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        sleep(5)
        audience_page.save_and_create_button().click()
        sleep(5)
        proj_page.audience_menu_icon(audience_name).click()
        proj_page.audienceEditIcon(audience_name)
        sleep(30)
        status = audience_page.save_and_create_button().get_attribute('disabled')
        self.assertEqual(status,'true','save and create disable feature not working')
        self.webdriver.find_element_by_css_selector(".back").click()

        proj_page.audience_menu_icon(audience_name).click()
        proj_page.audience_delete_icon(audience_name).click()
        proj_page.AlertOkButton().click()

    def test_created_audience_timestamp(self):
        project_name = self.configAB["audience_timestamp"]["project_name"]
        audience_name = self.configAB["audience_timestamp"]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        sleep(10)
        actual_timestamp = self.webdriver.find_element_by_xpath("//div[contains(@class,'edit-when ng-scope')]").text
        # print("This is the actual timestamp " + actual_timestamp)
        date_time = audience_page.lbl_date_time().text
        user = audience_page.lbl_User().text
        data_env = audience_page.lbl_data_env().text
        expected_timestamp = "Last Created" + " " + date_time + " By " + user + " " + data_env
        assert actual_timestamp.startswith("Last Created")
        self.assertEqual(actual_timestamp, expected_timestamp)

    def test_saved_audience_timestamp(self):
        project_name = self.configAB["Quarter_on_criteria_builder"]["project_name"]
        audience_name = self.configAB["Quarter_on_criteria_builder"]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        sleep(10)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        sleep(10)
        # timestamp = self.webdriver.find_element_by_xpath("//*[@class='criteria-panel']/div[5]/div").text
        actual_timestamp = self.webdriver.find_element_by_xpath("//div[contains(@class,'edit-when ng-scope')]").text
        # print("This is the actual timestamp " + actual_timestamp)
        date_time = audience_page.lbl_date_time().text
        user = audience_page.lbl_User().text
        data_env = audience_page.lbl_data_env().text
        expected_timestamp = "Last Saved" + " " + date_time + " By " + user + " " + data_env
        assert actual_timestamp.startswith("Last Saved")
        self.assertEqual(actual_timestamp, expected_timestamp)

    def test_time_period_criteria(self):
        project_name = self.configAB["CreateAudience"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()

        audience_page = AudiencePage(self.webdriver, self.config)
        time_period = audience_page.get_time_period().text
        self.assertEqual(time_period, "Q1 2020", "Default Time period incorrect")

        audience_page.click_edit_time_period().click()
        sleep(5)
        time_period_list = self.webdriver.find_element_by_xpath(
            "//div[text()='Select Time Period*']/following::select[contains(@ng-model,'selectedTimePeriodsNew')]/option[contains(@value,'object')]").text

    def test_verify_Quarter(self):
        project_name = self.configAB["Quarter_on_criteria_builder"]["project_name"]
        audience_name = self.configAB["Quarter_on_criteria_builder"]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        sleep(10)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        sleep(10)
        data_env = audience_page.lbl_data_env().text
        # print("This is the value of data environement " + data_env)
        quarter_time = audience_page.Time_Period().text
        # print("This is the time period " + quarter_time)
        self.assertIn(quarter_time, data_env)
        audience_page.Time_Period_Edit().click()
        drp_quarter = audience_page.drp_Quarter()
        dd_quarter = Select(drp_quarter)
        dd_quarter.select_by_visible_text("Q2 2019")
        audience_page.btn_quarter_create().click()
        sleep(15)
        audience_page.save_audience_button().click()
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        self.assertIn(quarter_time, data_env)
        sleep(10)

        data_env = audience_page.lbl_data_env().text
        # print("This is the value of data environement " + data_env)
        quarter_time = audience_page.Time_Period().text
        # print("This is the time period " + quarter_time)
        self.assertIn(quarter_time, data_env)
        audience_page.Time_Period_Edit().click()
        drp_quarter = audience_page.drp_Quarter()
        dd_quarter = Select(drp_quarter)
        dd_quarter.select_by_visible_text("Q1 2020")
        audience_page.btn_quarter_create().click()
        audience_page.save_audience_button().click()
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        self.assertIn(quarter_time, data_env)

    def test_save_and_create_audience_button(self):
        project_name = self.configAB["Save_Create_button_audiences"]["project_name"]
        audience_name = self.configAB["Save_Create_button_audiences"]["audience_name"]
        omni_username = self.configAB["AELogin"]["username"]
        # omni_password         = self.configAB["AELogin"]["password"]
        shared_username = self.configAB["Save_Create_button_audiences"]["shared_userid"]
        shared_password = self.configAB["Save_Create_button_audiences"]["shared_pwd"]
        # category = self.configAB["Save_Create_button_audiences"]["category"]
        # sub_category = self.configAB["Save_Create_button_audiences"]["sub_category"]

        home_page = HomePage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        sleep(10)
        user_owner = audience_page.lbl_User().text
        print("This is the owner of this project " + user_owner)
        sleep(10)
        omni_first_name = omni_username.split('.')[0]
        print("This is the first name " + omni_first_name)
        omni_last_name = omni_username.split('.')[1]
        print("This is the last name " + omni_last_name)
        omni_owner = omni_first_name + " " + omni_last_name
        print("This is the omni_owner name " + omni_owner)
        # if user_owner == omni_username:
        btn_saveaud = audience_page.save_audience_button().is_enabled()
        print(btn_saveaud)
        self.assertIs(btn_saveaud, True)
        btn_savencreate = audience_page.save_and_create_button().is_enabled()
        print(btn_savencreate)
        self.assertIs(btn_savencreate, True)
        audience_page.add_criteria_plusicon().click()
        # audience_page.create_browsing_behaviour_domain_categories(category, sub_category)

        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)

        self.assertIs(btn_saveaud, True)
        self.assertIs(btn_savencreate, True)

        sleep(10)
        self.webdriver.switch_to_default_content()
        # actions = ActionChains(self.webdriver)
        # actions.move_to_element(project_page.img_profile()).perform()
        home_page.img_profile().click()
        sleep(5)
        home_page.link_signout().click()
        sleep(15)
        login_page = LoginPage(self.webdriver, self.config)
        login_page.login(shared_username, shared_password)
        sleep(15)
        WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='header_nav_btn']"))).click()

        sleep(5)
        # try:
        #     WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Clients']"))).click()
        #     sleep(5)
        #     WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'OMNI Demo') or contains(text(),'Omni Demo')]"))).click()
        #     sleep(5)
        #     WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//button[@class='header_nav_btn']"))).click()
        #     sleep(5)
        # except:
        #     pass
        WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
        sleep(5)
        iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        self.webdriver.switch_to.frame(iframe)

        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        sleep(10)
        user_owner = audience_page.lbl_User().text
        print("This is the owner of this project " + user_owner)
        sleep(10)
        shared_omni_first_name = shared_username.split('.')[0]
        print("This is the shared first name " + shared_omni_first_name)
        shared_omni_last_name = shared_username.split('.')[1]
        print("This is the shared last name " + shared_omni_last_name)
        shared_omni_owner = shared_omni_first_name + " " + shared_omni_last_name
        print("This is the shared omni_owner name " + shared_omni_owner)
        # if user_owner == omni_username:
        btn_saveaud = audience_page.save_audience_button().is_enabled()
        print(btn_saveaud)
        self.assertIs(btn_saveaud, False)
        btn_savencreate = audience_page.save_and_create_button().is_enabled()
        print(btn_savencreate)
        self.assertIs(btn_savencreate, False)
        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_criteria_plusicon().click()
        # audience_page.create_browsing_behaviour_domain_categories(category, sub_category)

        audience_page.add_dataSource('Purchase Behavior')
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
        self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)

        self.assertIs(btn_saveaud, False)
        self.assertIs(btn_savencreate, False)

    # def test_verify_agerange_starts_from_eighteen_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     project_page.add_audience_button().click()
    #     sleep(10)
    #     # Adding Criteria
    #     audience_page.add_dataSource("Demographic Data")
    #     sleep(5)
    #     audience_page.filter_col_dropdown().click()
    #     audience_page.webdriver.find_element_by_xpath("//option[text()='Age']").click()
    #     age_range = self.webdriver.find_element_by_xpath("//div[@class='criteria-edit-label slider-value-label']").text
    #     self.assertEqual(age_range, "Between 18 and 100", "Age range incorrect for demographic data")
    #     # Deleting Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_verify_agerange_starts_from_eighteen_advance_audience_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Adding Criteria
    #     project_page.add_audience_button().click()
    #     sleep(10)
    #     audience_page.add_dataSource("Advanced Audience Data")
    #     showing_age_list = audience_page.check_advance_age()
    #     str =showing_age_list.replace("\n", "\t").replace("Age Range in Household - ","").replace("Age - Head of Household","")\
    #         .replace("Age - Input Individual","").replace("18-24","").replace("25-34","").replace("35-44","").replace("45-54","").replace("55-64","").replace("65-74","")\
    #         .replace("75+","").replace(" - Male","").replace(" - Female","").replace(" - Unknown Gender","").replace("-","").strip()
    #
    #     self.assertEqual(str, "", "Age attributes are not correct")
    #     # Deleting Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_saved_audience_timestamp_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     project_name = 'Test Proj' + rand
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Adding Criteria
    #     project_page.add_audience_button().click()
    #     sleep(10)
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_audience_button().click()
    #     sleep(5)
    #     self.webdriver.switch_to_default_content()
    #     home_page.lbl_Audience_Explorer_omni().click()
    #     sleep(20)
    #     iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
    #     self.webdriver.switch_to.frame(iframe)
    #     home_page.searchProjects(project_name)
    #     sleep(5)
    #     project_page.audience_menu_icon('Test Audience1').click()
    #     project_page.audienceEditIcon('Test Audience1')
    #     actual_timestamp = self.webdriver.find_element_by_xpath("//div[contains(@class,'edit-when ng-scope')]").text
    #     # print("This is the actual timestamp " + actual_timestamp)
    #     date_time = audience_page.lbl_date_time().text
    #     user = audience_page.lbl_User().text
    #     data_env = audience_page.lbl_data_env().text
    #     expected_timestamp = "Last Saved" + " " + date_time + " By " + user + " " + data_env
    #     assert actual_timestamp.startswith("Last Saved")
    #     self.assertEqual(actual_timestamp, expected_timestamp)
    #     # Deleting Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_time_period_criteria_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     project_name = 'Test Proj' + rand
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Adding Criteria
    #     project_page.add_audience_button().click()
    #     time_period = audience_page.get_time_period().text
    #     self.assertEqual(time_period, "Q2 2019", "Default Time period incorrect")
    #
    #     audience_page.click_edit_time_period().click()
    #     sleep(5)
    #     time_period_list = self.webdriver.find_element_by_xpath(
    #         "//div[text()='Select Quarter*']/following::select[contains(@ng-model,'selectedTimePeriodsNew')]/option[contains(@value,'object')]").text
    #     # Deleting Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_save_and_create_disable_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_and_create_button().click()
    #     sleep(5)
    #     project_page.audience_menu_icon('Test Audience1').click()
    #     project_page.audienceEditIcon('Test Audience1')
    #     status = audience_page.save_and_create_button().get_attribute('disabled')
    #     self.assertEqual(status,'true','save and create disable feature not working')
    #     # Deleting Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_verify_Quarter_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     project_name = 'Test Proj' + rand
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_and_create_button().click()
    #     sleep(10)
    #     self.webdriver.switch_to_default_content()
    #     home_page.lbl_Audience_Explorer_omni().click()
    #     sleep(5)
    #     iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
    #     self.webdriver.switch_to.frame(iframe)
    #     home_page.searchProjects(project_name)
    #     sleep(5)
    #     project_page.audience_menu_icon('Test Audience1').click()
    #     project_page.audienceEditIcon('Test Audience1')
    #     sleep(10)
    #     data_env = audience_page.lbl_data_env().text
    #     #print("This is the value of data environment " + data_env)
    #     quarter_time = audience_page.Time_Period().text
    #     #print("This is the time period " + quarter_time)
    #     self.assertIn(quarter_time, data_env)
    #     audience_page.Time_Period_Edit().click()
    #     drp_quarter = audience_page.drp_Quarter()
    #     dd_quarter = Select(drp_quarter)
    #     dd_quarter.select_by_visible_text("Q2 2019")
    #     audience_page.btn_quarter_create().click()
    #     audience_page.save_audience_button().click()
    #     project_page.audience_menu_icon('Test Audience1').click()
    #     project_page.audienceEditIcon('Test Audience1')
    #     self.assertIn(quarter_time, data_env)
    #     sleep(10)
    #     data_env = audience_page.lbl_data_env().text
    #     #print("This is the value of data environement " + data_env)
    #     quarter_time = audience_page.Time_Period().text
    #     #print("This is the time period " + quarter_time)
    #     self.assertIn(quarter_time, data_env)
    #     audience_page.Time_Period_Edit().click()
    #     drp_quarter = audience_page.drp_Quarter()
    #     dd_quarter = Select(drp_quarter)
    #     dd_quarter.select_by_visible_text("Q1 2019")
    #     audience_page.btn_quarter_create().click()
    #     audience_page.save_audience_button().click()
    #     project_page.audience_menu_icon('Test Audience1').click()
    #     project_page.audienceEditIcon('Test Audience1')
    #     self.assertIn(quarter_time, data_env)
    #     # Deleting Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_save_and_create_audience_button_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     project_name = 'Test Proj' + rand
    #     omni_username = self.configAB["AELogin"]["username"]
    #     shared_username = 'ADMINQA.TEST'
    #     shared_password = 'Welcome@321'
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Audience Creation
    #     project_page.add_audience_button().click()
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.save_and_create_button().click()
    #     sleep(10)
    #     self.webdriver.switch_to_default_content()
    #     home_page.lbl_Audience_Explorer_omni().click()
    #     sleep(5)
    #     iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
    #     self.webdriver.switch_to.frame(iframe)
    #     home_page.searchProjects(project_name)
    #     sleep(5)
    #     project_page.audience_menu_icon('Test Audience1').click()
    #     project_page.audienceEditIcon('Test Audience1')
    #     sleep(10)
    #     user_owner = audience_page.lbl_User().text
    #     print("This is the owner of this project " + user_owner)
    #     sleep(10)
    #     omni_first_name = omni_username.split('.')[0]
    #     print("This is the first name " + omni_first_name)
    #     omni_last_name = omni_username.split('.')[1]
    #     print("This is the last name " + omni_last_name)
    #     omni_owner = omni_first_name + " " + omni_last_name
    #     print("This is the omni_owner name " + omni_owner)
    #     # if user_owner == omni_username:
    #     btn_saveaud = audience_page.save_audience_button().is_enabled()
    #     print(btn_saveaud)
    #     self.assertIs(btn_saveaud, True)
    #     btn_savencreate = audience_page.save_and_create_button().is_enabled()
    #     print(btn_savencreate)
    #     self.assertIs(btn_savencreate, True)
    #     audience_page.add_criteria_plusicon().click()
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     self.assertIs(btn_saveaud, True)
    #     self.assertIs(btn_savencreate, True)
    #
    #     sleep(10)
    #     self.webdriver.switch_to_default_content()
    #     # actions = ActionChains(self.webdriver)
    #     # actions.move_to_element(project_page.img_profile()).perform()
    #     home_page.img_profile().click()
    #     sleep(5)
    #     home_page.link_signout().click()
    #     sleep(15)
    #     login_page = LoginPage(self.webdriver, self.config)
    #     login_page.login(shared_username, shared_password)
    #     sleep(15)
    #     WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='header_nav_btn']"))).click()
    #
    #     sleep(5)
    #     # try:
    #     #     WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Clients']"))).click()
    #     #     sleep(5)
    #     #     WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'OMNI Demo') or contains(text(),'Omni Demo')]"))).click()
    #     #     sleep(5)
    #     #     WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//button[@class='header_nav_btn']"))).click()
    #     #     sleep(5)
    #     # except:
    #     #     pass
    #     WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
    #     sleep(5)
    #     iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
    #     self.webdriver.switch_to.frame(iframe)
    #
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon('Test Audience1').click()
    #     project_page.audienceEditIcon('Test Audience1')
    #     sleep(10)
    #     user_owner = audience_page.lbl_User().text
    #     print("This is the owner of this project " + user_owner)
    #     sleep(10)
    #     shared_omni_first_name = shared_username.split('.')[0]
    #     print("This is the shared first name " + shared_omni_first_name)
    #     shared_omni_last_name = shared_username.split('.')[1]
    #     print("This is the shared last name " + shared_omni_last_name)
    #     shared_omni_owner = shared_omni_first_name + " " + shared_omni_last_name
    #     print("This is the shared omni_owner name " + shared_omni_owner)
    #     # if user_owner == omni_username:
    #     btn_saveaud = audience_page.save_audience_button().is_enabled()
    #     print(btn_saveaud)
    #     self.assertIs(btn_saveaud, False)
    #     btn_savencreate = audience_page.save_and_create_button().is_enabled()
    #     print(btn_savencreate)
    #     self.assertIs(btn_savencreate, False)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     audience_page.add_criteria_plusicon().click()
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     self.assertIs(btn_saveaud, False)
    #     self.assertIs(btn_savencreate, False)
    #     # Deleting Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()