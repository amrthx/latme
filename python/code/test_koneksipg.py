import psycopg2

dsn = "host={} dbname={} user={} password={}".format('192.168.0.222','retail','admin','mirota')
conn = psycopg2.connect(dsn)
cur = conn.cursor()

# proses filenya
file_baca = open("supp.txt","r")
baca = file_baca.readlines()
#update data
n=1
for data in baca:
    a=data.rstrip('\n')
    update_sql = "UPDATE supplier set aktif='0' where relasi='%s'" % a
    cur.execute(update_sql)
    conn.commit()    
    print ("no->%d kode supplier-> %s" % (n,a)) 
    n +=1
#tutup file
file_baca.close()
#tutup dbase
cur.close()
conn.close()
