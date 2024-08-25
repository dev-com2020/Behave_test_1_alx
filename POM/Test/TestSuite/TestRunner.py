from unittest import TestLoader, TestSuite, TextTestRunner

import testtools

from POM.Test.Scripts.test_Home_page import DemoBlazeHomePage
from POM.Test.Scripts.test_contact_button import Contact_Button

if __name__ == '__main__':
    test_loader = TestLoader()
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(DemoBlazeHomePage),
        test_loader.loadTestsFromTestCase(Contact_Button),
    ))

    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

    parralel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case,None) for case in test_suite))
    parralel_suite.run(testtools.StreamResult())