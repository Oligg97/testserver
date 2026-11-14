"""Indsæt sensorresultaterne fra results.json i SQLite-databasen."""

import json
import sqlite3
from pathlib import Path

results_file = Path(__file__).with_name("results.json")
results = json.loads(results_file.read_text(encoding="utf-8"))
database_file = Path(__file__).with_name("sensordata.db")


def insert_item(connection, item):
    """Indsætter en enkelt post i sensor_data-tabellen i SQLite-databasen."""
    connection.execute(
        """
        INSERT INTO sensor_data (nameid, sensor, input, result, timestamp)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            item["id"],
            item["sensor"],
            json.dumps(item["inputs"]),
            item["result"],
            item["timestamp"],
        ),
    )


with sqlite3.connect(database_file) as connection:
    # Opret tabellen første gang; SQLite gemmer JSON-input som TEXT.
    connection.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            uid INTEGER PRIMARY KEY AUTOINCREMENT,
            nameid TEXT,
            sensor TEXT,
            input TEXT,
            result BOOLEAN,
            timestamp TEXT
        )
    """)

    for result in results:
        print(f"{result['id']} ({result['sensor']}): {result['result']}") # Udskriv resultaterne
        insert_item(connection, result)

print(f"{len(results)} JSON-poster indsat i {database_file.name}")
