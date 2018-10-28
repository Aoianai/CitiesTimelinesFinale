## DrawShapeSave

import sqlite3

class SaveCoor:
    def __init__(self, fileName):
        self.xStore = 2
        self.yStore = 2
        self.fileName = 'shapes.db'
        self.buildLevel = 1

    def cursorCreate(self):
        db = sqlite3.connect('shapes.db')
        cur = db.cursor()

        cur.execute("""INSERT INTO shapes(shapeX, shapeY, buildL)
                       values(?,?,?)"""(self.xStore, self.yStore, self.buildLevel))
        db.commit

        cur.execute("SELECT * FROM shapes")
        rows = cur.fetchall()
        for row in rows:
            print(row)
