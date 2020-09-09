from framework.utils import SQLUtils
from framework.common import jsonGetter

from framework.logger.logger import Logger
logger = Logger(__file__).getlog()

SQLtest = 'resources/sql.json'
creditals = jsonGetter.GetJson.getFile(SQLtest, "creditals")

sql = SQLUtils.SQL(host=creditals.get("host"),
             user=creditals.get("user"),
             passwd=creditals.get("passwd"),
             database=creditals.get("database")
             )

class Request:
    def __init__(self):
        self.MIN_PROCESS_TIME = "SELECT project.name, test.name, test.end_time - test.start_time as min_time FROM test JOIN project ON test.project_id=project.id ORDER BY project.name, test.name;"
        self.UNIC_TESTS = "SELECT project.name, COUNT(DISTINCT test.name) AS num_tests FROM project JOIN test ON project.id = test.project_id GROUP BY project.name"
        self.TESTS_AFTER2015 = 'SELECT project.name AS project, test.name AS test, test.start_time AS time FROM project JOIN test ON test.project_id = project.id WHERE test.start_time > "2015-11-07" ORDER BY project.name, test.name'
        self.TESTS_FIREFOX_CHROME = "SELECT COUNT(test.id) AS Browsers FROM test WHERE test.browser = 'chrome' UNION SELECT COUNT(test.id) FROM test WHERE test.browser = 'firefox'"

    def minProcessTime(self):
        cursor = sql.connect()
        result = sql.runscript(cursor, self.MIN_PROCESS_TIME)
        logger.info("\n________________MIN_PROCESS_TIME_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________MIN_PROCESS_TIME_END_________________\n")
        return result


    def unicTests(self):
        cursor = sql.connect()
        result = sql.runscript(cursor, self.UNIC_TESTS)
        logger.info("\n________________UNIC_TESTS_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________UNIC_TESTS_END_________________\n")
        return result

    def TestsAfter(self):
        cursor = sql.connect()
        result = sql.runscript(cursor, self.TESTS_AFTER2015)
        logger.info("\n________________TESTS_AFTER2015_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________TESTS_AFTER2015_END_________________\n")
        return result

    def TestsByBrowsers(self):
        cursor = sql.connect()
        result = sql.runscript(cursor, self.TESTS_FIREFOX_CHROME)
        logger.info("\n________________TESTS_FIREFOX_CHROME_START_________________\n")
        for x in result:
            logger.info(x)
        logger.info("\n________________TESTS_FIREFOX_CHROME_END_________________\n")
        return result

'''
USE union_reporting;
SELECT project.name
FROM project
JOIN test
ON 
'''