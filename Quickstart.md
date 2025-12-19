# 🚀 Guida Rapida - Portfolio ETF Explorer

Benvenuto! Questa guida ti aiuterà a iniziare in meno di 5 minuti.

## ⚡ Avvio Rapido (3 Comandi)

```bash
# 1. Installa dipendenze
pip install -r requirements.txt

# 2. Avvia l'app
streamlit run app.py

# 3. Apri il browser (si aprirà automaticamente)
# http://localhost:8501
```

Fatto! 🎉

## 📱 Cosa Puoi Fare Subito

### 1️⃣ Esplora i Portafogli

Nella **sidebar** a sinistra:
- Scegli una modalità di visualizzazione
- Applica filtri per livello di rischio
- Filtra per portafogli ESG o single ETF

### 2️⃣ Visualizza i Dettagli

Clicca su un portafoglio per vedere:
- ✅ Composizione dettagliata
- ✅ Allocazioni percentuali
- ✅ TER di ogni ETF
- ✅ Link diretti a JustETF

### 3️⃣ Impara i Concetti

Scorri fino alla sezione **"📚 Guida Rapida"** per:
- 💡 Concetti base degli investimenti
- ⚖️ Capire i livelli di rischio
- 🎯 Scegliere il portafoglio giusto
- 📖 Glossario dei termini

## 🎯 Trova il Tuo Portafoglio Ideale

### Sei Principiante? 🆕
1. Vai a **"📁 Per Categoria"**
2. Seleziona **"⭐ Portafogli Single ETF"**
3. Scegli un portafoglio con **"Rebalance: NO"**

### Hai Esperienza? 💼
1. Vai a **"📊 Per Livello di Rischio"**
2. Seleziona il tuo livello di tolleranza
3. Confronta portafogli multi-ETF

### Vuoi Investimenti Sostenibili? 🌱
1. Attiva il filtro **"Solo portafogli ESG"** nella sidebar
2. Esplora i portafogli disponibili

## 📊 Esempio Pratico

**Scenario**: Hai 30 anni, orizzonte 15+ anni, tolleranza media al rischio.

**Passaggi**:
1. Sidebar → Seleziona **"Rischio 5 - Medio"**
2. Scorri i portafogli disponibili
3. Espandi **PORT15** (Vanguard LifeStrategy 60%)
4. Controlla TER, composizione e link
5. Clicca sul link JustETF per approfondire

## 🔧 Personalizzazione

### Aggiungere Portafogli Personalizzati

1. Apri `AzionarioPort.txt`
2. Segui il formato degli esempi esistenti
3. Salva e riavvia l'app
4. Leggi `CONTRIBUTING.md` per dettagli completi

### Modificare Portafogli Esistenti

1. Trova il portafoglio in `AzionarioPort.txt`
2. Modifica allocazioni, ETF o parametri
3. Salva e riavvia l'app

## ⚠️ Checklist Prima di Investire

Prima di investire basandoti su questi portafogli:

- [ ] Ho letto il **DISCLAIMER** nell'app?
- [ ] Ho capito il mio orizzonte temporale?
- [ ] Conosco la mia tolleranza al rischio?
- [ ] Ho verificato i dati su **JustETF**?
- [ ] Ho considerato i costi di transazione?
- [ ] Ho consultato un consulente se necessario?

## 🐛 Problemi Comuni

**L'app non si avvia?**
```bash
# Reinstalla dipendenze
pip install --upgrade streamlit pandas
streamlit run app.py
```

**Errore "Module not found"?**
```bash
# Assicurati di essere nella directory corretta
cd portfolio-etf-explorer
pip install -r requirements.txt
```

**Porto già in uso?**
```bash
# Usa un porto diverso
streamlit run app.py --server.port 8502
```

## 📚 Prossimi Passi

1. **Esplora**: Dedica 15-30 minuti a esplorare tutti i portafogli
2. **Leggi**: Studia la sezione educativa nell'app
3. **Approfondisci**: Usa i link JustETF per ogni ETF
4. **Confronta**: Crea una lista di 2-3 portafogli interessanti
5. **Ricerca**: Fai ricerche approfondite prima di investire

## 💡 Suggerimenti Pro

- 🔍 Usa i **filtri** per ridurre rapidamente le opzioni
- 📊 Confronta il **TER medio** tra portafogli simili
- 🌍 Controlla la **diversificazione geografica** negli ETF
- 📅 Considera l'**orizzonte temporale** minimo
- 🔄 Valuta la frequenza di **ribilanciamento** che puoi gestire

## 🎓 Risorse Consigliate

Dopo aver esplorato l'app:

1. [JustETF](https://www.justetf.com/it/) - Database completo ETF
2. [Bogleheads Wiki](https://www.bogleheads.org/wiki/Main_Page) - Filosofia investimento passivo
3. [Portfolio Charts](https://portfoliocharts.com/) - Analisi storiche portafogli
4. [ETF.com](https://www.etf.com/) - Notizie e analisi ETF

## ⏰ Tempistiche Stimate

- **Installazione**: 2 minuti
- **Prima esplorazione**: 15 minuti
- **Studio approfondito**: 1-2 ore
- **Ricerca pre-investimento**: 5-10 ore (consigliato)

## 🎯 Obiettivo Finale

Questa app ti aiuta a:
- ✅ Comprendere le opzioni disponibili
- ✅ Identificare portafogli adatti al tuo profilo
- ✅ Apprendere concetti di investimento
- ❌ NON sostituire la consulenza professionale

## 📞 Hai Domande?

- Leggi il **README.md** completo
- Consulta **CONTRIBUTING.md** per aggiungere portafogli
- Apri una Issue su GitHub
- Consulta un professionista per decisioni finanziarie

---

**Buon investimento responsabile! 📈**

*Ricorda: I rendimenti passati non garantiscono rendimenti futuri. Investi solo ciò che puoi permetterti di perdere.*
