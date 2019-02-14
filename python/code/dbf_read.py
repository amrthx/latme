import sys
import csv
from dbfread import DBF

table = DBF('/home/ameer/Documents/kassa23/NOTAJL.DBF')
writer = csv.writer(sys.stdout)

writer.writerow(table.field_names)
for record in table:
    writer.writerow(list(record.values()))
