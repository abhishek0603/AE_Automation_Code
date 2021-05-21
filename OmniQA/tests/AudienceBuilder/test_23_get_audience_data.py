import json,os

from openpyxl.descriptors import Float
from selenium.webdriver import ActionChains

import tests
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from tests.AudienceBuilder import XLUtils


class conceptual_test(tests.SeleniumTest):
    def test_fetch_audience_data(self):
        project_name = self.configAB["Lotame_Viz"]["project_name"]
        path = os.path.join('testdata', 'sidebar.json')
        print("location:" + path)

        proj_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)
        home_page = HomePage(self.webdriver, self.config)

        with open(path) as file:
            data = json.load(file)
        for item in range(len(data)):
            link = data[item]["link"]
            # Project selection
            new_project_name = project_name + '_' + link
            print(new_project_name)
            sleep(5)
            home_page.searchProjects(new_project_name)
            sleep(10)
            num_aud_panel = len(self.webdriver.find_elements_by_xpath("//div[@class = 'audiences-section']//audience-panel"))
            print(num_aud_panel)
            for i in range (1,num_aud_panel+1):
                audience_name       = self.webdriver.find_element_by_xpath("(//div[@class = 'audience-title ng-binding'])[position()="+str(i)+"]").text
                individual_count    = self.webdriver.find_element_by_xpath("(//div[@class = 'audiences-section']//audience-panel//span[@class = 'id-count ng-binding'])[position()= "+str(i)+"]").text
                household_count     = self.webdriver.find_element_by_xpath("(//div[@class = 'audiences-section']//audience-panel//span[@class = 'hh-count ng-binding'])[position()= "+str(i)+"]").text
                device_count        = self.webdriver.find_element_by_xpath("(//div[@class = 'audiences-section']//audience-panel//span[@class = 'device-count ng-binding'])[position()= "+str(i)+"]").text
                print(individual_count)
                file_path = os.path.abspath("Datafile.xlsx")
                print(file_path)
                rows = XLUtils.getRowCount(file_path, "aud_data")
                print(rows)

                converted_indi          = audience_page.convert_str_to_number(individual_count)
                print(converted_indi)
                converted_house         = audience_page.convert_str_to_number(household_count)
                print(converted_house)
                converted_device        = audience_page.convert_str_to_number(device_count)
                print(converted_device)

                XLUtils.WriteData(file_path, "aud_data", rows + 1, 1, new_project_name)
                XLUtils.WriteData(file_path, "aud_data", rows + 1, 2, audience_name)

                #To get the number in human readable format for e.g 1000 to 1k
                # XLUtils.WriteData(file_path, "aud_data", rows+1, 3 , individual_count)
                # XLUtils.WriteData(file_path, "aud_data", rows+1, 4 , household_count)
                # XLUtils.WriteData(file_path, "aud_data", rows+1, 5 , device_count)


                #To get the number in long format for e.g 1k to 1000, 1M to 1000000
                XLUtils.WriteData(file_path, "aud_data", rows + 1, 3, converted_indi)
                XLUtils.WriteData(file_path, "aud_data", rows + 1, 4, converted_house)
                XLUtils.WriteData(file_path, "aud_data", rows + 1, 5, converted_device)

            sleep(10)
            # Navigating to home screen
            self.webdriver.switch_to_default_content()
            home_page.lbl_Audience_Explorer_omni().click()
            sleep(10)
            iframe = self.webdriver.find_elements_by_tag_name('iframe')[0]
            self.webdriver.switch_to.frame(iframe)








            # Audience Creation


