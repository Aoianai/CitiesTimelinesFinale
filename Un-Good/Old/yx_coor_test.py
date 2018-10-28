x_rows = cursor.execute("SELECT x_coor FROM coordinates")
y_rows = cursor.execute("SELECT y_coor FROM coordinates")

for row in rows:
