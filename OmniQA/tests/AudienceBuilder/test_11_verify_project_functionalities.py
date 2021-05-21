from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import tests,glob,os,xlrd
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.core.Util import my_random_string
from an.test.ab.LoginPage import LoginPage
from an.test.ab.AudiencePage import AudiencePage
from selenium.webdriver.support import expected_conditions as EC

class project_functionalities(tests.SeleniumTest):
    def test_search_projects(self):
        project_name  = self.configAB["SearchProjects"]["project_name"]

        home_page  = HomePage(self.webdriver,self.config)
        projectName = home_page.searchProjects(project_name)

        self.assertEqual(project_name, projectName, "Project Search failed")

    def test_create_public_project_on_project_page(self):
        project_name    = self.configAB["CreateProject"]["project_name"]
        data_env            = self.configAB["CreateProject"]["data_env"]

        home_page = HomePage(self.webdriver, self.config)
        proj_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        string = my_random_string(3)
        new_project_name = project_name + string
        project_name = proj_page.createProject(new_project_name, data_env)
        self.assertEqual(project_name,new_project_name,"Project creation failed")
        #     self.webdriver.quit()
        #     self.webdriver = webdriver.Chrome()
        #
        #     self.webdriver.maximize_window()
        #     self.webdriver.get(self.omni_url)
        #
        #     login_page = LoginPage(self.webdriver, self.config)
        #     login_page.login(shared_userid, shared_pwd)
        #
        #     sleep(5)
        #     home_page = HomePage(self.webdriver, self.config)
        #     home_page.openSideBar()
        #     WebDriverWait(self.webdriver, 100).until(
        #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
        #     sleep(5)
        #     iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        #     self.webdriver.switch_to_frame(iframe)
        #
        #
        #     home_page = HomePage(self.webdriver, self.config)
        #     home_page.searchProjects(new_project_name)

        proj_page.deleteProject(new_project_name)

    def test_create_private_project_on_project_page(self):
        project_name        = self.configAB["CreatePrivateProject"]["project_name"]
        objective           = self.configAB["CreatePrivateProject"]["objective"]
        data_env            = self.configAB["CreatePrivateProject"]["data_env"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        string = my_random_string(3)
        new_project_name = project_name + string

        proj_page = ProjectPage(self.webdriver,self.config)
        project_name = proj_page.createPrivateProject(new_project_name, objective, data_env)
        self.assertEqual(new_project_name,project_name,"Project creation failed")
        #     self.webdriver.quit()
        #     self.webdriver = webdriver.Chrome()
        #
        #     self.webdriver.maximize_window()
        #     self.webdriver.get(self.omni_url)
        #
        #     login_page = LoginPage(self.webdriver, self.config)
        #     login_page.login(shared_userid, shared_pwd)
        #
        #     sleep(5)
        #     home_page = HomePage(self.webdriver, self.config)
        #     home_page.openSideBar()
        #     WebDriverWait(self.webdriver, 100).until(
        #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
        #     sleep(5)
        #     iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        #     self.webdriver.switch_to_frame(iframe)
        #
        #
        #     home_page = HomePage(self.webdriver, self.config)
        #     home_page.searchProjects(new_project_name)
        proj_page.deleteProject(new_project_name)

    def test_create_project_objective_field(self):
        new_project_name = self.configAB["CreatePrivateProject"]["new_project_name"]
        data_env = self.configAB["CreatePrivateProject"]["data_env"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(new_project_name)
        string = my_random_string(3)
        new_project_name = new_project_name + string

        proj_page = ProjectPage(self.webdriver, self.config)
        length = proj_page.verify_objective_field(new_project_name, data_env)
        self.assertEqual(length, 120, "Objective field length limit incorrect")

    def test_edit_existing_project(self):
        project_name        = self.configAB["EditProject"]["project_name"]
        new_project_name    = self.configAB["EditProject"]["new_project_name"]

        home_page = HomePage(self.webdriver, self.config)
        proj_page = ProjectPage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        proj_name = home_page.edit_project_name(project_name,new_project_name)

        self.assertEqual(proj_name,new_project_name,"Edit Project failed")

        self.webdriver.back()

        self.webdriver.switch_to_default_content()
        proj_page.lbl_Audience_Explorer_omni().click()
        sleep(20)
        # WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
        # sleep(5)
        iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        self.webdriver.switch_to.frame(iframe)

        projectName = home_page.searchProjects(new_project_name)
        self.assertEqual(new_project_name, projectName, "Project Search failed")

        proj_name = home_page.edit_project_name(new_project_name, project_name)
        self.assertEqual(proj_name, project_name, "Edit Existing Project failed")

    def test_edit_new_project(self):
        project_name            = self.configAB["EditNewProject"]["project_name"]
        data_env                = self.configAB["EditNewProject"]["data_env"]
        new_project_name        = self.configAB["EditNewProject"]["new_project_name"]

        home_page = HomePage(self.webdriver, self.config)
        proj_page = ProjectPage(self.webdriver, self.config)

        home_page.createProject(project_name, data_env)

        proj_name = home_page.edit_project_name(project_name, new_project_name)

        self.assertEqual(proj_name, new_project_name, "Edit Project failed")

        self.webdriver.back()

        self.webdriver.switch_to_default_content()
        proj_page.lbl_Audience_Explorer_omni().click()
        sleep(20)
        # WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
        # sleep(5)
        iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        self.webdriver.switch_to.frame(iframe)

        projectName = home_page.searchProjects(new_project_name)
        self.assertEqual(new_project_name, projectName, "Project Search failed")

        proj_page.deleteProject(new_project_name)

    def test_html_capabilities_project_Search(self):
        new_project_name = self.configAB["html_capabilities_project_Search"]["project_name"]
        data_env         = self.configAB["html_capabilities_project_Search"]["data_env"]
        string           = my_random_string(3)
        for project in new_project_name.split(";"):
            proj = project + string
            home_page = HomePage(self.webdriver, self.config)
            proj_page = ProjectPage(self.webdriver, self.config)

            projectName = home_page.createProject(proj, data_env)

            self.assertEqual(projectName, proj, "Project with html tags not created")
            # sleep(5)
            # self.webdriver.refresh()
            # sleep(5)

            self.webdriver.back()

            self.webdriver.switch_to_default_content()
            proj_page.lbl_Audience_Explorer_omni().click()
            sleep(20)
            # WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
            # sleep(5)
            iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
            self.webdriver.switch_to.frame(iframe)

            home_page.searchProjects(proj)
            sleep(10)
            proj_page.deleteProject(proj)

    def test_public_project_other_user(self):
        rand = my_random_string(3)
        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        project_name = 'Test Proj' + rand
        print ("This is the project name created " + project_name)
        home_page.createProject(project_name, 'NA - United States')
        sleep(10)
        self.webdriver.switch_to_default_content()
        # actions = ActionChains(self.webdriver)
        # actions.move_to_element(project_page.img_profile()).perform()
        home_page.img_profile().click()
        sleep(5)
        home_page.link_signout().click()
        sleep(15)
        login_page = LoginPage(self.webdriver, self.config)
        login_page.login('ADMINQA.test', 'Welcome@321')
        sleep(15)
        WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='header_nav_btn']"))).click()
        sleep(5)
        WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
        sleep(5)
        iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        self.webdriver.switch_to.frame(iframe)
        home_page.searchProjects(project_name)
        project_page.project_menu_icon(project_name).click()
        home_page.project_edit_icon(project_name).click()
        # project_page.AddObjective().send_keys("Test 123")
        project_page.AddObjective().clear()
        project_page.AddObjective().send_keys('Test run time objective')
        sleep(5)
        audience_page.icon_greentick_objective().click()
        sleep(3)
        project_page.project_menu_icon(project_name).click()
        project_page.project_delete_icon(project_name).click()
        sleep(3)
        project_page.AlertOkButton().click()
        sleep(5)

    def test_project_objective_field(self):
        project_name      = self.configAB["Objective_Field_Test"]["project_name"]
        project_objective = self.configAB["Objective_Field_Test"]["objective"]
        # data_env = self.configAB["CreatePrivateProject"]["data_env"]

        home_page = HomePage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        project_page = ProjectPage(self.webdriver, self.config)
        project_page.project_menu_icon(project_name).click()
        home_page.project_edit_icon(project_name).click()
        # project_page.AddObjective().send_keys("Test 123")
        project_page.AddObjective().send_keys(project_objective)
        audience_page.icon_cross_objective().click()
        project_page.project_menu_icon(project_name).click()
        home_page.project_edit_icon(project_name).click()
        Prefilled_objective = audience_page.lbl_project_objective().text
        print("This is the prefilled value of objective " + Prefilled_objective)

    def test_audience_search_from_projectpage(self):
        project_name = self.configAB["SearchProjects"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        projectName = home_page.searchProjects(project_name)
        self.webdriver.find_element_by_xpath("//div[@class='dropdown-arrow']").click()
        self.webdriver.find_element_by_xpath("//*[@placeholder='Search for projects']").send_keys("DNT_Auto_Aud01")
        audience_selected = self.webdriver.find_element_by_xpath("//span[text()='DNT_Auto_Aud01']")
        audience_selected.click()
        print("Clicked on aud name")
        sleep(2)
        try:
            audience_selected.is_selected()
            print("Searched audiences got selected")
        except:
            print("Searched audiences did not get selected")

    # def test_edit_new_project_on_the_fly(self):
    #     rand = my_random_string(3)
    #     home_page = HomePage(self.webdriver, self.config)
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     # Project Creation
    #     home_page.createProject('Test Proj' + rand, 'NA - United States')
    #     sleep(10)
    #     # Editing created project
    #     project_name = 'Test Proj' + rand
    #     new_project_name = 'Test Proj' + rand + 'Edited'
    #     project_name = home_page.edit_project_name(project_name, new_project_name)
    #     self.assertEqual(project_name, new_project_name, "Edit Project failed")
    #     self.webdriver.back()
    #     self.webdriver.switch_to_default_content()
    #     project_page.lbl_Audience_Explorer_omni().click()
    #     sleep(20)
    #     # WebDriverWait(self.webdriver, 100).until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
    #     # sleep(5)
    #     iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
    #     self.webdriver.switch_to.frame(iframe)
    #     projectName = home_page.searchProjects(new_project_name)
    #     self.assertEqual(new_project_name, projectName, "Project Search failed")
    #     project_page.deleteProject(new_project_name)

