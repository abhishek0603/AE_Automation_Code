from ..core.PageObject import PageObject
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.common.keys import Keys


class HomePage(PageObject):
    # Define required page elements
    #searchProjectsDropDown       = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[@placeholder='Open An Audience Project']")))
    searchProjectsDropDown       = lambda self: self.webdriver.find_element_by_xpath("//*[@placeholder='Open An Audience Project']")
    GoButton                     = lambda self: self.webdriver.find_element_by_xpath("//button[@class='oval']")
    createNewProject             = lambda self: WebDriverWait(self.webdriver, 150).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Create a new project']")))
    ProjectNameTextbox           = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Name Your Audience Project']")))
    txt_Project_objective        = lambda self: self.webdriver.find_element_by_xpath("//input[@placeholder = 'Add an Objective']")
    SelectDataEnvironment        = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//dropdown")))
    CreateButton                 = lambda self: self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.submit()')]")
    CancelButton                 = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Cancel']")))
    ProjectName                  = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//*[@class='project-name']/div")))
    EditProjectButton            = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH,"//div[@class='edit-project-btn']")))
    EditSuccessButton            = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success-btn']")))
    EditCancelButton             = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cancel-btn']")))
    EditProjectTextBox           = lambda self: WebDriverWait(self.webdriver, 50).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success-btn']/preceding::input[1]")))
    cog_button                   = lambda self: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='cog-icon-btn ng-scope']")))
    link_signout                 = lambda self: self.webdriver.find_element_by_xpath("//a[text() = 'Sign Out']")
    img_profile                  = lambda self: self.webdriver.find_element_by_xpath("//button[@class = 'profile-tool-section']")
    lbl_Audience_Explorer_omni   = lambda self: self.webdriver.find_element_by_xpath("//a [text()= 'Audience Explorer (Omni)']")
    drp_admin_project            = lambda self: self.webdriver.find_element_by_xpath("//label/select")
    btn_back_admin_page          = lambda self: self.webdriver.find_element_by_xpath("//button[@class= 'btn btn-default']")
    chk_admin_audience_setting   = lambda self: self.webdriver.find_element_by_xpath("//*[contains(@value,'Export')]")

    Environment                  = lambda self, data_env    : WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH, "//div[text()='" + data_env + "']")))
    project_menu_icon            = lambda self, project_name: WebDriverWait(self.webdriver, 200).until(EC.visibility_of_element_located((By.XPATH,"//div[text()='" + project_name + "']//following::div[2]")))
    project_edit_icon            = lambda self, project_name: self.webdriver.find_element_by_xpath("//div[text()='" + project_name + "']//following::div[contains(@class ,'edit-button menu-panel-item')]")
    select_project               = lambda self, project_name: WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//*[text()='"+ project_name+"']")))

    def searchProjects(self,project_name):
        sleep(10)
        self.searchProjectsDropDown().clear()
        self.searchProjectsDropDown().send_keys(Keys.HOME)
        self.searchProjectsDropDown().send_keys(project_name)
        sleep(10)
        self.select_project(project_name).click()
        sleep(10)
        projectName = self.ProjectName().text
        return projectName

    def createProject(self,new_project_name,data_env):
        sleep(15)
        self.createNewProject().click()
        self.ProjectNameTextbox().send_keys(new_project_name)
        sleep(5)
        self.txt_Project_objective().send_keys('Test Project Objective')
        sleep(5)
        self.SelectDataEnvironment().click()
        self.Environment(data_env).click()
        self.CreateButton().click()
        sleep(10)
        projectName = self.ProjectName().text
        return projectName

    def edit_project_name(self,project_name,new_project_name):
        self.project_menu_icon(project_name).click()
        self.project_edit_icon(project_name).click()

        self.EditProjectTextBox().clear()
        self.EditProjectTextBox().send_keys(new_project_name)
        self.EditSuccessButton().click()
        sleep(15)
        proj_name= self.ProjectName().text
        return proj_name