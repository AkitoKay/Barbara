* Zusammenfassung

  Hier befindet sich alles Organisatorische.

* Groups

  - Python:
    - Front-End: Flo, Daniel
    - Back-End: Erik, Simon
  - Db: Markus, Angel
  - MiLFs: René, Robert, Eugen
  - Documentation: Simon


* Daten

  - [[https://raw.githubusercontent.com/noahjett/Movie-Goodreads-Analysis/master/books.csv]]
  - [[https://raw.githubusercontent.com/noahjett/Movie-Goodreads-Analysis/master/tmdb_5000_movies.csv]]
  - [[https://github.com/Currie32/500-Greatest-Albums/blob/master/albumlist.csv]]
  - [[https://www.kaggle.com/notgibs/500-greatest-albums-of-all-time-rolling-stone]]
    sign in, Githubversion Zeile drüber, aber ne interessante
    Seite...

* Notes

  - Movies krass umfangreich
  - Bücher ohne Erscheinungsdatum (random fake?)

* Technische Fragen

  Ein Hauptbestandteil der Aufgabe sind Suchvorgänge; Wollen wir die in
  der DB oder in Python machen?

  DB wahrscheinlich performanter, Python erlaubt Spielereien wie
  AutoComplete-Dropdown-Listen.

** Vorschlag:

   Da auch nach Teilen von Texten gesucht werden soll sind mehrfach
   Funde möglich.  Zusätzlich zu einer Gesamtliste der ausgegebenen
   Funde können deren Elemente AutoComplet-DropDown-Listen befüllen.
   Auswahl oder Eingabe bewirken erneute DB-Anfrage und Aktualisierung
   aller Listen.  Wenn DB-Rückgabe nur noch ein Datensatz ist oder ein
   Element aus Gesamtliste gewählt wird, werden alle Details geladen.
   Evtl während eines Suchvorgangs mit Views als Zwischenspeicher
   arbeiten.

   Option zum Ändern, Anlegen und Löschen bringt Problem der
   Datenkonsistenz mit sich; Vieleicht doch erstmal nur die explizit
   geforderten Punkte abarbeiten, damit wir nicht am Ende in Zeitnot
   geraten.  Eine Erweiterung für die 'Verwaltung' würde m.e. nicht
   die Struktur der Datenbank betreffen und wäre so auch im Nachhinein
   möglich.  (wenn der Python Code gut ist XD)

   Aufbau der Metadaten für Medien: Wie weit wollen wir da gehen?  Die
   obigen Datensätze sind ziemlich umfangreich. Wenn wir zum Bleistift
   mehrere Genres haben, bräuchten wir weitere n:m Beziehungen
   dafür... andererseits, warum auch nicht?^^ Falls wir mit großen
   Datensätzen arbeiten wollen, sollten wir auf jeden Fall stark auf
   Indizierung setzen.
