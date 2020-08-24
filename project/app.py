import psycopg2 as pg

# default postgres settings
db_connection_info = {"host": "localhost", "user": "postgres", "dbname": "postgres", "port": 5432}

# TODO: Override connection info
# when postgres runs on docker container
db_connection_info["host"] = "postgres"
db_connection_info["port"] = 5432
db_connection_info["password"] = 1234

db_connection_str = "host={host} user={user} dbname={dbname} password={password} port={port}".format(
    **db_connection_info
)

print("Connecting To: ", db_connection_str)
print("Current database: ", end="")
conn = pg.connect(db_connection_str)
cur = conn.cursor()
cur.execute(""" SELECT current_database()""")
for rows in cur.fetchall():
    print(rows)
cur.close()
conn.close()
