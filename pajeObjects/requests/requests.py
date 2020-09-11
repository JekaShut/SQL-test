from framework.utils import SQLUtils
from framework.common import jsonGetter

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

SQLtest = 'resources/sql.json'
creditals = jsonGetter.GetJson.getFile(SQLtest, "creditals")
data = jsonGetter.GetJson.getFile(SQLtest, "data")
sql_requests = jsonGetter.GetJson.getFile(SQLtest, "sql_requests")

sql = SQLUtils.SQL(host=creditals.get("host"),
             user=creditals.get("user"),
             passwd=creditals.get("passwd"),
             database=creditals.get("database")
             )

MIN_PROCESS_TIME = sql_requests.get("MIN_PROCESS_TIME")
UNIC_TESTS = sql_requests.get("UNIC_TESTS")
TESTS_AFTER2015 = sql_requests.get("TESTS_AFTER2015")[0] + data.get("date") + sql_requests.get("TESTS_AFTER2015")[1]
TESTS_FIREFOX_CHROME = sql_requests.get("TESTS_FIREFOX_CHROME")[0] + data.get("firefox") + sql_requests.get("TESTS_FIREFOX_CHROME")[1] + data.get("chrome") + sql_requests.get("TESTS_FIREFOX_CHROME")[2]



class Request:
    def request_minProcessTime(self):
        cursor = sql.cursor()
        result = sql.runscript(cursor, MIN_PROCESS_TIME)
        logger.info("\n________________MIN_PROCESS_TIME_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________MIN_PROCESS_TIME_END_________________\n")
        return result


    def request_unicTests(self):
        cursor = sql.cursor()
        result = sql.runscript(cursor, UNIC_TESTS)
        logger.info("\n________________UNIC_TESTS_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________UNIC_TESTS_END_________________\n")
        return result

    def request_TestsAfter(self):
        cursor = sql.cursor()
        result = sql.runscript(cursor, TESTS_AFTER2015)
        logger.info("\n________________TESTS_AFTER2015_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________TESTS_AFTER2015_END_________________\n")
        return result

    def request_TestsByBrowsers(self):
        cursor = sql.cursor()
        result = sql.runscript(cursor, TESTS_FIREFOX_CHROME)
        logger.info("\n________________TESTS_FIREFOX_CHROME_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________TESTS_FIREFOX_CHROME_END_________________\n")
        return result

    def closeConnection(self):
        sql.closeConnect()

'''
USE union_reporting;
SELECT project.name
FROM project
JOIN test
ON 
'''