# Gender Bias in Wikidata: Darstellung von Berufsklischees

## 1. Einleitung

Digitale Wissenssysteme wie Wikidata spielen eine zentrale Rolle bei der Organisation und Bereitstellung von Informationen. Gleichzeitig wird zunehmend diskutiert, dass solche Datenbanken gesellschaftliche Ungleichheiten nicht nur abbilden, sondern auch verstärken können.

Ein besonders relevanter Aspekt ist der sogenannte Gender Bias: die ungleiche Darstellung und Repräsentation von Geschlechtern in Daten. Diese Arbeit untersucht, inwiefern sich solche Verzerrungen am Beispiel von Berufsbildern in Wikidata erkennen lassen.


## 2. Forschungsfrage

Die zentrale Forschungsfrage lautet:

**Inwiefern führt die Struktur von Wikidata zu einer Unterrepräsentation bestimmter Berufe und zu geschlechtsspezifischen Verzerrungen?**


## 3. Datenquelle

Die Daten wurden aus **Wikidata** mittels **SPARQL-Abfragen** extrahiert.

Verwendete Variablen:
- Beruf (`occupation`)
- Geschlecht (`gender`)
- Anzahl von Personen pro Kombination

Beispielhafte analysierte Berufe:
- CEO (Führungsposition)
- Arzt / Ärztin (medizinischer Bereich)
- Pflege / Pflegerin (fürsorgliche Tätigkeit)


## 4. Methodik

Die Analyse erfolgte in mehreren Schritten:

### 4.1 Datenextraktion
- Abfrage relevanter Berufe und Geschlechterverteilungen über SPARQL
- Export der Daten als CSV-Dateien

### 4.2 Datenaufbereitung
- Einlesen der Daten mit **Python (pandas)**
- Bereinigung der Daten (z. B. Datentypen)
- Strukturierung der Kategorien

### 4.3 Datenanalyse
Es wurden zwei Analyseformen verwendet:

1. **Absolute Werte**
   - Darstellung der Anzahl von Personen pro Beruf und Geschlecht

2. **Relative Werte (Prozent)**
   - Berechnung von Anteilen innerhalb des Gesamtdatensatzes
   - Vergleich der relativen Sichtbarkeit von Berufsgruppen

### 4.4 Visualisierung
Die Visualisierung erfolgte mit:
- **matplotlib**
- **seaborn**


## 5. Ergebnisse

Die Ergebnisse zeigen deutliche Unterschiede in der Darstellung von Berufen:

### 5.1 Führungspositionen (CEO)
- Starke Dominanz männlicher Personen
- Weibliche Personen deutlich unterrepräsentiert

### 5.2 Medizinische Berufe
- Männer dominieren den Arztberuf
- Frauen sind deutlich seltener repräsentiert

### 5.3 Pflegeberufe
- Starke Dominanz weiblicher Personen
- Männer sind deutlich unterrepräsentiert

### 5.4 Gesamtverteilung
Die prozentuale Darstellung zeigt zusätzlich:
- Bestimmte Berufsgruppen (z. B. Arzt) sind insgesamt stärker in Wikidata vertreten
- Andere Berufe (insbesondere alltägliche Tätigkeiten) sind kaum sichtbar


## 6. Interpretation

Die beobachteten Muster entsprechen klassischen gesellschaftlichen Geschlechterstereotypen:

- Führungs- und prestigeträchtige Berufe → überwiegend männlich  
- Fürsorgliche und unterstützende Tätigkeiten → überwiegend weiblich  

Darüber hinaus zeigt die Analyse, dass Wikidata **keine neutrale Abbildung der Realität** darstellt:

- Es werden vor allem **sichtbare und relevante Personen** erfasst  
- Alltägliche Berufe sind strukturell unterrepräsentiert  

Dies führt zu einer Verzerrung der Daten, die bestehende Ungleichheiten nicht nur widerspiegelt, sondern potenziell verstärkt.


## 7. Limitationen

Die Analyse unterliegt mehreren Einschränkungen:

- Wikidata erfasst nicht die gesamte Bevölkerung  
- Fokus auf öffentlich dokumentierte Personen  
- Unterschiede in der Datenqualität je nach Beruf  
- Geschlecht wird meist binär erfasst  

Diese Faktoren können die Ergebnisse beeinflussen und führen zu einer eingeschränkten Aussagekraft.


## 8. Fazit

Die Ergebnisse zeigen, dass Wikidata eine selektive Darstellung von Berufen enthält, die stark von gesellschaftlicher Sichtbarkeit und Relevanz geprägt ist.

Dabei werden bestehende Geschlechterverteilungen teilweise reproduziert und verstärkt. Besonders auffällig ist die Unterrepräsentation weiblicher Personen in Führungspositionen sowie die Dominanz von Frauen in fürsorglichen Tätigkeiten.

Die Analyse verdeutlicht, dass Daten nicht neutral sind, sondern durch soziale Strukturen geprägt werden.


## 9. Technologien

- Python
- pandas
- matplotlib
- seaborn
- SPARQL
- Wikidata


## 10. Reproduzierbarkeit

Alle Analysen können mit den bereitgestellten CSV-Dateien und dem Jupyter Notebook (`analysis.ipynb`) reproduziert werden.
