import psycopg2

dsn = "host={} dbname={} user={} password={}".format('192.168.0.222','retail','admin','mirota')
conn = psycopg2.connect(dsn)
cur = conn.cursor()

# proses filenya
file_baca = open("supp.txt","r")
baca = file_baca.readlines()
#select data
n=1
for data in baca:
    a=data.rstrip('\n')
    select_sql = "select relasi,aktif from supplier where aktif=0 and relasi='%s'" % a
    cur.execute(select_sql)
    for row in cur:
        print ("aktif->%s kode supplier-> %s" % (row[1],row[0])) 
    n +=1
#tutup file
file_baca.close()
#tutup dbase
cur.close()
conn.close()
