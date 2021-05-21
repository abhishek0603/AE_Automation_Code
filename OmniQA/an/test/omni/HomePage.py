from ..core.PageObject import PageObject
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class HomePage(PageObject):
    # Define required page elements
    InsightLink             = lambda self: self.webdriver.find_element_by_xpath("//*[@class='omni-app-tiles']//div[text()='Insight']")
    PlanningLink            = lambda self: self.webdriver.find_element_by_xpath("//*[@class='omni-app-tiles']//div[text()='Planning']")
    ActivationLink          = lambda self: self.webdriver.find_element_by_xpath("//*[@class='omni-app-tiles']//div[text()='Activation']")
    OptimizationLink        = lambda self: self.webdriver.find_element_by_xpath("//*[@class='omni-app-tiles']//div[text()='Optimization']")
    WorkflowLink            = lambda self: self.webdriver.find_element_by_xpath("//*[@class='omni-app-tiles']//div[text()='Workflow']")
    InsightPopup            = lambda self: self.webdriver.find_element_by_xpath("//span/div[text()='Insight']")
    sidebarButton           = lambda self: WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH,"//*[@class='header_nav_btn']")))
    #sidebar links
    sb_AnnalectDMP          = lambda self: WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Annalect DMP']")))
    sb_AudienceExplorer     = lambda self: WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH,"//span[text()='Audience Explorer (Omni)']")))
    sb_ContentInspiration   = lambda self: self.webdriver.find_element_by_xpath("//span[text()='Content Inspiration']")
    sb_Attribution          = lambda self: self.webdriver.find_element_by_xpath("//span[text()='Attribution']")
    sb_TVContent            = lambda self: self.webdriver.find_element_by_xpath("//span[text()='TV Content']")
    sb_AudienceInsights     = lambda self: self.webdriver.find_element_by_xpath("//span[text()='Audience Insights']")
    sb_ChannelPlanner       = lambda self: self.webdriver.find_element_by_xpath("//span[text()='Channel Planner']")
    sb_Clients              = lambda self: self.webdriver.find_element_by_xpath("//a[text()='Clients']")
    sb_Intel                = lambda self: self.webdriver.find_element_by_xpath("//span[contains(text(),'Intel')]")
    sb_DataExplorer         = lambda self: self.webdriver.find_element_by_xpath("//span[text()='Data Explorer']")

    header_image            = lambda self: self.webdriver.find_element_by_xpath("//div[@class='header_title']/img")
    Omniring1               = lambda self: self.webdriver.find_element_by_xpath("//*[@id='omni-ring-1-section']")
    Omniring2               = lambda self: self.webdriver.find_element_by_xpath("//*[@id='omni-ring-2-section']")
    Omniring3               = lambda self: self.webdriver.find_element_by_xpath("//*[@id='omni-ring-3-section']")
    Omniring4               = lambda self: self.webdriver.find_element_by_xpath("//*[@id='omni-ring-4-section']")
    Omniring5               = lambda self: self.webdriver.find_element_by_xpath("//*[@id='omni-ring-5-section']")
    DataExplorerLink        = lambda self: self.webdriver.find_element_by_xpath("//*[@class='FlexContainer']//*[text()='Data Explorer']")
    AudienceProjSearch      = lambda self: WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH,"//input[@placeholder='Search for projects']")))
    Omnilogo                = lambda self: self.webdriver.find_element_by_xpath("//img[@class='omni-logo']")
    AppInsightABLink        = lambda self: WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH,"//*[text()='Audience Builder']")))
    settingsButton          = lambda self: WebDriverWait(self.webdriver, 100).until(EC.presence_of_element_located((By.XPATH,"//*[@title='Settings']")))


    def verifyHomePageApplicationLinks(self):
        sleep(20)
        self.InsightLink().click()
        sleep(10)
        self.PlanningLink().click()
        sleep(10)
        self.ActivationLink().click()
        sleep(10)
        self.OptimizationLink().click()
        sleep(10)
        self.WorkflowLink().click()

    def getOptimizationPage(self):
        sleep(5)
        self.OptimizationLink().click()

    def getDataExplorerPage(self):
        self.DataExplorerLink().click()

    def openSideBar(self):
        sleep(15)
        self.sidebarButton().click()

    def verifySideBarInsightLinks(self):
        sleep(10)
        self.sb_AudienceExplorer().click()

    def verifySideBarClients(self):
        sleep(5)
        self.sidebarButton().click()
        sleep(5)
        self.sb_Clients().click()
        sleep(5)
        self.sb_Intel().click()
        sleep(5)
        image_source = self.header_image().get_attribute("ng-src")
        return image_source

    def getClientList(self):
        sleep(5)
        self.sidebarButton().click()
        sleep(10)
        clients = ''
        temp = self.sb_Clients()
        temp1= temp.is_displayed()
        print(temp1)
        if temp1:
            self.sb_Clients().click()
            sleep(10)
            for elm in self.webdriver.find_elements_by_xpath("//span[contains(@class,'sidebar-client-name')]"):
                clients = clients + elm.text
            return clients
        else:
            return clients

    def verifySettingsLink(self):
        sleep(10)
        self.settingsButton().click()

    def cachingTest(self):
        sleep(10)
        self.webdriver.switch_to.default_content()
        self.sidebarButton().click()
        sleep(10)
        self.sb_AudienceExplorer().click()
        sleep(15)

        self.sidebarButton().click()
        sleep(10)
        self.sb_ContentInspiration().click()
        sleep(15)

        self.sidebarButton().click()
        sleep(10)
        self.sb_Attribution().click()
        sleep(15)

        self.sidebarButton().click()
        sleep(10)
        self.sb_TVContent().click()
        sleep(15)

        self.sidebarButton().click()
        sleep(10)
        self.sb_ChannelPlanner().click()
        sleep(15)

        self.Omnilogo().click()
        sleep(10)
        self.OptimizationLink().click()
        sleep(10)
        self.DataExplorerLink().click()
        sleep(10)
        self.DataExplorerLink().click()
