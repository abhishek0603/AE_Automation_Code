from ..core.PageObject import PageObject
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


class AudiencePage(PageObject):
    audience_name_textbox    = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Name Your Audience']")))
    save_audience_button     = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Save Audience']")))
    save_and_build_button    = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Save and Build']")))
    save_and_create_button   = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Save and Create']")))
    inner_criteria_plusIcon  = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.CLASS_NAME, "plus")))
    add_dataSource_plusIcon  = lambda self: WebDriverWait(self.webdriver, 150).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Add a Data Source']/following::div")))
    datasource_type          = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Demographic Data']")))
    add_criteria_plusicon    = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@ng-click,'criteriaAdd')]")))
    filter_col_dropdown      = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//select[contains(@ng-model,'criteriaColumnSelector')]")))
    criteria_createButton    = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "(//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")))
    aud_back_arrow           = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='back']")))
    get_time_period          = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='criteria-group']/div[2]/div[1]")))
    click_edit_time_period   = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='criteria-group']/div[2]/div[2]")))
    icon_greentick_objective = lambda self: self.webdriver.find_element_by_xpath("//div[@class ='success-btn']")
    lbl_individuals          = lambda self, aud_name: self.webdriver.find_element_by_xpath("//div[text()='" + aud_name + "']//following::span[contains(@ng-bind, 'audience.idCount')]")
    lbl_household            = lambda self, aud_name: self.webdriver.find_element_by_xpath("//div[text()='" + aud_name + "']//following::span[contains(@ng-bind, 'audience.hhCount')]")
    lbl_devices              = lambda self, aud_name: self.webdriver.find_element_by_xpath("//div[text()='" + aud_name + "']//following::span[contains(@ng-bind, 'audience.deviceCount')]")
    lbl_date_time            = lambda self: self.webdriver.find_element_by_xpath("//div[contains(@class,'edit-when ng-scope')]//following::span[1]")
    lbl_User                 = lambda self: self.webdriver.find_element_by_xpath("//div[contains(@class,'edit-when ng-scope')]//following::span[2]")
    lbl_data_env             = lambda self: self.webdriver.find_element_by_xpath("//div[contains(@class,'edit-when ng-scope')]//following::span[3]")
    Time_Period              = lambda self: self.webdriver.find_element_by_xpath("//div[contains(@class,'text ng-binding')and contains(@ng-bind, 'TimePeriods')]")
    Time_Period_Edit         = lambda self: self.webdriver.find_element_by_xpath("//div[contains(@class,'edit') and contains(@ng-click, 'timePeriodSelect')]")
    drp_Quarter              = lambda self: self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'selectedTimePeriodsNew')]")
    btn_quarter_create       = lambda self: self.webdriver.find_element_by_xpath("//button[contains(@ng-disabled,'canCreateCriteria') and contains(text() , 'Create')]")
    icon_cross_objective     = lambda self: self.webdriver.find_element_by_xpath("//div[@class ='cancel-btn']")
    lbl_project_objective    = lambda self: self.webdriver.find_element_by_xpath("//p[@class='ng-binding']")
    select_ds_type           = lambda self, ds_type: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'data-source')]/div[text()='" + ds_type + "']")))
    lbl_PanelIndividuals     = lambda self, aud_name: self.webdriver.find_element_by_xpath("//div[contains(@class,'audience-title') and contains(text(),'" + aud_name + "')]//following::span[contains(@class, 'id-count ng-binding')]")
    lbl_PanelDevice          = lambda self, aud_name: self.webdriver.find_element_by_xpath("//div[contains(@class,'audience-title') and contains(text(),'" + aud_name + "')]//following::span[contains(@class, 'device-count ng-binding')]")
    lbl_PanelHousehold       = lambda self, aud_name: self.webdriver.find_element_by_xpath("//div[contains(@class,'audience-title') and contains(text(),'" + aud_name + "')]//following::span[contains(@class, 'hh-count ng-binding')]")



    def audience_rename(self,new_audience_name):
        self.audience_name_textbox().clear()
        self.audience_name_textbox().send_keys(new_audience_name)
        sleep(10)
        self.save_audience_button().click()

    def add_dataSource(self, ds_type):
        self.add_dataSource_plusIcon().click()
        self.select_ds_type(ds_type).click()
        sleep(10)
        return ds_type

    def check_advance_age(self):
        self.webdriver.find_element_by_xpath("//span[text()='Attributes by Category']/following::select").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//option[text()='Demographic']").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//span[text()='Attribute Subcategories']/following::select[1]").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//option[text()='Age']").click()
        sleep(5)
        age_list = self.webdriver.find_element_by_xpath("//span[text() = 'Attribute']/following::select[contains(@ng-model,'control.value')]").text
        return age_list

    def age_slider(self):
        sleep(5)
        # slider_target_left = self.webdriver.find_element_by_xpath("//span[contains(@class,'ui-slider-handle') and contains(@style ,'left: 34.1463%;')]")
        left = self.webdriver.find_element_by_xpath("//span[contains(@class,'ui-slider-handle')]")
        # ActionChains(self.webdriver).drag_and_drop_by_offset(left, 40, 0).perform()
        ActionChains(self.webdriver).click_and_hold(left).move_by_offset(90,0).release().perform()
        # ActionChains(self.webdriver).drag_and_drop(left, slider_target_left)
        right = self.webdriver.find_element_by_xpath("//span[contains(@class,'ui-slider-handle')][2]")
        # slider_target_right = self.webdriver.find_element_by_xpath("//span[contains(@class,'ui-slider-handle') and contains(@style ,'left: 53.6585%;')][2]")
        # ActionChains(self.webdriver).drag_and_drop_by_offset(right, -25, 0).perform()
        ActionChains(self.webdriver).click_and_hold(right).move_by_offset(-120,0).release().perform()
        # ActionChains(self.webdriver).drag_and_drop(right,slider_target_right)



    def copy_audience_criteria_within_self(self,data_source):
        sleep(10)
        self.webdriver.find_element_by_xpath("//div[text()='" + data_source + "']/following-sibling::div/div[2]").click()

    def delete_audience_criteria(self,data_source):
        self.webdriver.find_element_by_xpath("//div[text()='" + data_source + "']/following-sibling::div/div[1]").click()
        sleep(10)
        WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Ok')]"))).click()
        sleep(5)

    def copy_multiple_audience_criteria_within_self(self):
        sleep(5)
        self.webdriver.find_element_by_xpath("//img[@src='/static/img/copy-white.png']").click()
        sleep(10)

    def click_parenthesis_icon(self):
        self.webdriver.find_element_by_xpath("//div[@title='To apply, click to multi-select the criteria or source groups you want to parenthesize. Then click this icon.']").click()
        sleep(10)

    def create_advanced_audience_data_criteria(self, type, category, name, value):
        # self.webdriver.find_element_by_xpath("//span[text()='Attributes by Type']/following::select").click()
        # sleep(10)
        self.webdriver.find_element_by_xpath("//span[text()='Attributes by Type']/following::select//option[text()='" + type + "']").click()
        # self.webdriver.find_element_by_xpath("//option[text()='" + attr_type + "']").click()
        # self.webdriver.find_element_by_xpath("//span[text()='Attributes by Type']/following::select").click()
        sleep(10)


        # self.webdriver.find_element_by_xpath("//span[text()='Attribute By Category']/following::select").click()
        # sleep(10)
        self.webdriver.find_element_by_xpath("//span[text()='Attribute By Category']/following::select//option[text()='" + category + "']").click()
        # self.webdriver.find_element_by_xpath("//option[contains(text(),'" + category + "')]").click()
        # self.webdriver.find_element_by_xpath("//span[text()='Attribute By Category']/following::select").click()
        sleep(10)

        # self.webdriver.find_element_by_xpath("//span[text()='Attribute Name']/following::select").click()
        # sleep(10)
        self.webdriver.find_element_by_xpath("//span[text()='Attribute Name']/following::select//option[text()='" + name + "']").click()
        # self.webdriver.find_element_by_xpath("//span[text()='Attribute Name']/following::select").click()
        # criteria_text = self.webdriver.find_element_by_xpath("//span[text()='Attribute Name']/following::select").click()
        # self.webdriver.execute_script("arguments[0].click();", criteria_text)
        sleep(10)

        self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").send_keys(value)
        sleep(10)
        self.webdriver.find_element_by_xpath("//li[contains(text(),'" + value + "')]").click()

        # self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']//following::li[contains(text(), '" + value + "')]").click()
        # criteria_text = self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']")
        # self.webdriver.execute_script("arguments[0].click();", criteria_text)
        # criteria_text.send_keys(value)
        # criteria_value = self.webdriver.find_element_by_xpath("//li[contains(text(),'" + value + "')]")
        # self.webdriver.execute_script("arguments[0].click();", criteria_value)
        # WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + value + "')]"))).click()
        sleep(5)
        criteria_createButton = self.webdriver.find_element_by_xpath(
            "//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)
        # audience_page.criteria_createButton().click()
        sleep(5)

    def create_advanced_audience_data_criteria_multiple_attribute_value(self, attr_type, category, name, value):
        self.webdriver.find_element_by_xpath("//span[text()='Attributes by Type']/following::select").click()
        self.webdriver.find_element_by_xpath("//option[text()='" + attr_type + "']").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//span[text()='Attribute By Category']/following::select").click()
        self.webdriver.find_element_by_xpath("//option[contains(text(),'" + category + "')]").click()

        sleep(5)
        self.webdriver.find_element_by_xpath("//span[text()='Attribute Name']/following::select").click()
        self.webdriver.find_element_by_xpath("//option[contains(text(),'" + name + "')]").click()
        sleep(5)
        self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").click()
        for item in value:
            WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + item + "')]"))).click()

        self.webdriver.find_element_by_xpath("//div[contains(@title,'To apply,')]").click()
        self.criteria_createButton().click()

    # def create_browsing_behaviour_domain_categories(self, category, sub_category):
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Categories']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'control.value')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='" + category + "']").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").click()
    #     WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + sub_category + "')]"))).click()
    #
    #     self.criteria_createButton().click()
    #
    # def create_browsing_behaviour_domain_categories_single_sub_category(self, category, sub_category):
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Categories']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'control.value')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='" + category + "']").click()
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//span[text()='Domain Sub-Categories']/following::select").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='" + sub_category + "']").click()
    #
    #     self.criteria_createButton().click()
    #
    # def create_browsing_behaviour_domain_categories_multiple_sub_category(self, category, sub_category):
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Categories']").click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'control.value')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='" + category + "']").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").click()
    #     for item in sub_category:
    #         WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + item + "')]"))).click()
    #
    #     self.criteria_createButton().click()
    #
    # def create_browsing_behaviour_domain_names(self,name):
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Names']").click()
    #
    #     # self.webdriver.find_element_by_xpath("//div[contains(@title,'To apply,')]").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").send_keys(name)
    #     sleep(5)
    #     WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + name + "')]"))).click()
    #
    #     self.criteria_createButton().click()
    #
    # def create_browsing_behaviour_domain_names_multiple(self,name1,name2):
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Names']").click()
    #
    #     # self.webdriver.find_element_by_xpath("//div[contains(@title,'To apply,')]").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").send_keys(name1)
    #     sleep(5)
    #     WebDriverWait(self.webdriver, 50).until(
    #         EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + name1 + "')]"))).click()
    #
    #     self.criteria_createButton().click()
    #     self.add_criteria_plusicon().click()
    #     self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
    #     self.webdriver.find_element_by_xpath("//option[text()='Domain Names']").click()
    #
    #     # self.webdriver.find_element_by_xpath("//div[contains(@title,'To apply,')]").click()
    #     self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").send_keys(name2)
    #     sleep(5)
    #     WebDriverWait(self.webdriver, 50).until(
    #         EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + name2 + "')]"))).click()
    #
    #     self.criteria_createButton().click()

    def create_location_data_state(self,column, state):
        # self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]").click()
        # self.webdriver.find_element_by_xpath("//option[text()='State']").click()
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]//following::option[text()='" + column + "']").click()


        # self.webdriver.find_element_by_xpath("//div[contains(@title,'To apply,')]").click()
        self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").send_keys(state)
        sleep(5)
        WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'" + state + "')]"))).click()
        sleep(5)
        criteria_createButton = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)

    def create_purchase_data_criteria(self,column, category):
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]//following::option[text()='" + column + "']").click()
        sleep(10)
        self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").send_keys(category)
        sleep(10)
        self.webdriver.find_element_by_xpath("//li[contains(text(),'" + category + "')]").click()
        sleep(5)
        criteria_createButton = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)

    def create_demographic_data_criteria(self,column):
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]//following::option[text()='" + column + "']").click()
        sleep(5)
        self.age_slider()
        sleep(5)
        criteria_createButton = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)

    def create_TV_viewership_data_criteria(self,column, category):
        self.webdriver.find_element_by_xpath("//select[contains(@ng-model,'criteriaColumnSelector')]//following::option[text()='" + column + "']").click()
        sleep(10)
        self.webdriver.find_element_by_xpath("//input[@placeholder ='Begin typing to search...']").send_keys(category)
        sleep(10)
        self.webdriver.find_element_by_xpath("//li[contains(text(),'" + category + "')]").click()
        sleep(5)
        criteria_createButton = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.criteriaApply()') and (@class='red-btn')]")
        self.webdriver.execute_script("arguments[0].click();", criteria_createButton)

    def convert_str_to_number(self,x):
        num = 0
        last_str = x[-1]
        rem_str = x[:-1]
        print(last_str)
        if(last_str == 'K'):
            num = float(rem_str) * 1000
            print(num)
        elif(last_str=='M'):
            num = float(rem_str) * 1000000
            print(num)
        elif(last_str=='B'):
            num = float(rem_str) * 1000000000
            print(num)
        else:
            print("number is neither in K nor in M")
        return num







