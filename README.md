# Bachelor Thesis an der Goethe Universität in Frankfurt am Main
_________________________________________________________________________________________
Kurzbeschreibung
Dieses Repository begleitet die Bachelorarbeit „Robuste transformatorbasierte Sprache-zu-Text-Methoden für die automatische Transkription von Interviews“.
Es umfasst den kompletten Workflow, um

  1. deutschsprachige Audiodateien vorzubereiten,

  2. sie mittels VST-Plugins künstlich zu verfremden,

  3. ein vortrainiertes Wav2Vec 2.0 XLS-R-300 M-Modell feinzujustieren und

  4. die resultierenden Word-Error-Rates (WER) zu analysieren.
________________________________________________________________________________________


Verzeichnisstruktur

<img width="814" height="438" alt="image" src="https://github.com/user-attachments/assets/47433659-5495-4dc1-b83a-43e85986c5e5" />

________________________________________________________________________________________


### Voraussetzungen
  1.  Python ≥ 3.9

  2.  GPU mit ≥ 8 GB VRAM empfohlen

  3.  Wichtige Pakete (werden in den Notebooks via pip install nachgezogen):
      transformers>=4.28 - datasets - torch/torchaudio - librosa - jiwer - pydub - pedalboard - seaborn - matplotlib
_______________________________________________________________________________________

### Workflow – Schritt für Schritt
  1.  Daten vorbereiten
      Notebook Audioformat.ipynb
      .  Konvertiert alle .mp3-Dateien aus Common Voice DE in 16-kHz-WAV.

  2. Audio künstlich verfremden
     Skripte first_input_of_plugings.py → second_input_of_plugins.py → third_input_of_plugins.py
     .  Wenden sukzessiv drei Pedalboard-Ketten an (EQ, Reverb, Chorus, Distortion u.​a.).
     .  Erzeugen jeweils neue Dateien Con1_…, Con2_…, Con3_….

  3. Effekte visualisieren
    Notebook The_effect.ipynb
    .  Zeigt Rohwellenform, Spektrogramm und Energiekurven vor/nach jedem Plugin-Schritt.

  4. ASR-Modell feinjustieren & bewerten
     .  Notebook Trainer.ipynb
     .  Lädt facebook/wav2vec2-xls-r-300m.
     .  Erstellt CTC-Tokenizer mit deutschem Alphabet.
     .  Trainiert auf sauberem und verfremdetem Common-Voice-German-Subset.
     .  Misst WER auf allen drei Störstufen.
________________________________________________________________________________________

### Ergebnisse

Die erzielten WER-Kennzahlen werden nach Abschluss von Trainer.ipynb automatisch ausgegeben und können dort abgelesen werden. Durch progressive Datenverfremdung steigt erwartungsgemäß der Fehler­anteil; das Fine-Tuning reduziert diesen jedoch signifikant auf allen Stufen.

### Reproduzierbarkeit
Alle Zwischenschritte, Hyperparameter und Metriken werden in den Notebooks abgespeichert.
Um einen Lauf von Grund auf neu zu starten, löschen Sie ggf. lokale Modell-/Cache-Verzeichnisse und führen Sie die Notebooks erneut aus.
______________________________________________________________________________________

### Lizenz
  1.  Quellcode: MIT
  2.  Audiodaten (Common Voice): Mozilla Public License 2.0
  3.  Vortrainiertes Modell: (Meta AI)
______________________________________________________________________________________


### Kontakt
Mahmoud Alhag Ali
E-Mail: mahmoudalhagali97@gmail.com

Viel Erfolg beim Nachvollziehen und Weiterentwickeln!




