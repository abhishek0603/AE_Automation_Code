import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from an.test.core.Util import my_random_string

class cpm_rate(tests.SeleniumTest):
    def test_dv360_rate_card(self):
        section = self.__class__.__name__
        project_name = self.configAB["cpm_rate"]["project_name"]
        audience_name = self.configAB["cpm_rate"]["audience_name"]
        #Click on DV360
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audience_share_icon(audience_name).click()
        self.webdriver.find_element_by_xpath(
            "//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'DV360')]").click()

        rate = WebDriverWait(self.webdriver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//table[@class='rate-card-table']/tbody/tr/th/span"))).text
        self.assertEqual(rate, "$1.05", "DV360 Ratecard Incorrect")
        # self.webdriver.find_element_by_xpath("// button[text() = 'Cancel']").click()

    def test_facebook_rate_card(self):
        section = self.__class__.__name__
        project_name = self.configAB["cpm_rate"]["project_name"]
        audience_name = self.configAB["cpm_rate"]["audience_name"]
        #Click on Facebook
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audience_share_icon(audience_name).click()
        self.webdriver.find_element_by_xpath(
            "//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'Facebook')]").click()

        rate = WebDriverWait(self.webdriver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//table[@class='rate-card-table']/tbody/tr/th/span"))).text
        self.assertEqual(rate, "$1.05", "Facebook Ratecard Incorrect")
        # self.webdriver.find_element_by_xpath("// button[text() = 'Cancel']").click()

    def test_tradedesk_rate_card(self):
        section = self.__class__.__name__
        project_name = self.configAB["cpm_rate"]["project_name"]
        audience_name = self.configAB["cpm_rate"]["audience_name"]
        #Click on Tradedesk
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audience_share_icon(audience_name).click()
        self.webdriver.find_element_by_xpath(
            "//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'Trade Desk')]").click()

        rate = WebDriverWait(self.webdriver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//table[@class='rate-card-table']/tbody/tr/th/span"))).text
        self.assertEqual(rate, "$1.05", "Trade desk Ratecard Incorrect")
        # self.webdriver.find_element_by_xpath("// button[text() = 'Cancel']").click()

    def test_verify_activation_rate_on_copy_criteria(self):
        section = self.__class__.__name__
        project_name_act_rate        = self.configAB["cpm_rate"]["project_name_act_rate"]
        source_audience_name  = self.configAB["cpm_rate"]["source_audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name_act_rate)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(source_audience_name).click()
        project_page.audienceEditIcon(source_audience_name)

        audience_page = AudiencePage(self.webdriver, self.config)

        activation_rate1 =  WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(@class,'cost')]"))).text
        audience_page.copy_audience_criteria_within_self("Location Data")
        self.webdriver.find_element_by_xpath("//div[@class='sources-panel']/div[1]").click()

        #Opening criteria builder page
        project_page.AddAudienceButton().click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']").click()

        activation_rate2 = WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(@class,'cost')]"))).text

        self.assertEqual(activation_rate1,activation_rate2,'Activation rate differ after copy')
        audience_page.aud_back_arrow().click()

    def test_verify_activation_rate_and_CPM_value(self):
        section = self.__class__.__name__
        project_name = self.configAB["cpm_rate"]["project_name"]
        audience_name = self.configAB["cpm_rate"]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)

        home_page.searchProjects(project_name)

        project_page.audience_menu_icon(audience_name).click()
        project_page.audience_share_icon(audience_name).click()
        self.webdriver.find_element_by_xpath(
            "//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'Trade Desk')]").click()
        CPM_rate = WebDriverWait(self.webdriver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//table[@class='rate-card-table']/tbody/tr/th/span"))).text
        print(CPM_rate)
        self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'btn.onClick()')]//following::span[text()='Cancel']").click()

        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        activation_rate = WebDriverWait(self.webdriver, 50).until(
            EC.visibility_of_element_located((By.XPATH, "//span[contains(@class,'cost')]"))).text
        print(activation_rate)

        self.assertEqual(activation_rate, CPM_rate, 'Activation rate & CPM rate is not same')
        audience_page.aud_back_arrow().click()

    # def test_SemanticAudienceExplorer_rate_card(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB["cpm_rate"]["project_name"]
    #     audience_name = self.configAB["cpm_rate"]["audience_name"]
    #     # click on semantic explorer
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     self.webdriver.find_element_by_xpath(
    #         "//*[text()='" + audience_name + "']/following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'Semantic Audience Explorer')]").click()
    #
    #     rate = WebDriverWait(self.webdriver, 50).until(
    #         EC.visibility_of_element_located((By.XPATH, "//table[@class='rate-card-table']/tbody/tr/th/span"))).text
    #     self.assertEqual(rate, "$0.65", "Semantic Audience Explorer Ratecard Incorrect")

    # def test_verify_activation_rate_on_copy_criteria_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     audience_page = AudiencePage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Adding Criteria
    #     project_page.add_audience_button().click()
    #     audience_page.audience_name_textbox().send_keys('Test Audience1')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('facebook.com')
    #     audience_page.add_dataSource('Browsing Behavior')
    #     audience_page.create_browsing_behaviour_domain_names('instagram.com')
    #     copy_multiple_criteria_button = self.webdriver.find_element_by_xpath("//img[@src='/static/img/copy-white.png']")
    #     self.webdriver.execute_script("arguments[0].click();", copy_multiple_criteria_button)
    #     activation_rate1 =  WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(@class,'cost')]"))).text
    #     audience_page.aud_back_arrow().click()
    #     # Opening criteria builder page
    #     project_page.add_audience_button().click()
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='Insert Copied Criteria']").click()
    #     activation_rate2 = WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//span[contains(@class,'cost')]"))).text
    #     self.assertEqual(activation_rate1,activation_rate2,'Activation rate differ after copy')
    #     # Deleting Criteria and Project
    #     audience_page.aud_back_arrow().click()
    #     project_page.project_menu_icon('Test Proj' + rand).click()
    #     project_page.project_delete_icon('Test Proj' + rand).click()
    #     project_page.AlertOkButton().click()
