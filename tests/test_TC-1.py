from framework.common import jsonGetter
from pajeObjects.requests import requests
from pytest_testrail.plugin import pytestrail
import pytest
import time

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

CONFIG = 'resources/config.json'
TESTDATA = 'resources/testdata.json'
SITE = jsonGetter.GetJson.getFile(CONFIG, "SITE")
testdata1 = jsonGetter.GetJson.getFile(TESTDATA, "testdata1")

r = requests.Request() #some creditals

#@pytest.mark.usefixtures("get_driver")
class TestSuite1:
    @pytest.mark.parametrize("login, password, token", testdata1)
    #@pytestrail.case('C19380774')
    def test_one(self):
        r.minProcessTime()









