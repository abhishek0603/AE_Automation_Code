import tests,glob,os,xlrd
from time import sleep
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage

class audience_download(tests.SeleniumTest):
    def test_download_single_existing_audience(self):
        section = self.__class__.__name__
        project_name  = self.configAB["DownloadAudience"]["project_name"]
        audience_name = self.configAB["DownloadAudience"]["audience_name"]
        # Delete existing file in workspace
        path = self.workspace + "\\"+project_name+" - "+audience_name+".xlsx"
        print(path)
        print(glob.glob(path))
        for file in glob.glob(path):
            os.remove(file)

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        # Download Audience
        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audience_download_icon(audience_name).click()
        project_page.audience_data(audience_name).click()

        sleep(30)
        path1= self.workspace + "\\"+project_name+" - "+audience_name+".xlsx"
        check = os.path.exists(path1)

        self.assertEqual(check, True, "Audience download failed")

        for file in glob.glob(path1):
            excel_sheet = xlrd.open_workbook(file)
            sheet1 = excel_sheet.sheet_by_index(0)

            row = sheet1.row_slice(0)
            excel_header = row[0].value
            sheet        = excel_sheet.sheet_by_index(0)
            Cols=""
            for i in range(sheet1.ncols):
                Cols = Cols + str(sheet.cell_value(1, i))

            print(excel_header)
            row_count = sheet.nrows
            print(Cols)

            self.assertEqual(excel_header,"Location Data for \"DNT_Auto_Aud02\"","Column header not matching")
            # self.assertEqual(row_count,1002,"Row count not matching")
            # self.assertEqual(Cols,"Attribute TypeAttribute NameAttribute ValueAttribute DescriptionAttribute Value DescriptionTarget %Index","Column names not matching")

    def test_download_multiple_existing_Audience(self):
        section = self.__class__.__name__
        project_name  = self.configAB["DownloadMultipleAudience"]["project_name"]
        audience_name1 = self.configAB["DownloadMultipleAudience"]["audience_name1"]
        audience_name2 = self.configAB["DownloadMultipleAudience"]["audience_name2"]

        # Delete existing file in workspace
        path = self.workspace + "\\"+project_name+" - Audience Compare Export*.xlsx"
        print(path)
        print(glob.glob(path))
        for file in glob.glob(path):
            os.remove(file)

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        # Download Audience
        project_page = ProjectPage(self.webdriver, self.config)
        project_page.CompareTrigger().click()
        project_page.AudienceCheckbox(audience_name1).click()
        project_page.AudienceCheckbox(audience_name2).click()
        project_page.download_button().click()

        sleep(30)
        path1 = self.workspace + "\\"+project_name+" - Audience Compare Export.xlsx"
        check = os.path.exists(path1)

        self.assertEqual(check, True, "Audience download failed")

        for file in glob.glob(path1):
            excel_sheet = xlrd.open_workbook(file)
            sheet1 = excel_sheet.sheet_by_index(0)

            row = sheet1.row_slice(0)
            excel_header = row[0].value
            sheet = excel_sheet.sheet_by_index(0)
            Cols = ""
            for i in range(sheet1.ncols):
                Cols = Cols + str(sheet.cell_value(3, i))

            row_count = sheet.nrows
            print(Cols)
            self.assertEqual(excel_header, "Location Data for \"DNT_Auto_Aud02\" vs. \"DNT_Auto_Aud03\"", "Column header not matching")

