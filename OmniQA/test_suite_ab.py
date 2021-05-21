from unittest import TestLoader,TestSuite,TextTestRunner
from tests.AudienceBuilder.test_1_verify_audience_explorer_login import audience_explorer_login
# from tests.AudienceBuilder.test_2_verify_audience_distribute import audience_distribution
from tests.AudienceBuilder.test_3_verify_audience_rename import audience_rename
from tests.AudienceBuilder.test_4_verify_audience_compare import audience_compare
from tests.AudienceBuilder.test_5_verify_copy_audience_criteria import audience_copy_criteria
from tests.AudienceBuilder.test_6_verify_audience_criteria_parenthesis import audience_criteria_parenthesis
from tests.AudienceBuilder.test_7_verify_rate_card import cpm_rate
from tests.AudienceBuilder.test_8_verify_audience_history import audience_history
from tests.AudienceBuilder.test_9_verify_cog import cog
from tests.AudienceBuilder.test_10_verify_audience_criteria_lists import audience_criteria_lists
from tests.AudienceBuilder.test_11_verify_project_functionalities import project_functionalities
# from tests.AudienceBuilder.test_12_verify_audience_download import audience_download
from tests.AudienceBuilder.test_13_verify_criteria_builder_functionalities import criteria_builder_functionalities
# from tests.AudienceBuilder.test_14_verify_test_taxonomy import taxonomy
from  tests.AudienceBuilder.test_15_verify_viz_icon_tooltip import viz_icon_tooltip
from tests.AudienceBuilder.test_16_verify_audience_resulting_zero_result import audience_resulting_zero_results
from tests.AudienceBuilder.test_17_verify_audience_not_meeting_min_threshold import audience_not_meeting_min_threshold
from tests.AudienceBuilder.test_18_verify_audience_getting_build_error import audience_getting_build_error
from tests.AudienceBuilder.test_19_verify_audience_that_is_building import audience_that_is_building
from tests.AudienceBuilder.test_20_verify_audience_only_saved import audience_only_saved

try:
    import boto3
    import botocore
    import datetime

except Exception as e:
    print('Library not installed: boto3')


class S3Tools(object):

    def __init__(self, bucket, filename, path_local, path_s3):
        self.session = boto3.Session(aws_access_key_id='AKIAJA3WBSORGXRA7LCA', aws_secret_access_key='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',region_name='us-east-1')
        self.s3 = self.session.client('s3')
        self.bucket = bucket
        self.filename = filename
        self.path_local = path_local
        self.path_s3 = path_s3

    def uploadToS3(self):
        self.s3.upload_file(str(self.path_local + self.filename),
                            self.bucket, str(self.path_s3 + '/' + self.filename))
        print('upload complete')




# get all tests from class
audience_explorer_login         = TestLoader().loadTestsFromTestCase(audience_explorer_login)
# audience_distribution           = TestLoader().loadTestsFromTestCase(audience_distribution)
audience_rename                 = TestLoader().loadTestsFromTestCase(audience_rename)
audience_compare                = TestLoader().loadTestsFromTestCase(audience_compare)
audience_copy_criteria          = TestLoader().loadTestsFromTestCase(audience_copy_criteria)
audience_criteria_parenthesis   = TestLoader().loadTestsFromTestCase(audience_criteria_parenthesis)
cpm_rate                        = TestLoader().loadTestsFromTestCase(cpm_rate)
audience_history                = TestLoader().loadTestsFromTestCase(audience_history)
cog                             = TestLoader().loadTestsFromTestCase(cog)
audience_criteria_lists         = TestLoader().loadTestsFromTestCase(audience_criteria_lists)
project_functionalities         = TestLoader().loadTestsFromTestCase(project_functionalities)
# audience_explorer_download    = TestLoader().loadTestsFromTestCase(audience_download)
criteria_builder_functionalities= TestLoader().loadTestsFromTestCase(criteria_builder_functionalities)
# test_taxonomy                 = TestLoader().loadTestsFromTestCase(taxonomy)
viz_icon_tooltip                = TestLoader().loadTestsFromTestCase(viz_icon_tooltip)
audience_resulting_zero_results = TestLoader().loadTestsFromTestCase(audience_resulting_zero_results)
audience_not_meeting_min_threshold = TestLoader().loadTestsFromTestCase(audience_not_meeting_min_threshold)
audience_getting_build_error    = TestLoader().loadTestsFromTestCase(audience_getting_build_error)
audience_that_is_building       = TestLoader().loadTestsFromTestCase(audience_that_is_building)
audience_only_saved             = TestLoader().loadTestsFromTestCase(audience_only_saved)

# create a test suite
test_suite = TestSuite([
                        audience_explorer_login,
                        # audience_distribution,
                        audience_rename,
                        audience_compare,
                        audience_copy_criteria,
                        audience_criteria_parenthesis,
                        cpm_rate,
                        audience_history,
                        cog,
                        audience_criteria_lists,
                        project_functionalities,
                        #audience_explorer_download,
                        criteria_builder_functionalities,
                        # test_taxonomy,
                        viz_icon_tooltip,
                        audience_resulting_zero_results,
                        audience_not_meeting_min_threshold,
                        audience_getting_build_error,
                        audience_that_is_building,
                        audience_only_saved
                        ])
TextTestRunner(verbosity=2).run(test_suite)