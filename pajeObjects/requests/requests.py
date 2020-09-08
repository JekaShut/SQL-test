from framework.utils import SQLUtils
from framework.common import jsonGetter

SQLtest = 'resources/sql.json'
creditals = jsonGetter.GetJson.getFile(SQLtest, "creditals")

sql = SQLUtils.SQL(host=creditals.get("host"),
             user=creditals.get("user"),
             passwd=creditals.get("passwd"),
             database=creditals.get("database")
             )

class Request:
    def __init__(self):
        self.MIN_PROCESS_TIME = "SELECT * FROM api_key"
        self.UNIC_TESTS = ""
        self.TESTS_AFTER2015 = ""
        self.TESTS_FIREFOX_CHROME = ""

    def minProcessTime(self):
        cursor = sql.connect()
        result = sql.runscript(cursor, self.MIN_PROCESS_TIME)
        return result