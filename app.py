import streamlit as st
import pandas as pd

# Configurazione della pagina
st.set_page_config(
    page_title="Portafogli Modello - Esempi di Investimento",
    page_icon="📊",
    layout="wide"
)

# Titolo principale
st.title("📊 Esplora i Nostri Portafogli Modello")

# Introduzione
st.markdown("""
Benvenuto nella sezione dedicata agli **esempi di portafogli d'investimento**. 

Qui troverai esempi di portafogli diversificati costruiti con ETF UCITS, 
suddivisi per profilo di rischio (Basso, Medio, Alto). Questi portafogli sono 
pensati come **spunti didattici** per comprendere come costruire una strategia 
d'investimento bilanciata.

⚠️ **IMPORTANTE**: Queste informazioni sono fornite **a scopo puramente educativo** 
e non costituiscono consulenza finanziaria personalizzata. Prima di investire, 
fai sempre le tue ricerche e, se necessario, consulta un consulente finanziario 
professionale.
""")

st.divider()

# Definizione dei dati degli ETF
def get_portafogli_data():
    """Restituisce i dati strutturati dei portafogli modello"""
    
    portafogli = {
        "basso_rischio": {
            "titolo": "🛡️ Portafogli a Basso Rischio",
            "descrizione": """
            Questi portafogli sono orientati alla **stabilità** e alla **protezione del capitale**, 
            con una minore esposizione al mercato azionario. Ideali per chi ha un orizzonte 
            temporale breve-medio o bassa tolleranza al rischio.
            """,
            "portafogli": [
                {
                    "nome": "Basso Rischio 1 - ETF Unico (Orizzonte 7+ anni)",
                    "descrizione": """
                    Un ETF multi-asset bilanciato che investe in azioni e obbligazioni globali. 
                    Adatto a chi cerca **massima semplicità** con un rischio contenuto e un 
                    orizzonte temporale di almeno 7 anni.
                    """,
                    "componenti": [
                        {
                            "nome": "Vanguard LifeStrategy 40% Equity UCITS ETF Accumulating",
                            "isin": "IE00BMVB5P51",
                            "ter": "0.25%",
                            "tipo_asset": "Multi-Asset Bilanciato",
                            "allocazione": "100%",
                            "descrizione_breve": "Investimento globale con 40% azioni e 60% obbligazioni",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BMVB5P51"
                        }
                    ]
                },
                {
                    "nome": "Basso Rischio 2 - Multi-ETF (Orizzonte 5-7 anni)",
                    "descrizione": """
                    Portafoglio diversificato con **obbligazioni governative a breve e media scadenza**, 
                    una componente di oro per protezione e una quota azionaria ridotta con focus 
                    su bassa volatilità. Ideale per orizzonti temporali di 5-7 anni.
                    """,
                    "componenti": [
                        {
                            "nome": "SPDR Bloomberg 1-3 Year Euro Government Bond UCITS ETF",
                            "isin": "IE00B6YX5F63",
                            "ter": "0.15%",
                            "tipo_asset": "Obbligazionario Governativo EUR (1-3 anni)",
                            "allocazione": "30%",
                            "descrizione_breve": "Titoli di stato eurozona a breve scadenza",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B6YX5F63"
                        },
                        {
                            "nome": "Amundi Euro Government Bond 3-5Y UCITS ETF",
                            "isin": "LU1650488494",
                            "ter": "0.15%",
                            "tipo_asset": "Obbligazionario Governativo EUR (3-5 anni)",
                            "allocazione": "20%",
                            "descrizione_breve": "Titoli di stato eurozona a media scadenza",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=LU1650488494"
                        },
                        {
                            "nome": "iShares EUR Government Bond 0-1yr UCITS ETF",
                            "isin": "IE00B3FH7618",
                            "ter": "0.07%",
                            "tipo_asset": "Obbligazionario Governativo EUR (0-1 anno)",
                            "allocazione": "15%",
                            "descrizione_breve": "Titoli di stato eurozona a brevissima scadenza",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B3FH7618"
                        },
                        {
                            "nome": "Xtrackers MSCI World UCITS ETF 1C",
                            "isin": "IE00BJ0KDQ92",
                            "ter": "0.12%",
                            "tipo_asset": "Azionario Globale",
                            "allocazione": "15%",
                            "descrizione_breve": "Azioni globali paesi sviluppati",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BJ0KDQ92"
                        },
                        {
                            "nome": "iShares Edge MSCI World Minimum Volatility UCITS ETF USD (Acc)",
                            "isin": "IE00B8FHGS14",
                            "ter": "0.30%",
                            "tipo_asset": "Azionario Globale Min. Volatilità",
                            "allocazione": "10%",
                            "descrizione_breve": "Azioni globali a bassa volatilità",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B8FHGS14"
                        },
                        {
                            "nome": "iShares Physical Gold ETC",
                            "isin": "IE00B4ND3602",
                            "ter": "0.12%",
                            "tipo_asset": "Oro Fisico",
                            "allocazione": "10%",
                            "descrizione_breve": "Oro fisico per protezione e diversificazione",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B4ND3602"
                        }
                    ]
                },
                {
                    "nome": "Basso Rischio 3 - Target 2029 (Orizzonte ~3 anni)",
                    "descrizione": """
                    Portafoglio con **ETF a scadenza definita (Target Maturity 2029)**, ideale per chi 
                    ha un orizzonte temporale preciso di circa 3 anni. Combina obbligazioni corporate 
                    e governative con scadenza nel 2029.
                    """,
                    "componenti": [
                        {
                            "nome": "iShares iBonds Dec 2029 Term EUR Corporate UCITS ETF",
                            "isin": "IE000IHURBR0",
                            "ter": "0.12%",
                            "tipo_asset": "Obbligazionario Corporate EUR (Target 2029)",
                            "allocazione": "50%",
                            "descrizione_breve": "Obbligazioni corporate EUR con scadenza dicembre 2029",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE000IHURBR0"
                        },
                        {
                            "nome": "Xtrackers II Target Maturity Sept 2029 Italy and Spain Government Bond UCITS ETF 1C",
                            "isin": "LU0484969463",
                            "ter": "0.12%",
                            "tipo_asset": "Obbligazionario Governativo EUR (Target 2029)",
                            "allocazione": "50%",
                            "descrizione_breve": "Titoli di stato Italia e Spagna con scadenza settembre 2029",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=LU0484969463"
                        }
                    ]
                }
            ]
        },
        "medio_rischio": {
            "titolo": "⚖️ Portafogli a Medio Rischio",
            "descrizione": """
            Questi portafogli cercano un **equilibrio tra crescita del capitale e moderazione del rischio**. 
            Adatti a chi ha un orizzonte temporale di almeno 10 anni e accetta una moderata volatilità 
            per ottenere rendimenti potenzialmente più elevati.
            """,
            "portafogli": [
                {
                    "nome": "Medio Rischio 1 - ETF Unico (Orizzonte 10+ anni)",
                    "descrizione": """
                    Un ETF multi-asset con una **maggiore esposizione azionaria (60%)**, per chi cerca 
                    un buon compromesso tra semplicità e potenziale di rendimento con un orizzonte 
                    temporale lungo.
                    """,
                    "componenti": [
                        {
                            "nome": "Vanguard LifeStrategy 60% Equity UCITS ETF Accumulating",
                            "isin": "IE00BMVB5R75",
                            "ter": "0.25%",
                            "tipo_asset": "Multi-Asset Bilanciato",
                            "allocazione": "100%",
                            "descrizione_breve": "Investimento globale con 60% azioni e 40% obbligazioni",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BMVB5R75"
                        }
                    ]
                },
                {
                    "nome": "Medio Rischio 2 - Multi-ETF Bilanciato (Orizzonte 10+ anni)",
                    "descrizione": """
                    Portafoglio diversificato con **60% azionario globale**, obbligazioni corporate 
                    e governative a breve termine, e oro per protezione. Equilibrio tra crescita 
                    e stabilità.
                    """,
                    "componenti": [
                        {
                            "nome": "Amundi Prime All Country World UCITS ETF Acc",
                            "isin": "IE0003XJA0J9",
                            "ter": "0.07%",
                            "tipo_asset": "Azionario Globale (Sviluppati + Emergenti)",
                            "allocazione": "60%",
                            "descrizione_breve": "Azioni globali paesi sviluppati ed emergenti",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE0003XJA0J9"
                        },
                        {
                            "nome": "Vanguard EUR Corporate Bond UCITS ETF Accumulating",
                            "isin": "IE00BGYWT403",
                            "ter": "0.07%",
                            "tipo_asset": "Obbligazionario Corporate EUR",
                            "allocazione": "15%",
                            "descrizione_breve": "Obbligazioni corporate investment grade in euro",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BGYWT403"
                        },
                        {
                            "nome": "iShares Euro Government Bond 1-3yr UCITS ETF (Acc)",
                            "isin": "IE00B3VTMJ91",
                            "ter": "0.15%",
                            "tipo_asset": "Obbligazionario Governativo EUR (1-3 anni)",
                            "allocazione": "15%",
                            "descrizione_breve": "Titoli di stato eurozona a breve scadenza",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B3VTMJ91"
                        },
                        {
                            "nome": "iShares Physical Gold ETC",
                            "isin": "IE00B4ND3602",
                            "ter": "0.12%",
                            "tipo_asset": "Oro Fisico",
                            "allocazione": "10%",
                            "descrizione_breve": "Oro fisico per protezione e diversificazione",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B4ND3602"
                        }
                    ]
                },
                {
                    "nome": "Medio Rischio 3 - Diversificato con Real Estate e Inflation-Linked (Orizzonte 10+ anni)",
                    "descrizione": """
                    Portafoglio **altamente diversificato** con esposizione a mercati sviluppati ed emergenti, 
                    immobiliare europeo, oro, obbligazioni inflation-linked e governative a diverse scadenze. 
                    Pensato per protezione inflazione e decorrelazione.
                    """,
                    "componenti": [
                        {
                            "nome": "UBS Core MSCI World UCITS ETF USD acc",
                            "isin": "IE00BD4TXV59",
                            "ter": "0.06%",
                            "tipo_asset": "Azionario Globale Paesi Sviluppati",
                            "allocazione": "50%",
                            "descrizione_breve": "Azioni globali paesi sviluppati (replica ottimizzata)",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BD4TXV59"
                        },
                        {
                            "nome": "iShares Core MSCI Emerging Markets IMI UCITS ETF (Acc)",
                            "isin": "IE00BKM4GZ66",
                            "ter": "0.18%",
                            "tipo_asset": "Azionario Mercati Emergenti",
                            "allocazione": "5%",
                            "descrizione_breve": "Azioni mercati emergenti (large, mid e small cap)",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BKM4GZ66"
                        },
                        {
                            "nome": "Xtrackers FTSE EPRA/NAREIT Developed Europe Real Estate UCITS ETF 1C",
                            "isin": "LU0489337690",
                            "ter": "0.33%",
                            "tipo_asset": "Immobiliare Europa",
                            "allocazione": "5%",
                            "descrizione_breve": "REIT e società immobiliari europee",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=LU0489337690"
                        },
                        {
                            "nome": "Invesco Physical Gold A",
                            "isin": "IE00B579F325",
                            "ter": "0.12%",
                            "tipo_asset": "Oro Fisico",
                            "allocazione": "10%",
                            "descrizione_breve": "Oro fisico per protezione",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B579F325"
                        },
                        {
                            "nome": "iShares Euro Inflation Linked Government Bond UCITS ETF",
                            "isin": "IE00B0M62X26",
                            "ter": "0.09%",
                            "tipo_asset": "Obbligazionario Inflation-Linked EUR",
                            "allocazione": "10%",
                            "descrizione_breve": "Obbligazioni governative eurozona indicizzate all'inflazione",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B0M62X26"
                        },
                        {
                            "nome": "SPDR Bloomberg 1-3 Year Euro Government Bond UCITS ETF",
                            "isin": "IE00B6YX5F63",
                            "ter": "0.15%",
                            "tipo_asset": "Obbligazionario Governativo EUR (1-3 anni)",
                            "allocazione": "10%",
                            "descrizione_breve": "Titoli di stato eurozona a breve scadenza",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B6YX5F63"
                        },
                        {
                            "nome": "Amundi Euro Government Bond 10-15Y UCITS ETF Acc",
                            "isin": "LU1650489385",
                            "ter": "0.15%",
                            "tipo_asset": "Obbligazionario Governativo EUR (10-15 anni)",
                            "allocazione": "10%",
                            "descrizione_breve": "Titoli di stato eurozona a lunga scadenza",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=LU1650489385"
                        }
                    ]
                }
            ]
        },
        "alto_rischio": {
            "titolo": "🚀 Portafogli ad Alto Rischio",
            "descrizione": """
            Questi portafogli sono orientati alla **massima crescita del capitale** nel lungo periodo, 
            accettando un'alta volatilità. Adatti a chi ha un orizzonte temporale lungo (10+ anni) 
            e alta tolleranza alle fluttuazioni di mercato.
            """,
            "portafogli": [
                {
                    "nome": "Alto Rischio 1 - ETF Unico 100% Azionario Globale",
                    "descrizione": """
                    Un ETF **100% azionario globale** che include paesi sviluppati ed emergenti. 
                    Massima semplicità per chi cerca esposizione completa ai mercati azionari mondiali.
                    """,
                    "componenti": [
                        {
                            "nome": "SPDR MSCI All Country World UCITS ETF (Acc)",
                            "isin": "IE00B44Z5B48",
                            "ter": "0.12%",
                            "tipo_asset": "Azionario Globale (Sviluppati + Emergenti)",
                            "allocazione": "100%",
                            "descrizione_breve": "Azioni globali paesi sviluppati ed emergenti",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00B44Z5B48"
                        }
                    ]
                },
                {
                    "nome": "Alto Rischio 2 - Factor Investing (Value, Momentum, Quality)",
                    "descrizione": """
                    Portafoglio basato su **strategie factor investing** che combinano i fattori 
                    Value, Momentum e Quality per cercare di sovraperformare il mercato nel lungo termine, 
                    con una componente di oro per decorrelazione.
                    """,
                    "componenti": [
                        {
                            "nome": "iShares Edge MSCI World Value Factor UCITS ETF",
                            "isin": "IE00BP3QZB59",
                            "ter": "0.25%",
                            "tipo_asset": "Azionario Globale Factor Value",
                            "allocazione": "30%",
                            "descrizione_breve": "Azioni globali selezionate per fattore Value",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BP3QZB59"
                        },
                        {
                            "nome": "Xtrackers MSCI World Momentum UCITS ETF 1C",
                            "isin": "IE00BL25JP72",
                            "ter": "0.25%",
                            "tipo_asset": "Azionario Globale Factor Momentum",
                            "allocazione": "30%",
                            "descrizione_breve": "Azioni globali selezionate per fattore Momentum",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BL25JP72"
                        },
                        {
                            "nome": "Xtrackers MSCI World Quality UCITS ETF 1C",
                            "isin": "IE00BL25JL35",
                            "ter": "0.25%",
                            "tipo_asset": "Azionario Globale Factor Quality",
                            "allocazione": "25%",
                            "descrizione_breve": "Azioni globali selezionate per fattore Quality",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BL25JL35"
                        },
                        {
                            "nome": "WisdomTree Core Physical Gold",
                            "isin": "JE00BN2CJ301",
                            "ter": "0.12%",
                            "tipo_asset": "Oro Fisico",
                            "allocazione": "15%",
                            "descrizione_breve": "Oro fisico per decorrelazione",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=JE00BN2CJ301"
                        }
                    ]
                },
                {
                    "nome": "Alto Rischio 3 - Azionario Bilanciato USA/Ex-USA con Bond Eurozona",
                    "descrizione": """
                    Portafoglio **80% azionario** con bilanciamento tra mercato USA e resto del mondo 
                    (ex-USA), più una componente obbligazionaria governativa eurozona per 
                    stabilizzazione e diversificazione valutaria.
                    """,
                    "componenti": [
                        {
                            "nome": "Xtrackers MSCI World ex USA UCITS ETF 1C",
                            "isin": "IE0006WW1TQ4",
                            "ter": "0.12%",
                            "tipo_asset": "Azionario Globale ex-USA",
                            "allocazione": "40%",
                            "descrizione_breve": "Azioni paesi sviluppati escluso USA",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE0006WW1TQ4"
                        },
                        {
                            "nome": "SPDR S&P 500 UCITS ETF (Acc)",
                            "isin": "IE000XZSV718",
                            "ter": "0.03%",
                            "tipo_asset": "Azionario USA Large Cap",
                            "allocazione": "40%",
                            "descrizione_breve": "500 maggiori aziende USA",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE000XZSV718"
                        },
                        {
                            "nome": "Vanguard EUR Eurozone Government Bond UCITS ETF Accumulating",
                            "isin": "IE00BH04GL39",
                            "ter": "0.07%",
                            "tipo_asset": "Obbligazionario Governativo Eurozona",
                            "allocazione": "20%",
                            "descrizione_breve": "Titoli di stato eurozona tutte le scadenze",
                            "link_info": "https://www.justetf.com/it/etf-profile.html?isin=IE00BH04GL39"
                        }
                    ]
                }
            ]
        }
    }
    
    return portafogli


