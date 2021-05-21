import tests
from time import sleep
from an.test.omni.HomePage import HomePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import json,os

class SidebarLinksTest(tests.OmniSeleniumTest):
    def test_sidebarjson(self):
        path = os.path.join('testdata', 'sidebar.json')
        print("location:" + path)
        home_page = HomePage(self.webdriver, self.config)
        with open(path) as file:
            data = json.load(file)
        for item in range(len(data)):
            link = data[item]["link"]
            try:
                home_page.openSideBar()
                sleep(10)
                WebDriverWait(self.webdriver, 30).until(
                    EC.visibility_of_element_located((By.XPATH, "//span[text()='"+ link +"']"))).click()
                sleep(5)
            except:
                print("Side bar link:\""+ link+" \"not found")
                self.webdriver.refresh()

    # def test_SideBar_Insights_Link_verify(self):
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.openSideBar()
    #     sleep(10)
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Lotame)']"))).click()
    #     sleep(15)
    #     home_page.openSideBar()
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Neustar)']"))).click()
    #     sleep(15)
    #     home_page.openSideBar()
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Omni)']"))).click()
    #     sleep(15)
    #     home_page.openSideBar()
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Content Inspiration']"))).click()
    #     sleep(15)
    #     home_page.openSideBar()
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Audience Explorer (Semantic EU)']"))).click()
    #     sleep(15)
    #     home_page.openSideBar()
    #
    # def test_SideBar_Planning_Link_verify(self):
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.openSideBar()
    #     sleep(10)
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Channel Planner: Sandbox']"))).click()
    #     sleep(15)
    #     home_page.openSideBar()
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Investment Planner: Sandbox']"))).click()
    #
    #
    # def test_SideBar_Optimization_Link_verify(self):
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.openSideBar()
    #     sleep(10)
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Data Explorer']"))).click()
    #
    #
    # def test_SideBar_Workflow_Link_verify(self):
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.openSideBar()
    #     sleep(10)
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='PHD Source']"))).click()
    #
    #
    # def test_SideBar_Support_Link_verify(self):
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.openSideBar()
    #     sleep(10)
    #     WebDriverWait(self.webdriver, 100).until(
    #         EC.visibility_of_element_located((By.XPATH, "//span[text()='Taxonomy Builder']"))).click()
