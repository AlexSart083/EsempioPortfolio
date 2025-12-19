# 📊 Portfolio ETF Explorer - Guida ai Portafogli Modello

Applicazione web interattiva per esplorare portafogli di investimento basati su ETF UCITS, organizzati per profilo di rischio e categoria.

## 🌟 Caratteristiche Principali

- **Parser Automatico**: Legge e organizza automaticamente i dati da `AzionarioPort.txt`
- **3 Modalità di Visualizzazione**: Per rischio, per categoria, o vista completa
- **Filtri Avanzati**: Filtra per livello di rischio, ESG, numero di ETF
- **Interfaccia Intuitiva**: Design moderno con badge colorati e layout responsive
- **Sezione Educativa**: Guida completa ai concetti di investimento
- **Link Diretti**: Collegamenti a JustETF per ogni ETF

## 🚀 Come Avviare l'Applicazione

### Prerequisiti

- Python 3.8 o superiore
- pip (package manager Python)

### Installazione Locale

1. **Clona o scarica il repository**

2. **Installa le dipendenze**
   ```bash
   pip install -r requirements.txt
   ```

3. **Avvia l'applicazione**
   ```bash
   streamlit run app.py
   ```

4. **Apri il browser**
   L'app si aprirà automaticamente su `http://localhost:8501`

### Esecuzione con Docker (opzionale)

```bash
docker build -t portfolio-etf .
docker run -p 8501:8501 portfolio-etf
```

## 📁 Struttura del Progetto

```
.
├── app.py                      # Applicazione Streamlit principale
├── AzionarioPort.txt          # Database portafogli (formato strutturato)
├── requirements.txt           # Dipendenze Python
├── README.md                  # Questo file
└── .devcontainer/
    └── devcontainer.json      # Configurazione Dev Container
```

## 📊 Organizzazione dei Dati

I portafogli sono organizzati in 3 categorie:

### 🎯 Multi Portfolios
Portafogli diversificati con più ETF (2-7 componenti)
- Adatti a investitori con esperienza
- Richiedono ribilanciamento periodico
- Maggiore flessibilità di allocazione

### ⭐ Single Portfolios
Portafogli con un singolo ETF multi-asset
- Ideali per principianti
- Nessun ribilanciamento necessario
- Massima semplicità

### 🌱 ESG Portfolios
Portafogli con focus sostenibile
- Criteri ambientali, sociali e di governance
- ETF ESG-compliant
- Vari livelli di rischio disponibili

## 🎯 Livelli di Rischio

| Livello | Categoria | Volatilità | Orizzonte Minimo | Profilo Investitore |
|---------|-----------|------------|------------------|---------------------|
| 1-2 | 🛡️ Basso | 5-15% | 3-7 anni | Conservativo |
| 3-5 | ⚖️ Medio | 10-20% | 7-15 anni | Moderato |
| 6-8 | 🚀 Alto | 15-25%+ | 15+ anni | Aggressivo |

## 🔧 Funzionalità dell'App

### Filtri Disponibili

- **Livello di Rischio**: Seleziona uno o più livelli (1-8)
- **Solo ESG**: Mostra solo portafogli sostenibili
- **Single ETF**: Filtra portafogli con un solo ETF

### Modalità di Visualizzazione

1. **Per Livello di Rischio**: Raggruppa portafogli per categoria di rischio (Basso/Medio/Alto)
2. **Per Categoria**: Organizza per tipo (Multi/Single/ESG)
3. **Tutti i Portafogli**: Vista completa con tutti i portafogli disponibili

### Informazioni Visualizzate

Per ogni portafoglio:
- Badge del livello di rischio
- Orizzonte temporale minimo
- Frequenza di ribilanciamento
- Numero di componenti ETF
- Composizione dettagliata con allocazioni
- TER (Total Expense Ratio) per ogni ETF
- TER medio ponderato (per portafogli multi-ETF)
- Link diretti a JustETF per approfondimenti

## 📚 Sezione Educativa

