import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime,date
from time import sleep
import pandas as pd


class others(tests.SeleniumTest):

    def test_get_individuals(self):
        project_name = self.configAB["Conceptual"]["project_name"]
        today = datetime.today().strftime('%m%d%y')
        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        sleep(10)
        aud_name = []
        individual_count = []
        aud_list = self.webdriver.find_elements_by_xpath("//div[contains(@class ,'audience-title')]")
        for aud in aud_list:
            name = str(aud.text)
            aud_name.append(name)

        aud_list = self.webdriver.find_elements_by_xpath("//div[contains(@class ,'audience-title')]/following::div[@class='audience-info-item'][1]/div")
        for aud in aud_list:
            count = str(aud.text)
            individual_count.append(count)

        df = pd.DataFrame()
        df['aud_names'] = aud_name
        df['individual_count']  = individual_count
        print(df)
        # with pd.ExcelWriter('./aud_list_{0}.xlsx'.format(today)) as writer:
        #     df.to_excel(writer, sheet_name='Defect Detail', index=False)

        # print(dict(zip(aud_name, individual_count)))

    def test_content_inspiration(self):
        project_name = self.configAB["Conceptual"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)
        project_page = ProjectPage(self.webdriver, self.config)
        aud_list = self.webdriver.find_elements_by_xpath("//div[contains(@class ,'audience-title')]")

        for aud in aud_list:
            audience_name = str(aud.text)
            try:
                project_page.audience_menu_icon(audience_name).click()
                project_page.audience_share_icon(audience_name).click()
                project_page.ContentInspiration(audience_name)
            except Exception as e:
                print(audience_name, e)

        aud_name = []
        individual_count = []
        aud_list = self.webdriver.find_elements_by_xpath("//div[contains(@class ,'audience-title')]")
        for aud in aud_list:
            name = str(aud.text)
            aud_name.append(name)

        aud_list = self.webdriver.find_elements_by_xpath("//div[contains(@class ,'audience-title')]/following::div[@class='audience-info-item'][1]/div")
        for aud in aud_list:
            count = str(aud.text)
            individual_count.append(count)

        df = pd.DataFrame()
        df['aud_names'] = aud_name
        df['individual_count'] = individual_count
        print(df)

    def test_consumer_journey(self):
        # project_name = self.configAB["Conceptual"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects('Argentina 07-08')
        project_page = ProjectPage(self.webdriver, self.config)
        aud_list = self.webdriver.find_elements_by_xpath("//div[contains(@class ,'audience-title')]")

        for aud in aud_list:
            audience_name = str(aud.text)
            try:
                project_page.audience_menu_icon(audience_name).click()
                project_page.audience_share_icon(audience_name).click()
                project_page.ConsumerJourney(audience_name)
            except Exception as e:
                print(audience_name, e)

    def test_save_and_create_all_aud(self):
        # project_name = self.configAB["Conceptual"]["project_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects('Lotame_Switzerland_30-08-2019')
        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        sleep(5)
        aud_name_list = []
        aud_list = WebDriverWait(self.webdriver, 100).until(EC.presence_of_all_elements_located((By.XPATH,"//div[contains(@class ,'audience-title')]")))
        for aud in aud_list:
            audience_name = str(aud.text)
            aud_name_list.append(audience_name)


        for aud_name in aud_name_list:
            try:
                sleep(5)
                project_page.audience_menu_icon(aud_name).click()
                project_page.audienceEditIcon(aud_name)
            except Exception as e:
                print(aud_name, e)
                continue
            try:
                sleep(5)
                audience_page.save_and_create_button().click()
            except Exception as e:
                print(aud_name, e)
                audience_page.aud_back_arrow().click()