# Gender Bias in Wikidata: Vergleich von Berufsrepräsentationen

## 1. Einleitung

Digitale Wissensdatenbanken wie Wikidata spielen eine wichtige Rolle bei der Darstellung von Wissen. Gleichzeitig stellt sich die Frage, ob diese Daten neutrale Abbildungen der Realität sind oder bestehende gesellschaftliche Ungleichheiten widerspiegeln.

In dieser Analyse wird untersucht, wie Berufe in Wikidata dargestellt sind und inwiefern diese Darstellung von der realen Verteilung in der Bevölkerung abweicht.


## 2. Forschungsfrage

Die zentrale Forschungsfrage lautet:

**Inwiefern unterscheidet sich die Darstellung von Berufen in Wikidata von der tatsächlichen Geschlechterverteilung in der Realität, und welche geschlechtsspezifischen Verzerrungen ergeben sich daraus?**


## 3. Datenbasis

Für die Analyse wurden zwei Datenquellen verwendet:

### 3.1 Wikidata
- Extraktion von Berufen und Geschlechterverteilungen mittels SPARQL
- Fokus auf Personen mit dokumentierter Relevanz

### 3.2 Reale Daten
- Statistische Daten zur tatsächlichen Geschlechterverteilung in Berufen
- Vergleich als Referenz zur Einordnung der Wikidata-Ergebnisse


## 4. Methodik

Die Analyse besteht aus drei zentralen Schritten:

### 4.1 Auswahl von Berufen
Untersuchte Berufe umfassen sowohl:
- prestigeträchtige Berufe (z. B. CEO, Politiker, Ärzte)
- alltägliche Berufe (z. B. Pflege, Büroangestellte, Erzieher)

### 4.2 Berechnung der Geschlechteranteile
- Berechnung von Prozentanteilen (männlich/weiblich)
- getrennt für Wikidata und reale Daten

### 4.3 Vergleich Wikidata vs. Realität
- direkte Gegenüberstellung der Anteile
- Visualisierung mit Diagrammen
- Fokus auf Abweichungen zwischen beiden Datensätzen

## 5. Ergebnisse

### 5.1 Starke Unterschiede zwischen Wikidata und Realität

Die Analyse zeigt deutliche Abweichungen:

- In Wikidata sind **männlich dominierte Berufe deutlich stärker vertreten**
- Weiblich dominierte Berufe sind oft unterrepräsentiert

### 5.2 Beispiele

- **CEO:**
  - Wikidata: stark männlich dominiert
  - Realität: weniger stark unausgeglichen

- **Ärzte:**
  - Wikidata: sehr hoher Männeranteil (~90%)
  - Realität: deutlich ausgeglichener (~50/50)

- **Pflegeberufe:**
  - Wikidata: weiblich dominiert
  - Realität: ebenfalls weiblich dominiert, aber weniger extrem


### 5.3 Gesamtmuster

Ein zentrales Ergebnis ist:

> Berufe mit höherem gesellschaftlichen Status und Sichtbarkeit sind in Wikidata überrepräsentiert und gleichzeitig stärker männlich dominiert.


## 6. Vergleich des Männeranteils

Ein besonders wichtiger Befund ist der Vergleich des Männeranteils zwischen Wikidata und realen Daten:

- In fast allen untersuchten Berufen ist der **Männeranteil in Wikidata höher als in der Realität**
- Dies gilt besonders für:
  - Führungspositionen
  - politische Berufe
  - akademische Berufe

→ Daraus lässt sich schließen, dass Wikidata eine systematische Verzerrung in Richtung männlicher Sichtbarkeit aufweist.


## 7. Interpretation

Die Ergebnisse deuten darauf hin, dass Wikidata keine neutrale Abbildung der Realität darstellt.

Mögliche Gründe:

- Fokus auf „relevante“ Personen
- höhere Sichtbarkeit männlicher Personen
- historische Ungleichheiten in Berufen

Dies führt dazu, dass bestehende Geschlechterverhältnisse:
- verstärkt werden  
- und in Daten reproduziert werden  


## 8. Limitationen

- Wikidata enthält nicht alle Personen → Auswahlbias
- reale Daten variieren je nach Quelle
- Vergleich basiert auf aggregierten Daten
- Geschlecht meist binär erfasst


## 9. Fazit

Die Analyse zeigt, dass Wikidata eine verzerrte Darstellung von Berufen enthält.

Insbesondere werden:
- männlich dominierte Berufe stärker sichtbar
- weiblich dominierte Tätigkeiten unterrepräsentiert

Somit trägt Wikidata zur Reproduktion gesellschaftlicher Ungleichheiten in Daten bei.


## 10. Technologien

- Python
- pandas
- seaborn / matplotlib
- SPARQL
- Wikidata


## 11. Reproduzierbarkeit

Alle Ergebnisse können mit den bereitgestellten Daten und dem Jupyter Notebook reproduziert werden.
