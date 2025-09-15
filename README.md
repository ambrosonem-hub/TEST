# Modulo SAI - Gestione e Stampa

Questo repository contiene il modulo HTML per la gestione e stampa del SAI,
con dati caricati da un file JSON esterno (`enti_strutture.json`) generato a partire da Excel.

## 📂 Contenuto
- **modulo_completo_fixed_v2.html** → Il modulo completo (con calcoli, firme, riepilogo costi e stampa A4)
- **enti_strutture.json** → File JSON con i dati (enti, strutture, indirizzi)
- **enti_strutture.xlsx** → File Excel sorgente dei dati
- **excel_to_json.py** → Script Python per rigenerare il JSON a partire dall'Excel

## 🚀 Pubblicazione con GitHub Pages
1. Crea un repository su [GitHub](https://github.com/new)
2. Carica questi file nella root del repository
3. Vai su **Settings → Pages**
4. Imposta *Source*: `Deploy from a branch`
5. Seleziona branch `main` e cartella `/ (root)`
6. Salva → dopo circa 1 minuto avrai il link del modulo online, ad esempio:
   ```
   https://tuonome.github.io/modulo-sai/modulo_completo_fixed_v2.html
   ```

## 🔄 Aggiornare i dati
1. Modifica l'Excel `enti_strutture.xlsx`
2. Lancia lo script Python per rigenerare il JSON:
   ```bash
   python excel_to_json.py
   ```
3. Fai commit e push dei file aggiornati:
   ```bash
   git add .
   git commit -m "Aggiornati dati enti/strutture"
   git push
   ```
4. Ricarica la pagina GitHub Pages: i dati saranno aggiornati

## 💡 Note
- Su GitHub Pages il modulo funziona direttamente (usa `fetch()` per leggere `enti_strutture.json`).
- In locale, per provare i file, devi usare un piccolo server HTTP:
  ```bash
  python -m http.server 8000
  ```
  Poi apri [http://localhost:8000/modulo_completo_fixed_v2.html](http://localhost:8000/modulo_completo_fixed_v2.html)

---
✍️ Preparato per l'utilizzo con GitHub Pages