L'app include 4 tab educative:

1. **💡 Concetti Base**: Introduzione a ETF, TER, diversificazione
2. **⚖️ Livelli di Rischio**: Spiegazione dettagliata della volatilità
3. **🎯 Come Scegliere**: Guida passo-passo alla selezione
4. **📖 Glossario**: Definizioni dei termini tecnici

## 🌐 Deploy Online

### Streamlit Community Cloud (Consigliato - Gratuito)

1. Carica il progetto su **GitHub**
2. Vai su [share.streamlit.io](https://share.streamlit.io)
3. Connetti il tuo account GitHub
4. Seleziona il repository
5. Imposta il file principale: `app.py`
6. Clicca su **Deploy**!

### Heroku

```bash
# Installa Heroku CLI
heroku login
heroku create nome-app
git push heroku main
```

### Railway

1. Vai su [railway.app](https://railway.app)
2. Connetti il repository GitHub
3. Deploy automatico

## 🔄 Aggiornare i Dati

Per aggiornare i portafogli:

1. Modifica il file `AzionarioPort.txt`
2. Mantieni il formato:
   ```
   PORTxx - Risk X, ESG X, MinDurY X Rebalance XX
   XX% Nome ETF ISIN TER
   XX% Nome ETF ISIN TER
   ```
3. L'app ricaricherà automaticamente i nuovi dati

### Formato del File di Dati

```
Multi Portfolios

PORT2a - Risk 2, ESG 0, MinDurY 5 Rebalance 1y
10% SPDR MSCI World UCITS ETF IE00BFY0GT14 0,12
20% Amundi Smart Overnight Return UCITS ETF Acc LU1190417599 0,10

Single

PORT13 - Risk 3, ESG 0, MinDurY 7
Vanguard LifeStrategy 40% Equity UCITS ETF Accumulating IE00BMVB5M21 0,25

ESG

PORT27 - Risk 7, ESG 1, MinDurY 10
iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc) IE00B8KGV557 0,2
```

## 🛠️ Tecnologie Utilizzate

- **Streamlit** 1.28+ - Framework per web app interattive
- **Pandas** 2.0+ - Analisi e manipolazione dati
- **Python** 3.8+ - Linguaggio di programmazione

## 🔐 Privacy e Sicurezza

- ✅ Nessun dato personale raccolto
- ✅ Nessun tracking degli utenti
- ✅ Nessun cookie
- ✅ Open source e trasparente

## ⚠️ Disclaimer Importante

**Questa applicazione è fornita esclusivamente a scopo educativo.**

- ❌ NON costituisce consulenza finanziaria
- ❌ NON è una raccomandazione di investimento
- ❌ I dati potrebbero non essere aggiornati
- ✅ Verifica sempre con fonti ufficiali prima di investire
- ✅ Consulta un professionista per decisioni finanziarie

## 🐛 Segnalazione Bug

Se trovi un bug o hai un suggerimento:

1. Apri una Issue su GitHub
2. Descrivi il problema con dettagli
3. Includi screenshot se possibile

## 📝 Licenza

Questo progetto è rilasciato a scopo educativo. Sentiti libero di usarlo e modificarlo per i tuoi scopi di apprendimento.

## 🤝 Contribuire

I contributi sono benvenuti! Per contribuire:

1. Fai un Fork del progetto
2. Crea un branch per la tua feature (`git checkout -b feature/AmazingFeature`)
3. Commit le tue modifiche (`git commit -m 'Add some AmazingFeature'`)
4. Push al branch (`git push origin feature/AmazingFeature`)
5. Apri una Pull Request

## 📞 Contatti

Per domande o suggerimenti, apri una Issue su GitHub.

## 🙏 Ringraziamenti

- Dati ETF da fonti pubbliche
- JustETF per i link di approfondimento
- Community Streamlit per il framework

---

**Nota**: I rendimenti passati non sono indicativi di rendimenti futuri. Investi in modo responsabile.

**Versione**: 2.0 | **Data**: Dicembre 2025
