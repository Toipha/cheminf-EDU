import pymysql.cursors
import pandas as pd
from sqlalchemy import create_engine


host = 'den1.mysql6.gear.host'
db = 'situation'
usr = 'situation'
psword = 'cogni88.'

engine = create_engine('mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8'
                       % (usr, psword, host, '3306', db))



# Connect to the database
connection = pymysql.connect(host=host, user=usr, password=psword, database=db, cursorclass=pymysql.cursors.DictCursor)

UserId = 'Gerrit'
sql = "SELECT * FROM situation.q17_decarburization_data;"


# with connection.cursor() as cursor:
#   cursor.execute(sql % UserId)

df_raw = pd.read_sql(sql, engine)

# df = df_raw[(df_raw['timestamp'] >= '2023-01-14') & (df_raw['timestamp'] <= '2023-02-01')]
# df['timestamp'] = pd.to_datetime(df['timestamp'])
# df = df.set_index('timestamp')
# df = df.resample('10s').first()
# df = df.interpolate()
# db.head(10)

print(df_raw)