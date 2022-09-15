import sqlite3


connection = sqlite3.connect("climate.db")
cursor = connection.cursor()

sql_command = """
INSERT or IGNORE INTO ClimateData (Year, CO2, Temperature)
Values ("1950", "250", "14.1");"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData (Year, CO2, Temperature)
Values ("1960", "265", "15.5");"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData (Year, CO2, Temperature)
Values ("1970", "272", "16.3");"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData (Year, CO2, Temperature)
Values ("1980", "260", "18.1");"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData (Year, CO2, Temperature)
Values ("1990", "300", "17.3");"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData (Year, CO2, Temperature)
Values ("2000", "320", "19.1");"""
cursor.execute(sql_command)

sql_command = """
INSERT or IGNORE INTO ClimateData (Year, CO2, Temperature)
Values ("2010", "389", "20.2");"""
cursor.execute(sql_command)



import sqlite3
connection = sqlite3.connect("climate.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM ClimateData")
print("climatedata:")

result = cursor.fetchall()
for r in result:
    print(r)

import matplotlib.pyplot as plt

connection = sqlite3.connect("climate.db")
years = [1950,1960,1970,1980,1990,2000,2010]
co2 = [250,265,272,260,300,320,389]
temp = [14.1,15.5,16.3,18.1,17.3,19.1,20.2]

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")
plt.show()

connection.close()