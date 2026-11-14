#SQLite i Python
import sqlite3

#skab en forbindelse til databasen, HUSK AT GEMME DEN ET STED DU KAN FINDE IGEN.
conn = sqlite3.connect("sensordata.db")
print("Connection to database established!")

#skab en cursor
cursor = conn.cursor() #for at kunne udføre SQL kommandoer

#opret en tabel
cursor.execute("""CREATE TABLE sensor_data (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            nameid TEXT,
            sensor TEXT,
            input INTEGER,
            result BOOLEAN
)""")
#dog string bruges fordi manden i youtube-videoen siger det. Alternativt skulle det skrives på en linje.

# Datatyper:
# NULL: bruges til at angive at en værdi er tom
# INTEGER: bruges til heltal
# REAL: bruges til decimaltal
# TEXT: bruges til tekst
# BLOB: bruges til binære data, såsom billeder eller filer

conn.commit() #gem ændringerne i databasen

conn.close() #luk forbindelsen til databasen, best practice!