def mostra_portafoglio(portafoglio):
    """Visualizza i dettagli di un singolo portafoglio"""
    
    st.markdown(f"**Descrizione:** {portafoglio['descrizione']}")
    
    # Crea DataFrame con i componenti
    componenti_data = []
    for comp in portafoglio['componenti']:
        componenti_data.append({
            "Nome ETF": comp['nome'],
            "ISIN": comp['isin'],
            "TER": comp['ter'],
            "Tipo Asset": comp['tipo_asset'],
            "Allocazione": comp['allocazione'],
            "Descrizione": comp['descrizione_breve']
        })
    
    df = pd.DataFrame(componenti_data)
    
    # Mostra la tabella
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    # Link per maggiori informazioni
    st.markdown("**🔗 Link per approfondimenti:**")
    for comp in portafoglio['componenti']:
        st.markdown(f"- [{comp['nome']}]({comp['link_info']})")
    
    # Calcolo TER medio ponderato (se multi-ETF)
    if len(portafoglio['componenti']) > 1:
        ter_medio = sum(
            float(comp['ter'].replace('%', '')) * float(comp['allocazione'].replace('%', '')) / 100
            for comp in portafoglio['componenti']
        )
        st.info(f"💰 **TER medio ponderato del portafoglio:** {ter_medio:.2f}%")


