import streamlit as st
import pandas as pd
from portfolios_data import get_all_portfolios, get_statistics

# Configurazione della pagina
st.set_page_config(
    page_title="Portafogli Modello ETF - Guida agli Investimenti",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Stili CSS personalizzati
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        margin-bottom: 1rem;
    }
    .risk-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 0.5rem;
        font-weight: bold;
        font-size: 0.9rem;
        margin-right: 0.5rem;
    }
    .risk-low {
        background-color: #90EE90;
        color: #006400;
    }
    .risk-medium {
        background-color: #FFD700;
        color: #8B4500;
    }
    .risk-high {
        background-color: #FFA07A;
        color: #8B0000;
    }
    .info-box {
        background-color: #f0f8ff;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
        margin: 1rem 0;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #ffc107;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)


def load_portfolios():
    """
    Carica i portafogli dal modulo portfolios_data
    
    Returns:
        dict: Dizionario con i portafogli organizzati per categoria
    """
    try:
        portfolios = get_all_portfolios()
        stats = get_statistics()
        st.success(f"✅ Caricati **{stats['total_portfolios']} portafogli** con successo! ({stats['unique_etfs']} ETF unici)")
        return portfolios
    except Exception as e:
        st.error(f"❌ Errore nel caricamento dei dati: {str(e)}")
        return {'multi': [], 'single': [], 'esg': []}


def get_risk_category(risk_level):
    """Restituisce la categoria di rischio basata sul livello"""
    if risk_level <= 2:
        return 'Basso'
    elif risk_level <= 5:
        return 'Medio'
    else:
        return 'Alto'


def get_risk_badge_html(risk_level):
    """Genera HTML per il badge del rischio"""
    category = get_risk_category(risk_level)
    
    if category == 'Basso':
        css_class = 'risk-low'
        icon = '🛡️'
    elif category == 'Medio':
        css_class = 'risk-medium'
        icon = '⚖️'
    else:
        css_class = 'risk-high'
        icon = '🚀'
    
    return f'<span class="risk-badge {css_class}">{icon} Rischio {risk_level} - {category}</span>'


def display_portfolio(portfolio, show_expanded=False):
    """Visualizza un singolo portafoglio in un expander"""
    
    # Titolo del portafoglio
    title = f"{portfolio['id']} - Orizzonte: {portfolio['min_duration']} anni"
    
    # Badge ESG se applicabile
    if portfolio['esg'] == 1:
        title += " 🌱"
    
    with st.expander(title, expanded=show_expanded):
        # Badge rischio
        st.markdown(get_risk_badge_html(portfolio['risk_level']), unsafe_allow_html=True)
        
        # Informazioni generali
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Orizzonte Minimo", f"{portfolio['min_duration']} anni")
        
        with col2:
            st.metric("Ribilanciamento", portfolio['rebalance'])
        
        with col3:
            n_components = len(portfolio['components'])
            st.metric("N° ETF", n_components)
        
        # Note se presenti
        if portfolio['note']:
            st.info(f"ℹ️ {portfolio['note']}")
        
        # Tabella componenti
        if portfolio['components']:
            st.markdown("**📋 Composizione del Portafoglio:**")
            
            # Prepara i dati per la tabella
            df_data = []
            for comp in portfolio['components']:
                df_data.append({
                    'Allocazione': f"{comp['percentage']}%",
                    'Nome ETF': comp['name'],
                    'ISIN': comp['isin'],
                    'TER': f"{comp['ter']}%"
                })
            
            df = pd.DataFrame(df_data)
            st.dataframe(df, use_container_width=True, hide_index=True)
            
            # Calcola TER medio ponderato
            if len(portfolio['components']) > 1:
                ter_medio = sum(
                    float(comp['ter']) * float(comp['percentage']) / 100
                    for comp in portfolio['components']
                )
                st.success(f"💰 **TER medio ponderato:** {ter_medio:.3f}%")
            else:
                st.success(f"💰 **TER:** {portfolio['components'][0]['ter']}%")
            
            # Link JustETF per ogni componente
            st.markdown("**🔗 Link di approfondimento:**")
            for comp in portfolio['components']:
                link = f"https://www.justetf.com/it/etf-profile.html?isin={comp['isin']}"
                st.markdown(f"- [{comp['name']}]({link})")


def portfolio_wizard(portfolios):
    """Wizard interattivo per trovare il portafoglio ideale"""
    
    st.header("🎯 Trova il Tuo Portafoglio Ideale")
    
    st.markdown("""
    Rispondi ad alcune domande per scoprire quale portafoglio si adatta meglio alle tue esigenze.
    Questo strumento ti aiuterà a restringere le opzioni in base al tuo profilo di investitore.
    """)
    
    st.divider()
    
    # Inizializza session state per il wizard
    if 'wizard_completed' not in st.session_state:
        st.session_state.wizard_completed = False
        st.session_state.wizard_results = None
    
    # Step 1: Orizzonte Temporale
    st.subheader("⏰ Passo 1: Orizzonte Temporale")
    st.markdown("**Quando prevedi di aver bisogno di questi soldi?**")
    
    time_horizon = st.radio(
        "Seleziona l'orizzonte:",
        [
            "Meno di 3 anni",
            "3-7 anni",
            "7-10 anni",
            "Più di 10 anni",
            "15+ anni (lungo termine)"
        ],
        index=None,
        help="L'orizzonte temporale è fondamentale per determinare il livello di rischio appropriato"
    )
    
    st.divider()
    
    # Step 2: Esperienza
    st.subheader("💼 Passo 2: Esperienza con gli Investimenti")
    st.markdown("**Quanto sei familiare con gli investimenti in ETF?**")
    
    experience = st.radio(
        "Seleziona il tuo livello:",
        [
            "Principiante - È la mia prima volta",
            "Base - Ho qualche conoscenza teorica",
            "Intermedio - Ho già investito in ETF",
            "Esperto - Investo regolarmente e comprendo i mercati"
        ],
        index=None,
        help="Questo ci aiuta a suggerirti portafogli con la complessità appropriata"
    )
    
    st.divider()
    
    # Step 3: Tolleranza al Rischio
    st.subheader("⚖️ Passo 3: Tolleranza al Rischio")
    st.markdown("**Come reagiresti se il tuo investimento perdesse il 30% in un anno?**")
    
    risk_tolerance = st.radio(
        "Seleziona la risposta più vicina al tuo comportamento:",
        [
            "😰 Venderei immediatamente per evitare ulteriori perdite",
            "😟 Sarei molto preoccupato e considererei di vendere",
            "😐 Sarei preoccupato ma probabilmente manterrei l'investimento",
            "😊 Lo vedrei come un'opportunità per comprare a prezzi più bassi",
            "🚀 Investirei di più per approfittare dei prezzi bassi"
        ],
        index=None,
        help="La tolleranza al rischio è soggettiva - sii onesto con te stesso"
    )
    
    st.divider()
    
    # Step 4: Preferenza ESG
    st.subheader("🌱 Passo 4: Investimenti Sostenibili")
    st.markdown("**Ti interessa investire secondo criteri ESG (ambientali, sociali, governance)?**")
    
    esg_preference = st.radio(
        "Seleziona la tua preferenza:",
        [
            "Sì, voglio solo portafogli ESG",
            "Mi interessa, ma non è prioritario",
            "No, non è importante per me"
        ],
        index=None,
        help="I portafogli ESG investono in aziende con migliori pratiche ambientali e sociali"
    )
    
    st.divider()
    
    # Step 5: Complessità
    st.subheader("🔧 Passo 5: Complessità e Gestione")
    st.markdown("**Quanto tempo vuoi dedicare alla gestione del portafoglio?**")
    
    complexity = st.radio(
        "Seleziona la tua disponibilità:",
        [
            "Zero - Voglio un investimento completamente automatico",
            "Minima - Al massimo una revisione annuale",
            "Moderata - Posso dedicare qualche ora ogni 3-6 mesi"
        ],
        index=None,
        help="I portafogli single ETF non richiedono ribilanciamento"
    )
    
    st.divider()
    
    # Bottone per calcolare risultati
    if st.button("🎯 Trova i Miei Portafogli Ideali", type="primary", use_container_width=True):
        if all([time_horizon, experience, risk_tolerance, esg_preference, complexity]):
            # Calcola i suggerimenti
            results = calculate_recommendations(
                portfolios,
                time_horizon,
                experience,
                risk_tolerance,
                esg_preference,
                complexity
            )
            st.session_state.wizard_results = results
            st.session_state.wizard_completed = True
            st.rerun()
        else:
            st.error("⚠️ Per favore, rispondi a tutte le domande prima di continuare.")
    
    # Mostra risultati se disponibili
    if st.session_state.wizard_completed and st.session_state.wizard_results:
        st.divider()
        display_wizard_results(st.session_state.wizard_results, portfolios)
        
        # Bottone per ricominciare
        if st.button("🔄 Ricomincia il Questionario", use_container_width=True):
            st.session_state.wizard_completed = False
            st.session_state.wizard_results = None
            st.rerun()


def calculate_recommendations(portfolios, time_horizon, experience, risk_tolerance, esg_preference, complexity):
    """Calcola i portafogli raccomandati in base alle risposte del wizard"""
    
    # Determina il livello di rischio basato su orizzonte temporale e tolleranza
    risk_mapping = {
        "Meno di 3 anni": [1, 2],
        "3-7 anni": [2, 3],
        "7-10 anni": [3, 4, 5],
        "Più di 10 anni": [4, 5, 6],
        "15+ anni (lungo termine)": [5, 6, 7, 8]
    }
    
    tolerance_adjustment = {
        "😰 Venderei immediatamente per evitare ulteriori perdite": -2,
        "😟 Sarei molto preoccupato e considererei di vendere": -1,
        "😐 Sarei preoccupato ma probabilmente manterrei l'investimento": 0,
        "😊 Lo vedrei come un'opportunità per comprare a prezzi più bassi": 1,
        "🚀 Investirei di più per approfittare dei prezzi bassi": 2
    }
    
    # Livelli di rischio base
    base_risks = risk_mapping.get(time_horizon, [3, 4, 5])
    adjustment = tolerance_adjustment.get(risk_tolerance, 0)
    
    # Applica aggiustamento
    recommended_risks = []
    for risk in base_risks:
        adjusted = risk + adjustment
        adjusted = max(1, min(8, adjusted))  # Limita tra 1 e 8
        recommended_risks.append(adjusted)
    
    # Rimuovi duplicati e ordina
    recommended_risks = sorted(set(recommended_risks))
    
    # Determina preferenza single/multi
    single_only = complexity == "Zero - Voglio un investimento completamente automatico"
    prefer_single = complexity in ["Zero - Voglio un investimento completamente automatico", 
                                    "Minima - Al massimo una revisione annuale"]
    
    # Determina preferenza ESG
    esg_only = esg_preference == "Sì, voglio solo portafogli ESG"
    prefer_esg = esg_preference == "Mi interessa, ma non è prioritario"
    
    # Determina complessità massima basata su esperienza
    max_components = {
        "Principiante - È la mia prima volta": 1,
        "Base - Ho qualche conoscenza teorica": 4,
        "Intermedio - Ho già investito in ETF": 7,
        "Esperto - Investo regolarmente e comprendo i mercati": 10
    }
    max_etfs = max_components.get(experience, 4)
    
    # Raccogli tutti i portafogli
    all_portfolios = []
    for section in portfolios.values():
        all_portfolios.extend(section)
    
    # Filtra i portafogli
    candidates = []
    for portfolio in all_portfolios:
        # Filtro rischio
        if portfolio['risk_level'] not in recommended_risks:
            continue
        
        # Filtro ESG
        if esg_only and portfolio['esg'] != 1:
            continue
        
        # Filtro numero componenti
        if len(portfolio['components']) > max_etfs:
            continue
        
        # Filtro single ETF
        if single_only and len(portfolio['components']) > 1:
            continue
        
        # Calcola score
        score = 0
        
        # Preferenza single
        if prefer_single and len(portfolio['components']) == 1:
            score += 10
        
        # Preferenza ESG
        if prefer_esg and portfolio['esg'] == 1:
            score += 5
        
        # Preferenza per nessun ribilanciamento
        if complexity == "Zero - Voglio un investimento completamente automatico":
            if portfolio['rebalance'] == 'NO':
                score += 15
        
        # Vicinanza al rischio ideale (il rischio centrale del range)
        ideal_risk = recommended_risks[len(recommended_risks)//2] if recommended_risks else 5
        risk_distance = abs(portfolio['risk_level'] - ideal_risk)
        score -= risk_distance * 2
        
        candidates.append({
            'portfolio': portfolio,
            'score': score
        })
    
    # Ordina per score
    candidates.sort(key=lambda x: x['score'], reverse=True)
    
    # Prendi i top 3
    top_portfolios = [c['portfolio'] for c in candidates[:3]]
    
    return {
        'portfolios': top_portfolios,
        'recommended_risks': recommended_risks,
        'criteria': {
            'time_horizon': time_horizon,
            'experience': experience,
            'risk_tolerance': risk_tolerance,
            'esg_preference': esg_preference,
            'complexity': complexity,
            'single_only': single_only,
            'esg_only': esg_only,
            'max_etfs': max_etfs
        }
    }


def display_wizard_results(results, all_portfolios):
    """Visualizza i risultati del wizard"""
    
    st.success("✅ Analisi completata! Ecco i portafogli più adatti al tuo profilo:")
    
    # Mostra criteri di ricerca
    with st.expander("📋 Criteri utilizzati per la selezione", expanded=False):
        criteria = results['criteria']
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown(f"""
            **Profilo Temporale:**
            - Orizzonte: {criteria['time_horizon']}
            
            **Profilo di Rischio:**
            - Tolleranza: {criteria['risk_tolerance']}
            - Livelli suggeriti: {', '.join(map(str, results['recommended_risks']))}
            
            **Esperienza:**
            - Livello: {criteria['experience']}
            - Max ETF: {criteria['max_etfs']}
            """)
        
        with col2:
            st.markdown(f"""
            **Preferenze:**
            - ESG: {criteria['esg_preference']}
            - Gestione: {criteria['complexity']}
            - Solo Single ETF: {'Sì' if criteria['single_only'] else 'No'}
            """)
    
    st.divider()
    
    # Mostra portafogli raccomandati
    if results['portfolios']:
        st.subheader("🎯 I Tuoi Portafogli Consigliati")
        
        for idx, portfolio in enumerate(results['portfolios'], 1):
            st.markdown(f"### 🏆 Raccomandazione #{idx}")
            
            # Spiega perché è stato raccomandato
            reasons = []
            
            if len(portfolio['components']) == 1:
                reasons.append("✅ **Semplicità massima** - Un solo ETF, nessun ribilanciamento")
            
            if portfolio['esg'] == 1:
                reasons.append("🌱 **ESG compliant** - Investe secondo criteri sostenibili")
            
            if portfolio['rebalance'] == 'NO':
                reasons.append("⏰ **Zero manutenzione** - Non richiede ribilanciamento")
            
            if portfolio['risk_level'] in results['recommended_risks']:
                reasons.append(f"⚖️ **Rischio appropriato** - Livello {portfolio['risk_level']} adatto al tuo profilo")
            
            if len(portfolio['components']) <= 4:
                reasons.append("📊 **Facile da gestire** - Numero limitato di componenti")
            
            if reasons:
                st.markdown("**Perché questo portafoglio:**")
                for reason in reasons:
                    st.markdown(f"- {reason}")
                st.markdown("")
            
            # Visualizza il portafoglio
            display_portfolio(portfolio, show_expanded=True)
            
            st.divider()
    
    else:
        st.warning("""
        ### ⚠️ Nessun portafoglio trovato
        
        Non ho trovato portafogli che corrispondono esattamente ai tuoi criteri. 
        Prova a:
        - Modificare le tue preferenze nel questionario
        - Esplorare manualmente i portafogli disponibili
        - Considerare portafogli con criteri leggermente diversi
        """)
    
    # Suggerimento finale
    st.info("""
    💡 **Prossimi passi:**
    1. Studia attentamente i portafogli raccomandati
    2. Clicca sui link JustETF per approfondire ogni ETF
    3. Confronta i costi (TER) e le caratteristiche
    4. Consulta un professionista prima di investire
    """)


def main():
    # Intestazione
    st.markdown('<p class="main-header">📊 Portafogli Modello ETF UCITS</p>', unsafe_allow_html=True)
    
    st.markdown("""
    Benvenuto nella guida ai **portafogli modello basati su ETF UCITS**. Questa applicazione 
    ti aiuta a esplorare diverse strategie di investimento organizzate per profilo di rischio 
    e orizzonte temporale.
    """)
    
    # Disclaimer iniziale
    st.warning("""
    ⚠️ **IMPORTANTE**: Queste informazioni sono fornite **esclusivamente a scopo educativo**. 
    Non costituiscono consulenza finanziaria personalizzata. Consulta sempre un professionista 
    prima di prendere decisioni di investimento.
    """)
    
    st.divider()
    
    # Carica i dati
    portfolios = load_portfolios()
    
    # Controlla se ci sono portafogli caricati
    total_portfolios = sum(len(portfolios[section]) for section in portfolios)
    
    if total_portfolios == 0:
        st.error("""
        ### ❌ Nessun portafoglio caricato
        
        L'applicazione non ha potuto caricare i dati dei portafogli.
        Verifica che il file `portfolios_data.py` sia presente nella stessa directory di `app.py`.
        """)
        return
    
    # Sidebar per la navigazione
    st.sidebar.title("🧭 Navigazione")
    st.sidebar.markdown("---")
    
    # Selezione modalità principale
    main_mode = st.sidebar.radio(
        "Scegli come procedere:",
        ["🎯 Guidami alla Scelta (Consigliato)", "🔍 Esplora Liberamente"],
        help="La modalità guidata ti aiuta a trovare il portafoglio ideale con domande mirate"
    )
    
    if main_mode == "🔍 Esplora Liberamente":
        st.sidebar.markdown("---")
        
        # Selezione visualizzazione
        view_type = st.sidebar.radio(
            "Modalità di visualizzazione:",
            ["📊 Per Livello di Rischio", "📁 Per Categoria", "🔍 Tutti i Portafogli"]
        )
        
        st.sidebar.markdown("---")
        
        # Filtri
        st.sidebar.subheader("🎯 Filtri")
        
        # Filtro rischio
        all_risks = sorted(set(
            p['risk_level'] 
            for section in portfolios.values() 
            for p in section
        ))
        
        risk_filter = st.sidebar.multiselect(
            "Livello di Rischio:",
            options=all_risks,
            default=all_risks,
            format_func=lambda x: f"Rischio {x} - {get_risk_category(x)}"
        )
        
        # Filtro ESG
        esg_filter = st.sidebar.checkbox("Solo portafogli ESG", value=False)
        
        # Filtro numero ETF
        single_only = st.sidebar.checkbox("Solo portafogli single ETF", value=False)
        
        st.sidebar.markdown("---")
        
        # Info box nella sidebar
        st.sidebar.info("""
        **📖 Legenda:**
        - 🛡️ Rischio Basso (1-2)
        - ⚖️ Rischio Medio (3-5)
        - 🚀 Rischio Alto (6-8)
        - 🌱 ESG compliant
        """)
        
        # Contenuto principale - Modalità esplorazione
        if view_type == "📊 Per Livello di Rischio":
            display_by_risk(portfolios, risk_filter, esg_filter, single_only)
        
        elif view_type == "📁 Per Categoria":
            display_by_category(portfolios, risk_filter, esg_filter, single_only)
        
        else:  # Tutti i portafogli
            display_all_portfolios(portfolios, risk_filter, esg_filter, single_only)
    
    else:
        # Modalità wizard guidato
        st.sidebar.markdown("---")
        st.sidebar.info("""
        🎯 **Modalità Guidata**
        
        Rispondi ad alcune domande per scoprire i portafogli più adatti a te.
        
        Richiede circa 2 minuti.
        """)
        
        portfolio_wizard(portfolios)
    
    # Sezione educativa
    st.divider()
    display_educational_section()
    
    # Footer con disclaimer
    display_footer()


def filter_portfolios(portfolios, risk_filter, esg_filter, single_only):
    """Applica i filtri ai portafogli"""
    filtered = {'multi': [], 'single': [], 'esg': []}
    
    for section, portfolio_list in portfolios.items():
        for portfolio in portfolio_list:
            # Filtro rischio
            if portfolio['risk_level'] not in risk_filter:
                continue
            
            # Filtro ESG
            if esg_filter and portfolio['esg'] != 1:
                continue
            
            # Filtro single ETF
            if single_only and len(portfolio['components']) > 1:
                continue
            
            filtered[section].append(portfolio)
    
    return filtered


def display_by_risk(portfolios, risk_filter, esg_filter, single_only):
    """Visualizza portafogli organizzati per livello di rischio"""
    st.header("📊 Portafogli per Livello di Rischio")
    
    filtered = filter_portfolios(portfolios, risk_filter, esg_filter, single_only)
    
    # Combina tutti i portafogli
    all_portfolios = []
    for section in filtered.values():
        all_portfolios.extend(section)
    
    # Ordina per livello di rischio
    all_portfolios.sort(key=lambda x: x['risk_level'])
    
    # Raggruppa per categoria di rischio
    risk_groups = {
        'Basso': [],
        'Medio': [],
        'Alto': []
    }
    
    for portfolio in all_portfolios:
        category = get_risk_category(portfolio['risk_level'])
        risk_groups[category].append(portfolio)
    
    # Visualizza ogni gruppo
    for category in ['Basso', 'Medio', 'Alto']:
        if risk_groups[category]:
            if category == 'Basso':
                icon = '🛡️'
                color = '#90EE90'
            elif category == 'Medio':
                icon = '⚖️'
                color = '#FFD700'
            else:
                icon = '🚀'
                color = '#FFA07A'
            
            st.markdown(f"### {icon} Rischio {category}")
            st.markdown(f"<div style='background-color: {color}; padding: 0.5rem; border-radius: 0.5rem; margin-bottom: 1rem;'>Trovati {len(risk_groups[category])} portafogli</div>", unsafe_allow_html=True)
            
            for portfolio in risk_groups[category]:
                display_portfolio(portfolio)
            
            st.divider()


def display_by_category(portfolios, risk_filter, esg_filter, single_only):
    """Visualizza portafogli organizzati per categoria"""
    st.header("📁 Portafogli per Categoria")
    
    filtered = filter_portfolios(portfolios, risk_filter, esg_filter, single_only)
    
    # Portafogli Multi-ETF
    if filtered['multi']:
        st.subheader("🎯 Portafogli Multi-ETF")
        st.markdown("Portafogli diversificati con più componenti ETF")
        for portfolio in sorted(filtered['multi'], key=lambda x: x['risk_level']):
            display_portfolio(portfolio)
        st.divider()
    
    # Portafogli Single ETF
    if filtered['single']:
        st.subheader("⭐ Portafogli Single ETF")
        st.markdown("Portafogli semplificati con un unico ETF - ideali per principianti")
        for portfolio in sorted(filtered['single'], key=lambda x: x['risk_level']):
            display_portfolio(portfolio)
        st.divider()
    
    # Portafogli ESG
    if filtered['esg']:
        st.subheader("🌱 Portafogli ESG")
        st.markdown("Portafogli con focus su criteri ambientali, sociali e di governance")
        for portfolio in sorted(filtered['esg'], key=lambda x: x['risk_level']):
            display_portfolio(portfolio)
        st.divider()
    
    # Messaggio se nessun portafoglio corrisponde ai filtri
    if not any(filtered.values()):
        st.info("Nessun portafoglio corrisponde ai filtri selezionati. Prova a modificare i criteri di ricerca.")


def display_all_portfolios(portfolios, risk_filter, esg_filter, single_only):
    """Visualizza tutti i portafogli"""
    st.header("🔍 Tutti i Portafogli")
    
    filtered = filter_portfolios(portfolios, risk_filter, esg_filter, single_only)
    
    # Combina e ordina tutti i portafogli
    all_portfolios = []
    for section in filtered.values():
        all_portfolios.extend(section)
    
    all_portfolios.sort(key=lambda x: (x['risk_level'], x['id']))
    
    if all_portfolios:
        st.info(f"Trovati **{len(all_portfolios)} portafogli** che corrispondono ai filtri selezionati")
        
        for portfolio in all_portfolios:
            display_portfolio(portfolio)
    else:
        st.warning("Nessun portafoglio corrisponde ai filtri selezionati.")


def display_educational_section():
    """Visualizza la sezione educativa"""
    st.header("📚 Guida Rapida agli Investimenti")
    
    tab1, tab2, tab3, tab4 = st.tabs([
        "💡 Concetti Base", 
        "⚖️ Livelli di Rischio", 
        "🎯 Come Scegliere", 
        "📖 Glossario"
    ])
    
    with tab1:
        st.markdown("""
        ### 💡 Concetti Base
        
        **Cos'è un ETF?**
        
        Un ETF (Exchange Traded Fund) è un fondo di investimento quotato in borsa che replica 
        l'andamento di un indice, permettendo di diversificare con un unico strumento.
        
        **Cos'è il TER?**
        
        Il TER (Total Expense Ratio) è il costo annuo totale dell'ETF espresso in percentuale. 
        Un TER dello 0,20% significa che paghi 2€ all'anno per ogni 1.000€ investiti.
        
        **Perché diversificare?**
        
        La diversificazione riduce il rischio specifico investendo in molti asset diversi. 
        Come dice il proverbio: "Non mettere tutte le uova nello stesso paniere".
        """)
    
    with tab2:
        st.markdown("""
        ### ⚖️ Comprendere i Livelli di Rischio
        
        **Rischio ≠ Probabilità di Perdita nel Lungo Periodo**
        
        Il "rischio" in questa guida si riferisce alla **volatilità** (oscillazioni di valore), 
        non alla probabilità di perdere denaro su un orizzonte di 10-15 anni.
        
        **🛡️ Rischio Basso (1-2)**
        - Volatilità: 5-15% annua
        - Drawdown tipico: -10% / -20%
        - Ideale per: Orizzonti 3-7 anni, bassa tolleranza al rischio
        
        **⚖️ Rischio Medio (3-5)**
        - Volatilità: 10-20% annua
        - Drawdown tipico: -20% / -35%
        - Ideale per: Orizzonti 7-15 anni, moderata tolleranza al rischio
        
        **🚀 Rischio Alto (6-8)**
        - Volatilità: 15-25%+ annua
        - Drawdown tipico: -30% / -50%+
        - Ideale per: Orizzonti 15+ anni, alta tolleranza al rischio
        
        **⚠️ Il Vero Rischio è Vendere nel Momento Sbagliato**
        
        La maggior parte degli investitori perde denaro non a causa del mercato, ma perché 
        vende durante i ribassi trasformando perdite temporanee in perdite permanenti.
        """)
    
    with tab3:
        st.markdown("""
        ### 🎯 Come Scegliere il Portafoglio Giusto
        
        **1. Definisci il Tuo Orizzonte Temporale**
        - Meno di 3 anni → Rischio Basso
        - 3-10 anni → Rischio Basso/Medio
        - 10+ anni → Qualsiasi livello
        
        **2. Valuta la Tua Tolleranza Emotiva**
        
        Chiediti: "Se il mio portafoglio perdesse il 30% in un anno, riuscirei a non vendere?"
        - NO → Rischio Basso/Medio
        - SÌ, ma con difficoltà → Rischio Medio
        - SÌ, tranquillamente → Rischio Alto
        
        **3. Considera la Complessità**
        - Principiante → Portafogli Single ETF (⭐)
        - Intermedio → Portafogli con 2-4 ETF (⭐⭐)
        - Avanzato → Portafogli multi-componente (⭐⭐⭐)
        
        **4. Ribilanciamento**
        - "NO" → Non richiede manutenzione
        - "1y" → Ribilanciamento annuale consigliato
        - "3M" → Ribilanciamento trimestrale (solo per esperti)
        """)
    
    with tab4:
        st.markdown("""
        ### 📖 Glossario dei Termini
        
        **UCITS**: Standard europeo per fondi che garantisce elevati livelli di protezione degli investitori
        
        **Accumulating (Acc)**: ETF che reinveste automaticamente i dividendi
        
        **TER (Total Expense Ratio)**: Costo annuo di gestione dell'ETF
        
        **ISIN**: Codice identificativo internazionale del titolo
        
        **Rebalancing**: Processo di riportare le allocazioni ai pesi obiettivo
        
        **ESG**: Environmental, Social, Governance - criteri di investimento sostenibile
        
        **Factor Investing**: Strategia che si concentra su specifici fattori (Value, Momentum, Quality, ecc.)
        
        **Duration**: Sensibilità di un'obbligazione alle variazioni dei tassi di interesse
        
        **Drawdown**: Perdita massima dal picco precedente
        
        **Volatilità**: Misura delle oscillazioni di prezzo di un asset
        """)


def display_footer():
    """Visualizza il footer con disclaimer"""
    st.divider()
    
    st.error("""
    ### ⚠️ DISCLAIMER IMPORTANTE
    
    Le informazioni contenute in questa applicazione sono fornite **esclusivamente a scopo 
    educativo e informativo**. I portafogli presentati sono esempi teorici e **NON costituiscono**:
    
    - ❌ Consulenza finanziaria personalizzata
    - ❌ Raccomandazioni di investimento
    - ❌ Garanzie di rendimento futuro
    - ❌ Analisi della tua situazione finanziaria personale
    
    **Prima di investire:**
    
    1. 📊 Valuta attentamente la tua situazione finanziaria
    2. ⏰ Considera il tuo orizzonte temporale
    3. 🧠 Analizza la tua tolleranza al rischio
    4. 🔍 Effettua ricerche approfondite sui prodotti
    5. 👨‍💼 Consulta un consulente finanziario professionista
    
    **⚠️ Rischi degli Investimenti:**
    
    - I rendimenti passati non garantiscono rendimenti futuri
    - Ogni investimento comporta il rischio di perdita del capitale
    - La volatilità può causare perdite temporanee significative
    - I dati potrebbero non essere aggiornati
    
    **Verifica sempre le informazioni più recenti sui siti ufficiali degli emittenti prima di investire.**
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p><strong>Portfolio ETF Explorer</strong> | Versione 3.0 (Wizard Edition) | Dicembre 2025</p>
        <p><small>Applicazione educativa - Non costituisce consulenza finanziaria</small></p>
        <p><small>Dati da portfolios_data.py - Verifica sempre presso fonti ufficiali</small></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
