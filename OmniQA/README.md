This is the code to execute selenium unit tests on Omni.


##Requirements

The script uses the python2.7. Install dependencies using the following command:
```
pip install -r requirements.txt
```
##ChromeDriver
Download and place chromedriver.exe on project workspace to run in chrome

##Config files

test_suite_ab.py :- contains all the list of audience explorer testcases to be executed. On running the file test execution gets initiated.
Tests.cfg        :- contains the environment i.e the URL where the tests will be executed.
AudBuilder.cfg   :- contains the test data which are being used by the testcases.
tests/__init__.py:- contains setup method where webdriver is set.Select remote driver or chrome or firefox as per requirement.

##Credentials

```
[AELogin]
username = QA.test
password = Welc...
```

## How to execute specific test case.
Run files or functions in files under tests/AudienceBuilder for audience builder cases.
While running on pycharm make sure to set working directory(Run->Edit Configuration->working directory) to workspace root
instead of tests/AudienceBuilder else it will give key error while reading cfg files.

While running from command prompt make sure to run from workspace root instead of tests/AudienceBuilder

##Bamboo plan
Raise support acccess for Selenium-Dev project.
"Selenium Grid-Omni QA Automation" plan is linked to this repository.

Click on Edit->Default Job->Script
Under script body enter below command and save to run test suite:
python -m unittest test_suite_ab

To run any particular test cases enter command in below format and save:
python -m unittest tests.AudienceBuilder.test_1_verify_audience_explorer.audience_explorer.test_search_projects

To run plan click Run dropdown->Run Plan option





