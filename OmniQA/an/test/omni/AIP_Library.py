from ..core.PageObject import PageObject, InvalidPageError
from ..core.Util import wait_until
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Library(PageObject):
    # Define required page elements
    DataExplorerApplication = lambda self: self.webdriver.find_element_by_xpath("//h2[@ng-bind='client.orgName' and text()='Data Explorer']")
    LoaderTab               = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Loader']")
    LibraryTab              = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Library']")
    JobsTab                 = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Jobs']")
    JobSearch               = lambda self: self.webdriver.find_element_by_xpath("//*[@title='Search for a saved Job']")
    GoButton                = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Go']")
    ActionDropDwn           = lambda self: self.webdriver.find_element_by_xpath("//*[@id='tab4']//div[1]/div[8]/select//*[text()='Run Job']")
    JobQOkbutton            = lambda self: self.webdriver.find_element_by_xpath("//*[@ng-repeat='button in buttons']")
    DatasetsTab             = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Datasets']")
    DatasetSearch           = lambda self: self.webdriver.find_element_by_xpath("//*[@title='Search for a saved Dataset']")
    ActionDropDwnDeleteDS   = lambda self: self.webdriver.find_element_by_xpath("//select/*[text()='Delete Dataset']")
    DeleteDSOKButton        = lambda self: self.webdriver.find_element_by_xpath("//*[@ng-repeat='button in buttons']")
    DataCatalogsTab         = lambda self: self.webdriver.find_element_by_xpath("//*[text()='Data Catalogs']")
    DataCatalogsSearch      = lambda self: self.webdriver.find_element_by_xpath("//*[@title='Search for a saved Catalog']")
    DeleteCatalogIcon       = lambda self: self.webdriver.find_element_by_xpath("//a[@title='Delete']")
    DeleteCatalogOKbutton   = lambda self: self.webdriver.find_element_by_xpath("//*[@id='show-message-dialog']/div[2]/button[1]")

    def _validate_page(self, webdriver):
        try:
            # check URL of the page
            ade_url = "%s#/library?tab=tab1" % self.config["ade_url"]
            if webdriver.current_url != ade_url:
                raise Exception("We are not on the ADE page")
        except Exception as e:
            error = e.message
            if not error and hasattr(e, "msg"):
                error = e.msg
            #raise InvalidPageError(error)


    def RunJob(self,jobname):
        self.JobsTab().click()
        sleep(10)
        try:
            self.JobSearch().clear()
            self.JobSearch().send_keys(jobname)
            sleep(10)
            self.ActionDropDwn().click()
            sleep(10)
            self.GoButton().click()
            sleep(10)
            self.JobQOkbutton().click()
            self.webdriver.refresh()
        except Exception as err:
            print('Job not found:'+jobname+'-Error Detail:'+ str(err))

    def DeleteDataset(self,dataset_name):
        self.DatasetsTab().click()
        sleep(10)

        for num in range(1,15):
            try:
                self.DatasetSearch().clear()
                self.DatasetSearch().send_keys(dataset_name)
                sleep(10)
                self.ActionDropDwnDeleteDS().click()
                #ActionDropDwnDeleteDS = self.ActionDropDwnDeleteDS()
                #ActionDropDwnDeleteDS.send_keys(Keys.CONTROL + Keys.HOME)
                sleep(10)
                self.GoButton().click()
                sleep(10)
                self.DeleteDSOKButton().click()
            except Exception as err:
                print('Dataset to be deleted not found:' + str(err))

    def DeleteCatalog(self,catalog_name):
        try:
            self.DataCatalogsTab().click()
            self.DataCatalogsSearch().send_keys(catalog_name)
            sleep(15)
            self.DeleteCatalogIcon().click()
            sleep(15)
            self.DeleteCatalogOKbutton().click()
            sleep(15)
        except Exception as err:
            print('Catalog to be deleted not found:' + str(err))