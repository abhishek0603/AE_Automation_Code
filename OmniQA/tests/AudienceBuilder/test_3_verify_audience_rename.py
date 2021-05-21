import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from time import sleep

class audience_rename(tests.SeleniumTest):
    def test_existingAudience_rename(self):
        section = self.__class__.__name__
        project_name        = self.configAB[section]["project_name"]
        audience_name       = self.configAB[section]["audience_name"]
        new_audience_name   = self.configAB[section]["new_audience_name"]

        home_page = HomePage(self.webdriver,self.config)
        self.webdriver.switch_to_default_content()
        home_page.lbl_Audience_Explorer_omni().click()
        sleep(20)
        iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
        self.webdriver.switch_to.frame(iframe)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        try:
            project_page.audience_menu_icon(audience_name).click()
            project_page.audienceEditIcon(audience_name)

            audience_page = AudiencePage(self.webdriver, self.config)
            audience_page.audience_rename(new_audience_name)

            project_page.AudienceName(new_audience_name).click()

            #again renaming it back to original
            project_page.audience_menu_icon(new_audience_name).click()
            project_page.audienceEditIcon(new_audience_name)

            audience_page = AudiencePage(self.webdriver, self.config)
            audience_page.audience_rename(audience_name)

            project_page.AudienceName(audience_name).click()
        except:
            project_page.audience_menu_icon(new_audience_name).click()
            project_page.audienceEditIcon(new_audience_name)

            audience_page = AudiencePage(self.webdriver, self.config)
            audience_page.audience_rename(audience_name)

            project_page.AudienceName(audience_name).click()