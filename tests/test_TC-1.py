from framework.common import jsonGetter
from pajeObjects.requests import requests
from pytest_testrail.plugin import pytestrail
import pytest
import time

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

CONFIG = 'resources/config.json'
SITE = jsonGetter.GetJson.getFile(CONFIG, "SITE")


r = requests.Request()

#@pytest.mark.usefixtures("get_driver")
class TestSuite1:
    #@pytestrail.case('C19380774')
    def test_one(self):
        r.minProcessTime()
        r.unicTests()
        r.TestsAfter()
        r.TestsByBrowsers()









