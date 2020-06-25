#!/usr/bin/env python3

import boto3
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def lookupDeviceFarmProjectARN():
    # Set the region for SSM via an environment variable
    ssm = boto3.client("ssm")
    parameter = ssm.get_parameter(Name='DeviceFarmProjectArn', WithDecryption=True)
    deviceFarmProjectARN = parameter['Parameter']['Value']
    return deviceFarmProjectARN


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        devicefarm_client = boto3.client("devicefarm", region_name="us-west-2")
        testgrid_url_response = devicefarm_client.create_test_grid_url(
          projectArn=lookupDeviceFarmProjectARN(), expiresInSeconds=300)
        self.driver = webdriver.Remote(testgrid_url_response["url"], webdriver.DesiredCapabilities.FIREFOX)

#    def setUp(self):
#        self.driver = webdriver.Remote(
#        command_executor='http://127.0.0.1:4444/wd/hub',
#        desired_capabilities=DesiredCapabilities.CHROME)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source

    def tearDown(self):
#        self.driver.close()
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
