# Testserver

Et lille Python-projekt, der afprøver tre sensorfunktioner, gemmer resultaterne som JSON og indsætter dem i en SQLite-database.

Koden simulerer følgende aktuator- og sensorenheder:

- **AE1 (aktuatorenhed):** En alarmcentral, der modtager sensordata og kommunikerer med en server.
- **SE1 (sensorenhed):** En PIR- og lydsensor.
- **SE2 (sensorenhed):** Et gyroskop og et barometer.
- **SE3 (sensorenhed):** En Force Sensitive Resistor (FSR).

## Krav

- Python 3
- Ingen eksterne Python-pakker er nødvendige. Projektet bruger moduler, der følger med Python.

## Filer

- `AE1.py` kalder sensorfunktionerne med testinput, samler resultaterne og skriver dem til `results.json`.
- `SE1.py`, `SE2.py` og `SE3.py` indeholder hver sin sensorfunktion.
- `results.json` er JSON-filen med sensorens input, resultat og tidspunkt. Den bliver oprettet eller overskrevet af `AE1.py`.
- `save_to_db.py` læser `results.json`, opretter databasetabellen hvis den mangler, og indsætter posterne i databasen.
- `sensordata.db` er SQLite-databasen, som `save_to_db.py` bruger.

## Sådan kører du projektet

Kør kommandoerne fra projektmappen:

```text
python AE1.py
python save_to_db.py
```

Kør først `AE1.py`, så den opretter den nyeste `results.json`. Kør derefter `save_to_db.py` for at indsætte posterne i databasen.

## Sensorfunktionerne

- **SE1** returnerer `True`, hvis både `movement` og `noise` er `1`. Ellers returnerer den `False`.
- **SE2** returnerer `True`, hvis `fald` er `1`. Hvis `stod` er `1`, returnerer den `False`. Hvis begge værdier er `0`, udskriver den `OK` og returnerer `False`.
- **SE3** returnerer `True`, hvis `sleep` er `1`, og `False`, hvis `wake` er `1`. Hvis begge er `0`, returnerer funktionen i den nuværende kode `None`.

Inputværdierne til testene ændres i `AE1.py`, for eksempel:

```python
test1_inputs = {"movement": 1, "noise": 1}
test1 = SE1(**test1_inputs)
```

Dictionaryen `test1_inputs` indeholder de værdier, der både sendes til funktionen og gemmes i JSON-filen.

## Dataflow

1. `AE1.py` kalder `SE1`, `SE2` og `SE3` med testinput.
2. Scriptet samler sensorens navn, input, resultat og et tidsstempel i en liste.
3. Listen skrives til `results.json`. Tidsstemplet oprettes én gang pr. kørsel og deles af de tre testposter.
4. `save_to_db.py` læser JSON-filen og indsætter én række pr. post i `sensordata.db`.

Eksempel på en JSON-post:

```json
{
  "id": "test1",
  "sensor": "SE1",
  "inputs": {
    "movement": 1,
    "noise": 1
  },
  "result": true,
  "timestamp": "14-11-2026 14:49:54"
}
```

## Nogle tekniske detaljer

- **`Path(__file__).with_name(...)`** finder en fil i samme mappe som det aktuelle script. `__file__` er stien til scriptet, og `with_name` bruger samme mappe med et andet filnavn. Derfor virker filstierne også, hvis scriptet startes fra en anden mappe.
- **`**test1_inputs`** pakker dictionaryens værdier ud som navngivne argumenter. Kaldet svarer til `SE1(movement=1, noise=1)`. Det gør, at værdierne kun skal defineres ét sted.
- **JSON** er et tekstformat til strukturerede data. `json.dumps` omdanner sensorens `inputs`-dictionary til tekst, så den kan gemmes i en SQLite-kolonne.
- **SQLite** gemmer data i en lokal databasefil. `save_to_db.py` opretter tabellen `sensor_data`, hvis den ikke allerede findes. `uid` er et automatisk ID, mens `nameid`, `sensor`, `input`, `result` og `timestamp` indeholder værdier fra JSON-posten.
- SQL-forespørgslen bruger `?` som pladsholdere. Værdierne sendes separat til forespørgslen i stedet for at blive sat direkte ind i SQL-teksten.
- Databaseforbindelsens `with`-blok håndterer transaktionen: ændringerne gemmes, når blokken afsluttes uden fejl.

## Overskrivning og gentagne kørsler

- Hver kørsel af `AE1.py` overskriver `results.json` med de nyeste testresultater.
- Hver kørsel af `save_to_db.py` tilføjer rækker til databasen. Den sletter eller overskriver ikke tidligere rækker, så samme JSON kan blive indsat flere gange, hvis scriptet køres igen.
