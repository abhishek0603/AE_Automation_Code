from unittest import TestLoader,TestSuite,TextTestRunner
from tests.omni.test_1_verifyOmni import Omni01
from tests.omni.test_2_iframe import IFrameTest
from tests.omni.test_3_verifySetting import SettingsTest
from tests.omni.test_4_verifySidebarLinks import SidebarLinksTest

# get all tests from class
Omni01        = TestLoader().loadTestsFromTestCase(Omni01)
IFrameTest          = TestLoader().loadTestsFromTestCase(IFrameTest)
SettingsTest        = TestLoader().loadTestsFromTestCase(SettingsTest)
SidebarLinkTest     = TestLoader().loadTestsFromTestCase(SidebarLinksTest)


# create a test suite
test_suite = TestSuite([Omni01,
                        IFrameTest,
                        SettingsTest,
                        SidebarLinkTest
                        ])

TextTestRunner(verbosity=2).run(test_suite)
