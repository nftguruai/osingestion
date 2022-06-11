import psycopg2  
connection = psycopg2.connect(user="postgres",                                   
password="samwal74",                                   
host="localhost",                                   
port="5432",                                   
database="postgres") 
cur = connection.cursor() 
cur.execute("SELECT * FROM public.accounts limit 5")
rows=cur.fetchall()