import pymysql

class database_handler:
    def __init__(self):
        self.db = pymysql.connect(host='dronedb.c5cpbgsn3hyj.us-east-2.rds.amazonaws.com',
                             user='admin',
                             password='N0UBYbHIn49jCwF1fcXI',
                             database='dron_smogowy',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    def insert_values_measurement(self,id,pm10,pm25,humidity,hPa,temperature,IAQ,time):
        mycursor = self.db.cursor()
        query = 'INSERT INTO dron_smogowy.measurement(IdMeasurement, pm10, pm25, humidity, hPa, temperature, IAQ, time) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'
        val = (id,pm10,pm25,humidity,hPa,temperature,IAQ,time)
        mycursor.execute(query,val)
        self.db.commit()
        print(mycursor.rowcount, "record(s) inserted into measurement.")

    def insert_values_localization(self,id,longtitude,latitude,satelite):
        mycursor = self.db.cursor()
        query = 'INSERT INTO dron_smogowy.localization(IdMeasurement, longitude, latitude) VALUES(%s, %s, %s)'
        val = (id,longtitude,latitude)
        mycursor.execute(query,val)
        self.db.commit()
        print(mycursor.rowcount, "record(s) inserted into localization.")
    