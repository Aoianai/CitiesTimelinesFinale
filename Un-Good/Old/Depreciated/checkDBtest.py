## checkDBTest
## tests functions of checkDB.py

import unittest, checkDB

class CheckDBTest(unittest.TestCase):

    def test_openFile(self):
        testFile = CheckForCoor("testDB.db")
        testFile.openFile()
        testValue = testFile.
