import tests, datetime, glob, os, xlrd
from an.test.ab.HomePage import HomePage
from an.test.ab.ProjectPage import ProjectPage
from an.test.core.Util import get_env
import boto.s3.connection
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class audience_distribution(tests.SeleniumTest):
    # def test_channel_planner_distribution(self):
    #     section = self.__class__.__name__
    #     project_name  = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #
    #     # # Delete existing file in workspace
    #     # path = self.workspace + "\\Channel Propensity*.xlsx"
    #     # for file in glob.glob(path):
    #     #     os.remove(file)
    #
    #     home_page  = HomePage(self.webdriver,self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver,self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_download_icon(audience_name).click()
    #     project_page.DistributionType(audience_name,"Channel Planner").click()
    #
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located(
    #         (By.XPATH, "//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath(
    #         "//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath(
    #         "//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #     self.assertEqual(date, todays_date, "Distributed to Channel Planner tag's date incorrect")
    #     self.assertRegexpMatches(tag, "Distributed to Channel Planner|Distributing to Channel Planner", "Channel Planner tag incorrect")
    #     ########################################
    #     # sleep(20)
    #     # Verify header name in  file
    #     # for file in glob.glob(path):
    #     #     excel_sheet = xlrd.open_workbook(file)
    #     #     sheet1 = excel_sheet.sheet_by_index(0)
    #     #
    #     #     row = sheet1.row_slice(0)
    #     #     excel_header = row[0].value
    #     #     print(excel_header)
    #     #     self.assertEqual(excel_header, "Audience Name: DNT_AudShare_Test","File header incorrect")

    # def test_consumer_journey_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name_cj"]
    #     audience_name = self.configAB[section]["audience_name_cj"]
    #     key_id = self.configAB[section]["access_key_id"]
    #     key_pwd = self.configAB[section]["access_key_pwd"]
    #     folder_name = get_env(self.omni_url)
    #     #check file count from s3
    #     s3conn = boto.connect_s3(aws_access_key_id=key_id,aws_secret_access_key=key_pwd)
    #     bucket = s3conn.get_bucket('annalect-annalect-audiencebuilder', validate=False)
    #     lst = bucket.list(prefix="distribution/customer-journey/"+folder_name)
    #     count = []
    #     for key in lst:
    #         count.append(key)
    #
    #     print len(count)
    #
    #     # Distribution
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click(
    #     project_page.ConsumerJourney(audience_name)
    #     # timings = self.webdriver.execute_script("return window.performance.getEntriesByName();")
    #     # print timings
    #
    #     # check file count from s3
    #     sleep(150)
    #     lst = bucket.list(prefix="distribution/customer-journey/"+folder_name)
    #     count1 = []
    #     for key in lst:
    #         count1.append(key)
    #
    #     print len(count1)
    #     assert len(count1) > len(count),'File download didn\'t happen'

    # def test_content_inspiration_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     project_page.ContentInspiration(audience_name)
    #
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath(
    #         "//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath(
    #         "//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #     self.assertEqual(date, todays_date, "Distributed to Content Inspiration tag's date incorrect")
    #     self.assertRegexpMatches(tag, "Distributing to Content Inspiration|Distributed to Content Inspiration", "Content Inspiration tag incorrect")
    #     ########################################

    # def test_content_inspiration_curated_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #
    #     # Delete existing file in workspace
    #     path = self.workspace + "\\Audience_Services_Content_Inspiration_Video_List*.xlsx"
    #     for file in glob.glob(path):
    #         os.remove(file)
    #
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_download_icon(audience_name).click()
    #     project_page.DistributionType(audience_name, "Content Inspiration (Curated)").click()
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click(
    #     tag = self.webdriver.find_element_by_xpath(
    #         "//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]").text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath(
    #         "//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath(
    #         "//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #     self.assertEqual(date, todays_date, "created tag date incorrect")
    #     self.assertRegexpMatches(tag, "Distributed to Content Inspiration (Curated)|Distributed to Content Inspiration (Curated)", "Content Inspiration (Curated) tag incorrect")
    #     ########################################
    #     sleep(20)
    #     # Verify header name in  file
    #     for file in glob.glob(path):
    #         excel_sheet = xlrd.open_workbook(file)
    #         sheet1 = excel_sheet.sheet_by_index(0)
    #
    #         row = sheet1.row_slice(0)
    #         excel_header = row[0].value
    #         print(excel_header)
    #         self.assertEqual(excel_header, "Audience Video Export for Curation","File header incorrect")

    # def test_dbm_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #     key_id = self.configAB[section]["access_key_id"]
    #     key_pwd = self.configAB[section]["access_key_pwd"]
    #     folder_name = get_env(self.omni_url)
    #     # check file count from s3
    #
    #     s3conn = boto.connect_s3(aws_access_key_id=key_id,aws_secret_access_key=key_pwd)
    #     bucket = s3conn.get_bucket('annalect-annalect-audiencebuilder', validate=False)
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/dbm/"+folder_name)
    #     count = []
    #     for key in lst:
    #         count.append(key)
    #
    #     # print len(count)
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     project_page.DV360(audience_name)
    #
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #     # print(curr_time_value,tag_time_value)
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #     # print(date+" "+todays_date)
    #     self.assertEqual(date, todays_date, "Distributed to DV360 tag date incorrect")
    #     self.assertRegexpMatches(tag, "Distributed to DV360|Distributing to DV360", "DV360 tag incorrect")
    #     ########################################
    #     sleep(200)
    #     # check file count from s3
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/dbm/" + folder_name)
    #     count1 = []
    #     for key in lst:
    #         count1.append(key)
    #
    #     # print len(count1)
    #
    #     assert len(count1) > len(count), 'File download didn\'t happen'

    # def test_digital_content_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #     key_id = self.configAB[section]["access_key_id"]
    #     key_pwd = self.configAB[section]["access_key_pwd"]
    #     folder_name = get_env(self.omni_url)
    #     # check file count from s3
    #     s3conn = boto.connect_s3(aws_access_key_id=key_id,aws_secret_access_key=key_pwd)
    #     bucket = s3conn.get_bucket('annalect-annalect-audiencebuilder', validate=False)
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/dbm/"+folder_name)
    #     count = []
    #     for key in lst:
    #         count.append(key)
    #
    #     # print len(count)
    #
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     project_page.DigitalContent(audience_name)
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #     self.assertEqual(date, todays_date, "Distributed to Digital Content tag date incorrect")
    #     self.assertRegexpMatches(tag, "Distributed to Digital Content|Distributing to Digital Content", "Digital Content tag incorrect")
    #     ########################################
    #     sleep(200)
    #     # check file count from s3
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/dbm/"+folder_name)
    #     count1 = []
    #     for key in lst:
    #         count1.append(key)
    #
    #     # print len(count1)
    #
    #     assert len(count1) > len(count),'File download didn\'t happen'
    #
    # def test_facebook_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #     key_id        = self.configAB[section]["access_key_id"]
    #     key_pwd       = self.configAB[section]["access_key_pwd"]
    #     folder_name = get_env(self.omni_url)
    #     # check file count from s3
    #     s3conn = boto.connect_s3(aws_access_key_id= key_id,aws_secret_access_key=key_pwd)
    #     bucket = s3conn.get_bucket('annalect-annalect-audiencebuilder', validate=False)
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/fb/"+folder_name)
    #     count = []
    #     for key in lst:
    #         count.append(key)
    #
    #     # print len(count)
    #
    #     #Click on Facebook
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     project_page.Facebook(audience_name)
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #     self.assertEqual(date, todays_date, "Distributed to Facebook tag date incorrect")
    #     self.assertRegexpMatches("Distributing to Facebook", "Distributing to Facebook|Distributed to Facebook","Facebook tag incorrect")
    #     ########################################
    #     sleep(200)
    #     # check file count from s3
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/fb/"+folder_name)
    #     count1 = []
    #     for key in lst:
    #         count1.append(key)
    #     # print len(count1)
    #
    #     assert len(count1) > len(count),'File download didn\'t happen'

    # def test_SemanticAudienceExplorer_distribution(self):
    #     section = self.__class__.__name__
    #     project_name  = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #     key_id        = self.configAB[section]["access_key_id"]
    #     key_pwd       = self.configAB[section]["access_key_pwd"]
    #     folder_name = get_env(self.omni_url)
    #     # check file count from s3
    #     s3conn = boto.connect_s3(aws_access_key_id=key_id,aws_secret_access_key=key_pwd)
    #     bucket = s3conn.get_bucket('annalect-annalect-audiencebuilder', validate=False)
    #     lst = bucket.list(prefix="distribution/audience-activation-team/semasio/"+folder_name)
    #     count = []
    #     date_modified_lst = []
    #     for key in lst:
    #         count.append(key)
    #         date_modified_lst.append(key.last_modified)
    #
    #     # print len(count)
    #     #click on semantic explorer
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     project_page.SemanticAudienceExplorer(audience_name)
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #    ########################################
    #     sleep(200)
    #     # check file count from s3
    #     lst = bucket.list(prefix="distribution/audience-activation-team/semasio/"+folder_name)
    #     count1 = []
    #     date_modified_lst1 =[]
    #     for key in lst:
    #         count1.append(key)
    #         date_modified_lst1.append(key.last_modified)
    #     # print len(count1)
    #
    #     if len(count1) == len(count):
    #         date_modified_lst.sort()
    #         date_modified_lst1.sort()
    #         # print date_modified_lst
    #         # print date_modified_lst1
    #         assert date_modified_lst != date_modified_lst1,'File download didn\'t happen'
    #     else:
    #         assert len(count1) > len(count)  ,'File download didn\'t happen'
    #     self.assertEqual(date, todays_date, "Distributed to Semantic Audience Explorer tag date incorrect")
    #     self.assertRegexpMatches(tag, "Distributed to Semantic Audience Explorer|Distributing to Semantic Audience Explorer","Semantic Audience Explorer tag incorrect")

    # def test_tradedesk_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #     key_id = self.configAB[section]["access_key_id"]
    #     key_pwd = self.configAB[section]["access_key_pwd"]
    #     folder_name = get_env(self.omni_url)
    #     # check file count from s3
    #     s3conn = boto.connect_s3(aws_access_key_id=key_id,aws_secret_access_key=key_pwd)
    #     bucket = s3conn.get_bucket('annalect-annalect-audiencebuilder', validate=False)
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/ttd/"+folder_name)
    #     count = []
    #     for key in lst:
    #         count.append(key)
    #
    #     # print len(count)
    #     # click on Trade Desk
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     project_page.TradeDesk(audience_name)
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #     ########################################
    #     sleep(200)
    #     # check file count from s3
    #     lst = bucket.list(prefix="distribution/audience-activation-team/liveramp/ttd/"+folder_name)
    #     count1 = []
    #     for key in lst:
    #         count1.append(key)
    #
    #     # print len(count1)
    #
    #     assert len(count1) > len(count), 'File download didn\'t happen'
    #     self.assertEqual(date, todays_date, "Distributed to Trade Desk tag date incorrect")
    #     self.assertRegexpMatches(tag, "Distributed to Trade Desk|Distributing to Trade Desk", "Trade Desk tag incorrect")
    #
    # def test_tvContent_distribution(self):
    #     section = self.__class__.__name__
    #     project_name = self.configAB[section]["project_name"]
    #     audience_name = self.configAB[section]["audience_name"]
    #     key_id = self.configAB[section]["access_key_id"]
    #     key_pwd = self.configAB[section]["access_key_pwd"]
    #
    #     folder_name = get_env(self.omni_url)
    #     # check file count from s3
    #     s3conn = boto.connect_s3(aws_access_key_id=key_id,aws_secret_access_key=key_pwd)
    #     bucket = s3conn.get_bucket('annalect-annalect-audiencebuilder', validate=False)
    #     lst = bucket.list(prefix="distribution/audience-activation-team/videoamp/"+folder_name)
    #     count = []
    #     for key in lst:
    #         count.append(key)
    #
    #     # print len(count)
    #     #Click on TV Content
    #     home_page = HomePage(self.webdriver, self.config)
    #     home_page.searchProjects(project_name)
    #
    #     project_page = ProjectPage(self.webdriver, self.config)
    #     project_page.audience_menu_icon(audience_name).click()
    #     project_page.audience_share_icon(audience_name).click()
    #     project_page.TVContent(audience_name)
    #     #############History Tag check###########
    #     sleep(5)
    #     self.webdriver.find_element_by_xpath("//div[text()='" + audience_name + "']/following::div[4]").click()
    #
    #     project_page.HistoryTab().click()
    #     tag = (WebDriverWait(self.webdriver, 50).until(EC.visibility_of_element_located((By.XPATH,"//audience-history-list/ul/li/audience-history-item/ul[1]/li[2]")))).text
    #     now = datetime.datetime.now()
    #     todays_date = now.strftime("%b %d, %Y").replace(' 0', ' ')
    #     date = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[3]").text
    #
    #     # Verify today's time with log time
    #     time = self.webdriver.find_element_by_xpath("//audience-history-list/ul/li/audience-history-item/ul[1]/li[4]").text
    #     tag_time_value = int(time[:-3].replace(":", ""))
    #     curr_time_value = int(now.strftime("%I") + now.strftime("%M"))
    #
    #     assert (curr_time_value - tag_time_value) < 45, 'Time displayed in log seems incorrect'
    #
    #     self.assertEqual(date, todays_date, "Distributed to TV Content tag date incorrect")
    #     self.assertRegexpMatches(tag, "Distributed to TV Content|Distributing to TV Content", "TV Content tag incorrect")
    #     ########################################
    #     sleep(130)
    #     # check file count from s3
    #     lst = bucket.list(prefix="distribution/audience-activation-team/videoamp/"+folder_name)
    #     count1 = []
    #     for key in lst:
    #         count1.append(key)
    #
    #     # print len(count1)
    #
    #     assert len(count1) > len(count), 'File download didn\'t happen'

    def test_distribution_disable_feature(self):
        section = self.__class__.__name__
        project_name = self.configAB[section]["project_name"]
        audience_name = self.configAB[section]["audience_name"]

        home_page = HomePage(self.webdriver, self.config)
        home_page.searchProjects(project_name)

        project_page = ProjectPage(self.webdriver, self.config)
        project_page.audience_menu_icon(audience_name).click()
        project_page.audience_share_icon(audience_name).click()
        ele= self.webdriver.find_element_by_xpath("//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'Consumer Journey')]")
        text = ele.get_attribute('class')
        print(text)

        CI_text = self.webdriver.find_element_by_xpath("//*[text()='" + audience_name + "']//following::div[contains(@class ,distribute-dd-menu)]/div[contains(text(),'Content Inspiration')]").get_attribute('class')
        print(CI_text)