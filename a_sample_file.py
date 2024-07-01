import psycopg2
 
conn=psycopg2.connect(database='homework', user='postgres', host='localhost', password='1111', port=5432)
cursor=conn.cursor()

select="""create table sample(id serial primary key, name varchar(100));"""
cursor.execute(select)

conn.commit()
cursor.close()
conn.close()
