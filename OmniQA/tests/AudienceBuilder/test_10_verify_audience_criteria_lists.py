import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from selenium.common.exceptions import NoSuchElementException
from an.test.core.Util import my_random_string

class audience_criteria_lists(tests.SeleniumTest):
    def test_purchase_behaviour(self):
        project_name = self.configAB["purchase_behaviour"]["project_name"]
        ds_type = self.configAB["purchase_behaviour"]["ds_type"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        proj_page = ProjectPage(self.webdriver, self.config)
        proj_page.add_audience_button().click()
        sleep(10)
        audience_page = AudiencePage(self.webdriver, self.config)
        audience_page.add_dataSource(ds_type)
        sleep(5)
        cols = self.webdriver.find_elements_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]/option")
        col = ""
        for i in cols:
            col = i.text +col

        print(col)
        self.assertEqual(col, "QuintileProduct NameSubcategoryCategory", "Purchase behaviour column list incorrect")

    def test_purchase_behaviour_category(self):
        project_name = self.configAB["purchase_behaviour"]["project_name"]
        ds_type = self.configAB["purchase_behaviour"]["ds_type"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        sleep(5)
        project_page.add_audience_button().click()
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource(ds_type)
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
        sleep(5)
        try:
            self.webdriver.find_element_by_xpath("//input[@placeholder='Begin typing to search...']").click()
            self.webdriver.find_element_by_xpath("//li[contains(text(),'AIR FRESHENERS')]").click()
            audience_page.aud_back_arrow().click()
        except NoSuchElementException:
            assert False

    def test_purchase_behaviour_subcategory(self):
        project_name = self.configAB["purchase_behaviour"]["project_name"]
        ds_type = self.configAB["purchase_behaviour"]["ds_type"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        sleep(5)
        project_page.add_audience_button().click()
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource(ds_type)
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Subcategory']").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//an-typeahead").click()
        sleep(5)
        try:
            self.webdriver.find_elements_by_xpath("//an-typeahead/div/ul/li")
            audience_page.aud_back_arrow().click()
        except NoSuchElementException:
            assert False

    def test_purchase_behaviour_product_name(self):
        project_name = self.configAB["purchase_behaviour"]["project_name"]
        ds_type = self.configAB["purchase_behaviour"]["ds_type"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        sleep(5)
        project_page.add_audience_button().click()
        audience_page.audience_name_textbox().send_keys('Test Audience')
        audience_page.add_dataSource(ds_type)
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        self.webdriver.find_element_by_xpath("//option[text()='Product Name']").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//an-typeahead").click()
        sleep(5)
        list = self.webdriver.find_elements_by_xpath("//an-typeahead/div/ul/li")
        p_name = ""
        for i in list:
            product_name= i.text
            if "category" in product_name:
                p_name= product_name

        self.assertEqual(p_name, "", "Product names list contain category")

    def test_verify_numbers(self):
        project_name = self.configAB["individual_count"]["project_name"]
        audience_name = self.configAB["individual_count"]["audience_name"]
        home_page = HomePage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        project_page = ProjectPage(self.webdriver, self.config)
        sleep(10)
        project_page.selectAudiences(audience_name)
        sleep(5)
        lbl_individual = audience_page.lbl_individuals(audience_name).text
        print("This is the value of individuals on the right " + lbl_individual)
        sleep(10)
        lbl_panelindividuals = audience_page.lbl_PanelIndividuals(audience_name).text
        print("This is the value of individuals on the left div " + lbl_panelindividuals)
        self.assertEqual(lbl_individual, lbl_panelindividuals)

        lbl_households = audience_page.lbl_household(audience_name).text
        print("This is the value of household on the right " + lbl_households)
        sleep(10)
        lbl_householdpanel = audience_page.lbl_PanelHousehold(audience_name).text
        print("This is the value of households on the left div " + lbl_householdpanel)
        self.assertEqual(lbl_households, lbl_householdpanel)

        lbl_device = audience_page.lbl_devices(audience_name).text
        print("This is the value of devices on the right " + lbl_device)
        sleep(10)
        lbl_devicepanel = audience_page.lbl_PanelDevice(audience_name).text
        print("This is the value of device on the left div " + lbl_devicepanel)
        self.assertEqual(lbl_device, lbl_devicepanel)

    # def test_purchase_behaviour_on_the_fly(self):
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
    #     audience_page.add_dataSource('Purchase Behavior')
    #     sleep(5)
    #     cols = self.webdriver.find_elements_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]/option")
    #     col = ""
    #     for i in cols:
    #         col = i.text +col
    #
    #     print(col)
    #     self.assertEqual(col, "QuintileProduct NameSubcategoryCategory", "Purchase behaviour column list incorrect")
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_purchase_behaviour_category_on_the_fly(self):
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
    #     audience_page.add_dataSource('Purchase Behavior')
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Category']").click()
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//an-typeahead").click()
    #     sleep(5)
    #     try:
    #         self.webdriver.find_elements_by_xpath("//an-typeahead/div/ul/li")
    #     except NoSuchElementException:
    #         assert False
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_purchase_behaviour_subcategory_on_the_fly(self):
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
    #     audience_page.add_dataSource('Purchase Behavior')
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Subcategory']").click()
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//an-typeahead").click()
    #     sleep(5)
    #     try:
    #         self.webdriver.find_elements_by_xpath("//an-typeahead/div/ul/li")
    #     except NoSuchElementException:
    #         assert False
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
    #
    # def test_purchase_behaviour_product_name_on_the_fly(self):
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
    #     audience_page.add_dataSource('Purchase Behavior')
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Product Name']").click()
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//an-typeahead").click()
    #     sleep(5)
    #     list = self.webdriver.find_elements_by_xpath("//an-typeahead/div/ul/li")
    #     p_name = ""
    #     for i in list:
    #         product_name= i.text
    #         if "category" in product_name:
    #             p_name= product_name
    #
    #     self.assertEqual(p_name, "", "Product names list contain category")
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()