# Sidebar per navigazione
st.sidebar.title("📋 Navigazione")
st.sidebar.markdown("""
Scegli il profilo di rischio più adatto alle tue esigenze:
- **Basso Rischio**: Stabilità e protezione (3-7+ anni)
- **Medio Rischio**: Equilibrio crescita/stabilità (10+ anni)
- **Alto Rischio**: Massima crescita di lungo periodo (10+ anni)
""")

profilo_selezionato = st.sidebar.radio(
    "Vai alla sezione:",
    ["Tutti i Portafogli", "Basso Rischio", "Medio Rischio", "Alto Rischio"]
)

# Carica i dati
portafogli_data = get_portafogli_data()

# Funzione per mostrare una categoria di portafogli
def mostra_categoria(categoria_key, categoria_data):
    st.header(categoria_data['titolo'])
    st.markdown(categoria_data['descrizione'])
    
    for i, portafoglio in enumerate(categoria_data['portafogli'], 1):
        with st.expander(f"📁 {portafoglio['nome']}", expanded=(i == 1)):
            mostra_portafoglio(portafoglio)
    
    st.divider()


# Mostra i portafogli in base alla selezione
if profilo_selezionato == "Tutti i Portafogli":
    mostra_categoria("basso_rischio", portafogli_data["basso_rischio"])
    mostra_categoria("medio_rischio", portafogli_data["medio_rischio"])
    mostra_categoria("alto_rischio", portafogli_data["alto_rischio"])
