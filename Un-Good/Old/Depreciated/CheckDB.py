## CheckDB

import sqlite3


class CheckForCoor:
    def __init__(self,xCoorSQL, fileName):
        self.fileName = fileName
        self.returnArray = []
        self.myArray = []
        self.xCoorSQL = xCoorSQL
    
    def openFile(self, fileName):
        db = sqlite3.connect(self.fileName)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM shapes")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
            self.returnArray.append(row)

    def denyShape(self):
        import DrawShapeMain
        if self.xCoorSQL in self.returnArray:
            SpaceBuild()
        else:
            return(True)
