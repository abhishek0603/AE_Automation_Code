from ..core.PageObject import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys


class ProjectPage(PageObject):
    # Define required page elements
    createNewProject            = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Create a new project']")))
    add_audience_button         = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".add-audience-btn")))
    CompareTrigger              = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".compare-trigger")))
    ProjectNameTextbox          = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Name Your Audience Project']")))
    SelectDataEnvironment       = lambda self: self.webdriver.find_element_by_xpath("//div[@class='an-dropdown-selected']")
    CreateButton                = lambda self: self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.submit()')]")
    cancelCreateProject         = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Cancel']")))
    ProjectName                 = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@class='project-name']/div")))
    AddAudienceButton           = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='add-audience-btn']")))
    AudienceNameTextBox         = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//*[@placeholder='Name Your Audience']")))
    SaveAudienceButton          = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save Audience']")))
    SaveAndBuildButton          = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Save and Build']")))
    AlertCancelButton           = lambda self: self.webdriver.find_element_by_xpath("//button[contains(text(),'Cancel')]")
    ClearSelectedButton         = lambda self: WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".clear-button")))
    download_button             = lambda self: WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='download-button']")))
    UploadTaxonomyBrowseButton  = lambda self: WebDriverWait(self.webdriver, 30).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='browse-button']")))
    TaxonomyName                = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Taxonomy Name']")))
    SetAsProjectDefault         = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Set as Project Default')]/preceding::input[1]")))
    SetTaxonomyButton           = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Set Taxonomy')]")))
    DeleteTaxonomyButton        = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Delete Taxonomy')]")))
    TaxonomyUploadButton        = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Upload')]")))
    SelectPrivateRadioButton    = lambda self: self.webdriver.find_element_by_xpath("//label[text()='Private']//preceding::input[1]")
    AddObjective                = lambda self: self.webdriver.find_element_by_xpath("//input[@placeholder='Add an Objective']")
    CpmRateOkButton             = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Ok')]")))
    DeleteProjOkButton          = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='an-primary-button ng-binding']")))
    AlertOkButton               = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'Ok')]")))
    HistoryTab                  = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[contains(text(),'History')]")))
    open_history                = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[@title='Open']")))
    close_history               = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//button[@title='Close']")))
    view_filters_knob           = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@class='knob']")))
    audience_back_arrow         = lambda self: self.webdriver.find_element_by_xpath("//button[@title='Back']")
    compare_button              = lambda self: self.webdriver.find_element_by_xpath("//div[contains(@class,'compare-button')]")
    DataSource                  = lambda self, data_Source_name: self.webdriver.find_element_by_xpath("//div[text()='" + data_Source_name + "']//preceding::input[1]")
    AudienceName                = lambda self, audience_name   : WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='" + audience_name + "']")))
    AudienceCheckbox            = lambda self, audience_name   : self.webdriver.find_element_by_xpath("//div[text()='" + audience_name +"']//preceding::input[1]")
    audience_menu_icon          = lambda self, audience_name   : WebDriverWait(self.webdriver, 150).until(EC.presence_of_element_located((By.XPATH,"//div[text()='" + audience_name + "']//following::div[1]")))
    audience_share_icon         = lambda self, audience_name   : self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']//following::div[contains(@class ,'distribute-button menu-panel-item')]")
    audience_delete_icon        = lambda self, audience_name   : self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']//following::div[contains(@class ,'delete-button menu-panel-item')]")
    audience_download_icon      = lambda self, audience_name   : self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']//following::div[contains(@class ,'download-button menu-panel-item')]")
    project_menu_icon           = lambda self, project_name    : WebDriverWait(self.webdriver, 200).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='" + project_name + "']//following::div[2]")))
    project_delete_icon         = lambda self, project_name    : self.webdriver.find_element_by_xpath("//div[text()='" + project_name + "']//following::div[contains(@class ,'delete-button menu-panel-item')]")
    Environment                 = lambda self, data_env        : WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='" + data_env + "']")))
    DistributionType            = lambda self, audience_name, distribution_name: self.webdriver.find_element_by_xpath("//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'" + distribution_name + "')]")
    audience_data               = lambda self, audience_name   : self.webdriver.find_element_by_xpath("//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'Audience Data')]")
    lbl_Audience_Explorer_omni  = lambda self: self.webdriver.find_element_by_xpath("//a [text()= 'Audience Explorer (Omni)']")
    bubble_Chart_Icon           = lambda self: self.webdriver.find_element_by_xpath("//button[@title='Bubble Chart']")
    selectProjectsDropdown      = lambda self: self.webdriver.find_element_by_xpath("//div[contains(@class,'dropdown-arrow')]")
    searchProjectsDropDown      = lambda self: self.webdriver.find_element_by_xpath("//*[@placeholder='Search for projects']")
    select_project              = lambda self, project_name: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[text()='" + project_name + "']")))

    def searchProjects(self,project_name):
        sleep(10)
        self.selectProjectsDropdown().click()
        self.searchProjectsDropDown().clear()
        self.searchProjectsDropDown().send_keys(Keys.HOME)
        self.searchProjectsDropDown().send_keys(project_name)
        sleep(10)
        self.select_project(project_name).click()
        sleep(10)
        projectName = self.ProjectName().text
        return projectName

    def verifyAudienceBackgroundColor(self,audience_name):
        color = self.webdriver.find_element_by_xpath("//div[text()='"+ audience_name +"']//ancestor::div[2]").value_of_css_property('background-color')
        return color

    def createProject(self, new_project_name, data_env):
        sleep(10)
        self.createNewProject().click()
        self.ProjectNameTextbox().send_keys(new_project_name)
        sleep(5)
        self.SelectDataEnvironment().click()
        sleep(5)
        self.Environment(data_env).click()
        self.CreateButton().click()
        sleep(15)
        projectName = self.ProjectName().text
        return projectName

    def createPrivateProject(self, new_project_name, objective, data_env):
        self.createNewProject().click()
        self.ProjectNameTextbox().send_keys(new_project_name)
        self.AddObjective().send_keys(objective)
        self.SelectPrivateRadioButton().click()
        self.SelectDataEnvironment().click()
        # sleep(10)
        self.Environment(data_env).click()
        self.CreateButton().click()
        sleep(15)
        projectName = self.ProjectName().text
        return projectName

    def verify_objective_field(self,new_project_name,data_env):
        self.createNewProject().click()
        self.ProjectNameTextbox().send_keys(new_project_name)
        for x in range(1, 43):
            self.AddObjective().send_keys("abc")
        obj = self.AddObjective().get_attribute('value')
        return len(obj)

    def click_upload_project_icon(self,project_name):
        WebDriverWait(self.webdriver, 200).until(EC.visibility_of_element_located(
            (By.XPATH, "//div[text()='" + project_name + "']//following::div[2]"))).click()
        self.webdriver.find_element_by_xpath(
            "//div[text()='" + project_name + "']//following::div[contains(@class ,'journey-taxonomy-form-button menu-panel-item')]").click()

    def deleteProject(self,project_name):
        self.project_menu_icon(project_name).click()
        self.project_delete_icon(project_name).click()
        self.AlertOkButton().click()

    def deleteAudience(self,audience_name):
        self.audience_delete_icon(audience_name).click()
        self.AlertOkButton().click()

    def select_datasource_visualization(self,visual_type):
        WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//form[@name='chartBase']/select[1]"))).click()
        self.webdriver.find_element_by_xpath("//option[@label='"+ visual_type + "']").click()
        sleep(5)

    def select_category(self,type):
        self.webdriver.find_element_by_xpath("//form[@name='chartBase']/select[2]").click()
        self.webdriver.find_element_by_xpath("//option[@label='" + type + "']").click()
        sleep(5)

    def select_subcategory(self,type):
        self.webdriver.find_element_by_xpath("//form[@name='chartBase']/select[3]").click()
        self.webdriver.find_element_by_xpath("//option[@label='" + type + "']").click()
        sleep(5)

    def selectAudiences(self,audience_name):
        self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']").click()
        self.bubble_Chart_Icon().click()
        sleep(5)
        individual = self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::span[contains(@class, 'id-count ng-binding')]").text
        print(individual)
        household = self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::span[contains(@class, 'hh-count ng-binding')]").text
        print(household)
        device = self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::span[contains(@class, 'device-count ng-binding')]").text
        print(device)
        return individual,household,device

    def audienceEditIcon(self,audience_name):
        sleep(5)
        self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']//following::div[contains(@class ,'edit-button menu-panel-item')]").click()

    def ConsumerJourney(self,audience_name):
        self.DistributionType(audience_name, "Consumer Journey").click()
        sleep(15)
        self.CpmRateOkButton().click()
        self.AlertOkButton().click()

    def ContentInspiration(self,audience_name):
        self.DistributionType(audience_name, "Content Inspiration").click()
        sleep(10)
        self.CpmRateOkButton().click()
        self.AlertOkButton().click()

    def DV360(self,audience_name):
        self.DistributionType(audience_name, "DV360").click()
        sleep(10)
        self.CpmRateOkButton().click()
        self.AlertOkButton().click()

    def DigitalContent(self,audience_name):
        self.DistributionType(audience_name, "Digital Content").click()
        sleep(10)
        self.AlertOkButton().click()

    def Facebook(self, audience_name):
        self.DistributionType(audience_name, "Facebook").click()
        sleep(10)
        self.CpmRateOkButton().click()
        self.AlertOkButton().click()

    def SemanticAudienceExplorer(self,audience_name):
        self.DistributionType(audience_name, "Semantic Audience Explorer").click()
        sleep(10)
        self.CpmRateOkButton().click()
        self.AlertOkButton().click()

    def TradeDesk(self,audience_name):
        self.DistributionType(audience_name, "Trade Desk").click()
        sleep(10)
        self.CpmRateOkButton().click()
        self.AlertOkButton().click()

    def TVContent(self,audience_name):
        self.DistributionType(audience_name, "TV Content").click()
        sleep(10)
        self.CpmRateOkButton().click()
        self.AlertOkButton().click()

    # def upload_new_taxonomy(self,path,taxonomy_name):
    #     self.TaxonomyName().send_keys(taxonomy_name)
    #     self.UploadTaxonomyBrowseButton().click()
    #     autoit.win_active("Open")
    #     sleep(5)
    #     autoit.control_send("Open", "Edit1", path)
    #     autoit.control_send("Open", "Edit1", "{ENTER}")
    #
    #     autoit.control_set_text("Open", "Edit1", path)
    #     self.UploadTaxonomyBrowseButton().click()
    #     self.UploadTaxonomyBrowseButton().send_keys(path)