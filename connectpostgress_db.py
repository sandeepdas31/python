#to connect with postgresql and to perforem database ,table creation, insert
# upadte and delete operation
import psycopg2

conn= psycopg2.connect(database="My_DB", user= "postgres", password="Sandip@123", host = "127.0.0.1", port = "5432")
print("Connection established")

cur=conn.cursor()
cur.execute('''create table job(
                id integer, name text, position text);''')
print("table created succesfully")

cur.execute("Insert into job values ('1','Sandeep','Software trainee');")
print("row inserted successfully")

cur.execute(("select id, name, position from job"))
rows=cur.fetchall()
for row in rows:
    print("id=", row[0])
    print("name=", row[1])
    print("position=",row[2])

cur.execute("update job set name='kumar' where id='1' ")
print("update success")
cur.execute(("select id, name, position from job"))
rows=cur.fetchall()
for row in rows:
    print("id=", row[0])
    print("name=", row[1])
    print("position=",row[2])

conn.commit()
conn.close()