elif profilo_selezionato == "Basso Rischio":
    mostra_categoria("basso_rischio", portafogli_data["basso_rischio"])
elif profilo_selezionato == "Medio Rischio":
    mostra_categoria("medio_rischio", portafogli_data["medio_rischio"])
elif profilo_selezionato == "Alto Rischio":
    mostra_categoria("alto_rischio", portafogli_data["alto_rischio"])


# Disclaimer finale
st.markdown("---")
st.warning("""
### ⚠️ Disclaimer Importante

Queste informazioni sono fornite **esclusivamente a scopo educativo e informativo**. 
I portafogli presentati sono **esempi teorici** e non costituiscono:

- Consulenza finanziaria personalizzata
- Raccomandazioni di investimento
- Garanzie di rendimento futuro

**Prima di investire:**
1. Valuta attentamente la tua situazione finanziaria personale
2. Considera il tuo orizzonte temporale e la tua tolleranza al rischio
3. Fai le tue ricerche approfondite sui prodotti finanziari
4. Consulta un consulente finanziario professionale se necessario

I rendimenti passati non sono indicativi dei rendimenti futuri. Ogni investimento comporta rischi, 
inclusa la possibile perdita del capitale investito.
""")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>App creata a scopo didattico • Dati aggiornati a Dicembre 2025 • 
    Verifica sempre le informazioni più recenti sui siti ufficiali degli emittenti</small>
</div>
""", unsafe_allow_html=True)
