import tests
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.ab.AudiencePage import AudiencePage
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

class viz_icon_tooltip(tests.SeleniumTest):
    def test_infoviz_icon_existing_audience(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page  = HomePage(self.webdriver,self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        sleep(15)
        project_page.AudienceName(audience_name).click()

        info_Viz_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Audience Profile')]")
        info_Viz_title = info_Viz_Icon.get_attribute("title")
        print(info_Viz_title)
        ActionChains(self.webdriver).move_to_element(info_Viz_Icon).perform()
        self.assertEqual("Audience Profile", info_Viz_title)

    def test_bubblechart_icon_existing_audience(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page  = HomePage(self.webdriver,self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()

        bubble_chart_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Bubble Chart')]")
        bubble_chart_title = bubble_chart_Icon.get_attribute("title")
        print(bubble_chart_title)
        ActionChains(self.webdriver).move_to_element(bubble_chart_Icon).perform()
        self.assertEqual("Bubble Chart", bubble_chart_title)

    def test_barchart_icon_existing_audience(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()

        bar_chart_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Bar Chart')]")
        bar_chart_title = bar_chart_Icon.get_attribute("title")
        print(bar_chart_title)
        ActionChains(self.webdriver).move_to_element(bar_chart_Icon).perform()
        self.assertEqual("Bar Chart", bar_chart_title)

    def test_infoviz_icon_from_landing_page(self):
        section = self.__class__.__name__
        audience_name = self.configAB[section]["audience_name"]

        home_page  = HomePage(self.webdriver,self.config)
        home_page.searchProjects(audience_name)

        info_Viz_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Audience Profile')]")
        info_Viz_title = info_Viz_Icon.get_attribute("title")
        print(info_Viz_title)
        ActionChains(self.webdriver).move_to_element(info_Viz_Icon).perform()
        self.assertEqual("Audience Profile", info_Viz_title)

    def test_bubblechart_icon_from_landing_page(self):
        section = self.__class__.__name__
        audience_name = self.configAB[section]["audience_name"]

        home_page  = HomePage(self.webdriver,self.config)
        home_page.searchProjects(audience_name)

        bubble_chart_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Bubble Chart')]")
        bubble_chart_title = bubble_chart_Icon.get_attribute("title")
        print(bubble_chart_title)
        ActionChains(self.webdriver).move_to_element(bubble_chart_Icon).perform()
        self.assertEqual("Bubble Chart", bubble_chart_title)

    def test_barchart_icon_from_landing_page(self):
        section = self.__class__.__name__
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(audience_name)

        bar_chart_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Bar Chart')]")
        bar_chart_title = bar_chart_Icon.get_attribute("title")
        print(bar_chart_title)
        ActionChains(self.webdriver).move_to_element(bar_chart_Icon).perform()
        self.assertEqual("Bar Chart", bar_chart_title)

    def test_infoviz_icon_from_project_workspace(self):
        section = self.__class__.__name__
        project_name2 = self.configAB[section]["project_name2"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name2)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.searchProjects(audience_name)

        info_Viz_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Audience Profile')]")
        info_Viz_title = info_Viz_Icon.get_attribute("title")
        print(info_Viz_title)
        ActionChains(self.webdriver).move_to_element(info_Viz_Icon).perform()
        self.assertEqual("Audience Profile", info_Viz_title)

    def test_bubblechart_icon_from_project_workspace(self):
        section = self.__class__.__name__
        project_name2 = self.configAB[section]["project_name2"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name2)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.searchProjects(audience_name)

        bubble_chart_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Bubble Chart')]")
        bubble_chart_title = bubble_chart_Icon.get_attribute("title")
        print(bubble_chart_title)
        ActionChains(self.webdriver).move_to_element(bubble_chart_Icon).perform()
        self.assertEqual("Bubble Chart", bubble_chart_title)

    def test_barchart_icon_from_project_workspace(self):
        section = self.__class__.__name__
        project_name2 = self.configAB[section]["project_name2"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name2)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.searchProjects(audience_name)

        bar_chart_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-attr-title,'Bar Chart')]")
        bar_chart_title = bar_chart_Icon.get_attribute("title")
        print(bar_chart_title)
        ActionChains(self.webdriver).move_to_element(bar_chart_Icon).perform()
        self.assertEqual("Bar Chart", bar_chart_title)

    def test_infoviz_default_view(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        sleep(10)
        Info_Viz = self.webdriver.find_element_by_xpath("//div[contains(@id,'dataVisualizations')]")
        # info_Viz_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.selectChartType(1)')]")
        if Info_Viz.is_displayed():
            print("Infoviz is getting displayed")
        else:
            print("Infoviz is not getting displayed")

    def test_infoviz_getting_displayed_after_editing(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]
        new_audience_name = self.configAB[section]["new_audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)
        audience_page = AudiencePage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()
        project_page.audience_menu_icon(audience_name).click()
        project_page.audienceEditIcon(audience_name)
        audience_page.audience_rename(new_audience_name)
        sleep(10)
        Info_Viz = self.webdriver.find_element_by_xpath("//div[contains(@id,'dataVisualizations')]")
        # info_Viz_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.selectChartType(1)')]")
        if Info_Viz.is_displayed():
            print("Infoviz is getting displayed")
        else:
            print("Infoviz is not getting displayed")

        # renaming to original one
        project_page.AudienceName(new_audience_name).click()
        project_page.audience_menu_icon(new_audience_name).click()
        project_page.audienceEditIcon(new_audience_name)
        audience_page.audience_rename(audience_name)

    def test_compare_icon_not_visible_when_on_infoviz(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name).click()

        compare_icon = self.webdriver.find_element_by_css_selector('.compare-trigger')
        if compare_icon.is_displayed():
            print("Compare Icon is visible")
        else:
            print("Compare Icon is not visible")

    def test_profile_insights_does_not_exist_for_NonUs(self):
        section = self.__class__.__name__
        project_name  = self.configAB[section]["project_non_us"]
        audience_name = self.configAB[section]["non_us_aud_name1"]

        home_page = HomePage(self.webdriver, self.config)
        project_page = ProjectPage(self.webdriver, self.config)

        home_page.searchProjects(project_name)
        project_page.AudienceName(audience_name ).click()

        try:
            info_Viz_Icon = self.webdriver.find_element_by_xpath("//button[contains(@ng-click,'$ctrl.selectChartType(1)')]")
            # info_Viz_title = info_Viz_Icon.get_attribute("title")
            info_Viz_Icon.is_displayed()
            print("info_Viz_title is enabled")
        except:
            print("info_Viz_title is disabled")

