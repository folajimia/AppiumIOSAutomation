import unittest
import os
from random import randint
from appium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By










class LoginTests(unittest.TestCase):

    def setUp(self):

        app = ('/Users/jimiadekoya/Library/Developer/Xcode/DerivedData/AppiumTest-gcgsbepefhezpfcysgmcatmhyyly/Build/Products/Debug-iphonesimulator/AppiumTest.app')
        self.driver = webdriver.Remote(
            command_executor='http://127.0.0.1:4723/wd/hub',
            desired_capabilities={
                'app': app,
                'platformName': 'iOS',
                'platformVersion': '12.1',
                'deviceName': 'iPhone 7'
            }
        )

    def testEmailField(self):
        emailTF = self.driver.find_element_by_accessibility_id('emailTextField')
        emailTF.send_keys("test@test.com")
        emailTF.send_keys(Keys.RETURN)
        sleep(1)
        self.assertEqual(emailTF.get_attribute("value"),"test@test.com")

    def testPasswordField(self):
        passwordTF = self.driver.find_element_by_accessibility_id('passwordTextfield')
        passwordTF.send_keys("validPW")
        passwordTF.send_keys(Keys.RETURN)
        sleep(1)
        #confirm password field is masked
        self.assertNotEqual(passwordTF.get_attribute("value"),"validPW")

    def testLogin(self):
        self.testEmailField()
        self.testPasswordField()
        self.driver.find_element_by_accessibility_id('loginButton').click()
        sleep(1)
        #smiley = self.driver.find_element_by_accessibility_id('smileyImage')
        smiley = self.driver.find_element_by_accessibility_id("smileyImage")
        self.assertTrue(smiley.get_attribute("wdVisible"))




    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
    unittest.TextTestRunner(verbosity=2).run(suite)






