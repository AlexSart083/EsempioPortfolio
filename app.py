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
    .risk-very-high {
        background-color: #8B0000;
        color: #FFFFFF;
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
    elif risk_level <= 7:
        return 'Alto'
    else:  # risk_level == 8
        return 'Molto Alto'


def get_risk_badge_html(risk_level):
    """Genera HTML per il badge del rischio"""
    category = get_risk_category(risk_level)
    
    if category == 'Basso':
        css_class = 'risk-low'
        icon = '🛡️'
    elif category == 'Medio':
        css_class = 'risk-medium'
        icon = '⚖️'
    elif category == 'Alto':
        css_class = 'risk-high'
        icon = '🚀'
    else:  # Molto Alto
        css_class = 'risk-very-high'
        icon = '⚡'
    
    return f'<span class="risk-badge {css_class}">{icon} Rischio {risk_level} - {category}</span>'


def display_portfolio(portfolio, show_expanded=False):
    """Visualizza un singolo portafoglio in un expander"""
    
    # Titolo del portafoglio con nome friendly
    title = f"{portfolio['name']}"
    
    # Badge ESG se applicabile
    if portfolio['esg'] == 1:
        title += " 🌱"
    
    with st.expander(title, expanded=show_expanded):
        # ID tecnico piccolo in alto
        st.caption(f"ID Tecnico: {portfolio['id']} | Orizzonte minimo: {portfolio['min_duration']} anni")
        
        # Badge rischio
        st.markdown(get_risk_badge_html(portfolio['risk_level']), unsafe_allow_html=True)
        
        # Descrizione strategia (NUOVO)
        st.markdown("### 🎯 Strategia")
        st.info(portfolio['strategy_description'])
        
        # Warning speciale per rischio 8
        if portfolio['risk_level'] == 8:
            st.error("""
            ⚠️ **ATTENZIONE: PORTAFOGLIO CON LEVERAGE (2x)**
            
            Questo portafoglio utilizza strumenti con leva finanziaria che amplificano sia i guadagni che le perdite.
            
            **Rischi Principali:**
            - ❌ NON adatto a principianti
            - ❌ Richiede esperienza e monitoraggio costante
            - ⚠️ Rischio di perdite superiori al 50% in brevi periodi
            - ⚠️ Effetto "decay" in mercati laterali
            - ⚠️ Ribilanciamento trimestrale obbligatorio
            
            **Consigliato SOLO per investitori esperti che comprendono completamente i rischi del leverage.**
            """)
        
        st.markdown("---")  # Separatore visivo
        
        # Informazioni generali
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Orizzonte Minimo", f"{portfolio['min_duration']} anni")
        
        with col2:
            st.metric("Ribilanciamento", portfolio['rebalance'])
        
        with col3:
            n_components = len(portfolio['components'])
            st.metric("N° ETF", n_components)
        
        # Note se presenti (oltre alla strategia)
        if portfolio['note'] and portfolio['note'] != portfolio.get('strategy_description', ''):
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
    
    st.info("📝 Il questionario richiede circa 3-4 minuti. Più sei preciso nelle risposte, migliore sarà il risultato!")
    
    st.divider()
    
    # Inizializza session state per il wizard
    if 'wizard_completed' not in st.session_state:
        st.session_state.wizard_completed = False
        st.session_state.wizard_results = None
    
    # Step 1: Età/Fase della Vita
    st.subheader("👤 Passo 1: Età e Fase della Vita")
    st.markdown("**In quale fascia d'età ti trovi?**")
    
    age_range = st.radio(
        "Seleziona la tua età:",
        [
            "Meno di 30 anni - Inizio carriera",
            "30-45 anni - Consolidamento professionale",
            "45-60 anni - Picco carriera, pre-pensione",
            "Più di 60 anni - Pensione o vicino alla pensione"
        ],
        index=None,
        help="L'età influenza sia l'orizzonte temporale che la tolleranza al rischio appropriata"
    )
    
    st.divider()
    
    # Step 2: Capitale Iniziale
    st.subheader("💰 Passo 2: Capitale da Investire")
    st.markdown("**Quanto pensi di investire inizialmente?**")
    
    initial_capital = st.radio(
        "Seleziona la fascia:",
        [
            "Meno di 5.000€",
            "5.000€ - 20.000€",
            "20.000€ - 50.000€",
            "Più di 50.000€"
        ],
        index=None,
        help="Il capitale influenza le scelte di diversificazione e i costi di transazione"
    )
    
    st.divider()
    
    # Step 3: Orizzonte Temporale
    st.subheader("⏰ Passo 3: Orizzonte Temporale")
    st.markdown("**Quando prevedi di aver bisogno di questi soldi?**")
    
    time_horizon = st.radio(
        "Seleziona l'orizzonte:",
        [
            "Meno di 3 anni - Breve termine",
            "3-7 anni - Medio termine",
            "7-10 anni - Medio-lungo termine",
            "10-15 anni - Lungo termine",
            "Più di 15 anni - Molto lungo termine"
        ],
        index=None,
        help="L'orizzonte temporale è fondamentale per determinare il livello di rischio appropriato"
    )
    
    st.divider()
    
    # Step 4: Obiettivo Investimento
    st.subheader("🎯 Passo 4: Obiettivo dell'Investimento")
    st.markdown("**Qual è il tuo obiettivo principale con questo investimento?**")
    
    investment_goal = st.radio(
        "Seleziona l'obiettivo:",
        [
            "Pensione - Costruire capitale per il futuro",
            "Grande acquisto - Casa, auto, educazione figli",
            "Crescita patrimonio - Aumentare il capitale nel tempo",
            "Preservazione capitale - Proteggere dall'inflazione",
            "Libertà finanziaria - Rendita passiva"
        ],
        index=None,
        help="L'obiettivo aiuta a determinare il profilo rischio/rendimento appropriato"
    )
    
    st.divider()
    
    # Step 5: Percentuale Patrimonio
    st.subheader("💼 Passo 5: Peso nel Tuo Patrimonio")
    st.markdown("**Questo investimento rappresenta che percentuale del tuo patrimonio totale?**")
    
    portfolio_percentage = st.radio(
        "Seleziona la proporzione:",
        [
            "Tutto o quasi tutto (80-100%)",
            "Parte maggiore (50-80%)",
            "Parte significativa (20-50%)",
            "Parte minore (meno del 20%)"
        ],
        index=None,
        help="Se rappresenta tutto il tuo patrimonio, servono scelte più prudenti"
    )
    
    st.divider()
    
    # Step 6: Esperienza
    st.subheader("📚 Passo 6: Esperienza con gli Investimenti")
    st.markdown("**Quanto sei familiare con gli investimenti in ETF?**")
    
    experience = st.radio(
        "Seleziona il tuo livello:",
        [
            "Principiante - È la mia prima volta con investimenti",
            "Base - Ho letto e studiato, ma poca pratica",
            "Intermedio - Ho già investito in ETF o fondi",
            "Esperto - Investo regolarmente e comprendo i mercati"
        ],
        index=None,
        help="Questo ci aiuta a suggerirti portafogli con la complessità appropriata"
    )
    
    st.divider()
    
    # Step 7: Tolleranza al Rischio Emotiva
    st.subheader("⚖️ Passo 7: Tolleranza al Rischio")
    st.markdown("**Come reagiresti se il tuo investimento perdesse il 30% in un anno?**")
    
    risk_tolerance = st.radio(
        "Seleziona la risposta più vicina al tuo comportamento:",
        [
            "😰 Venderei immediatamente - Non sopporto le perdite",
            "😟 Sarei molto preoccupato - Probabilmente venderei",
            "😐 Sarei preoccupato ma manterrei - Capisco la volatilità",
            "😊 Lo vedrei come opportunità - Comprerei di più se possibile",
            "🚀 Sono tranquillo - È normale, compro ancora"
        ],
        index=None,
        help="La tolleranza al rischio è soggettiva - sii onesto con te stesso"
    )
    
    st.divider()
    
    # Step 8: Reddito e Stabilità
    st.subheader("💵 Passo 8: Situazione Reddituale")
    st.markdown("**Come descriveresti il tuo reddito e la tua stabilità lavorativa?**")
    
    income_stability = st.radio(
        "Seleziona la tua situazione:",
        [
            "Reddito stabile e sicuro - Posso investire regolarmente",
            "Reddito variabile - Preferisco flessibilità",
            "Reddito incerto - Potrei aver bisogno dei soldi",
            "Pensionato/a - Vivo di rendite o pensione"
        ],
        index=None,
        help="La stabilità del reddito influenza quanto rischio puoi permetterti"
    )
    
    st.divider()
    
    # Step 9: Preferenza ESG
    st.subheader("🌱 Passo 9: Investimenti Sostenibili")
    st.markdown("**Ti interessa investire secondo criteri ESG (ambientali, sociali, governance)?**")
    
    esg_preference = st.radio(
        "Seleziona la tua preferenza:",
        [
            "Sì, voglio solo portafogli ESG - È una priorità",
            "Mi interessa ma non è essenziale - Bonus se disponibile",
            "No, non è importante - Focus solo su rendimento/rischio"
        ],
        index=None,
        help="I portafogli ESG investono in aziende con migliori pratiche ambientali e sociali"
    )
    
    st.divider()
    
    # Step 10: Complessità
    st.subheader("🔧 Passo 10: Tempo e Complessità")
    st.markdown("**Quanto tempo vuoi dedicare alla gestione del portafoglio?**")
    
    complexity = st.radio(
        "Seleziona la tua disponibilità:",
        [
            "Zero - Voglio investire e dimenticare (set & forget)",
            "Minima - Al massimo un controllo annuale",
            "Moderata - Posso ribilanciare ogni 3-6 mesi se necessario",
            "Alta - Mi piace monitorare e gestire attivamente"
        ],
        index=None,
        help="I portafogli single ETF non richiedono ribilanciamento"
    )
    
    st.divider()
    
    # Bottone per calcolare risultati
    if st.button("🎯 Trova i Miei Portafogli Ideali", type="primary", use_container_width=True):
        if all([age_range, initial_capital, time_horizon, investment_goal, portfolio_percentage, 
                experience, risk_tolerance, income_stability, esg_preference, complexity]):
            # Calcola i suggerimenti
            results = calculate_recommendations(
                portfolios,
                age_range,
                initial_capital,
                time_horizon,
                investment_goal,
                portfolio_percentage,
                experience,
                risk_tolerance,
                income_stability,
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


def calculate_recommendations(portfolios, age_range, initial_capital, time_horizon, investment_goal, 
                             portfolio_percentage, experience, risk_tolerance, income_stability, 
                             esg_preference, complexity):
    """Calcola i portafogli raccomandati in base alle risposte del wizard"""
    
    # STEP 1: Determina livello di rischio base
    
    # Mapping età → influenza rischio base
    age_risk_modifier = {
        "Meno di 30 anni - Inizio carriera": +1,
        "30-45 anni - Consolidamento professionale": 0,
        "45-60 anni - Picco carriera, pre-pensione": -1,
        "Più di 60 anni - Pensione o vicino alla pensione": -2
    }
    
    # Mapping orizzonte temporale → range di rischio base
    time_risk_mapping = {
        "Meno di 3 anni - Breve termine": [1, 2],
        "3-7 anni - Medio termine": [2, 3],
        "7-10 anni - Medio-lungo termine": [3, 4, 5],
        "10-15 anni - Lungo termine": [4, 5, 6],
        "Più di 15 anni - Molto lungo termine": [5, 6, 7]  # Escluso 8!
    }
    
    # Mapping obiettivo → preferenza rischio
    goal_risk_modifier = {
        "Pensione - Costruire capitale per il futuro": 0,
        "Grande acquisto - Casa, auto, educazione figli": -1,
        "Crescita patrimonio - Aumentare il capitale nel tempo": +1,
        "Preservazione capitale - Proteggere dall'inflazione": -2,
        "Libertà finanziaria - Rendita passiva": 0
    }
    
    # Mapping percentuale patrimonio → prudenza
    wealth_risk_modifier = {
        "Tutto o quasi tutto (80-100%)": -2,  # Molto prudente
        "Parte maggiore (50-80%)": -1,
        "Parte significativa (20-50%)": 0,
        "Parte minore (meno del 20%)": +1  # Può rischiare di più
    }
    
    # Mapping tolleranza emotiva → aggiustamento rischio
    tolerance_adjustment = {
        "😰 Venderei immediatamente - Non sopporto le perdite": -2,
        "😟 Sarei molto preoccupato - Probabilmente venderei": -1,
        "😐 Sarei preoccupato ma manterrei - Capisco la volatilità": 0,
        "😊 Lo vedrei come opportunità - Comprerei di più se possibile": +1,
        "🚀 Sono tranquillo - È normale, compro ancora": +1  # Max +1 per sicurezza
    }
    
    # Mapping stabilità reddito → prudenza
    income_risk_modifier = {
        "Reddito stabile e sicuro - Posso investire regolarmente": +1,
        "Reddito variabile - Preferisco flessibilità": 0,
        "Reddito incerto - Potrei aver bisogno dei soldi": -2,
        "Pensionato/a - Vivo di rendite o pensione": -1
    }
    
    # Calcola rischio base dall'orizzonte temporale
    base_risks = time_risk_mapping.get(time_horizon, [3, 4, 5])
    
    # Applica tutti i modificatori
    total_adjustment = (
        age_risk_modifier.get(age_range, 0) +
        goal_risk_modifier.get(investment_goal, 0) +
        wealth_risk_modifier.get(portfolio_percentage, 0) +
        tolerance_adjustment.get(risk_tolerance, 0) +
        income_risk_modifier.get(income_stability, 0)
    )
    
    # Applica aggiustamento al range
    recommended_risks = []
    for risk in base_risks:
        adjusted = risk + total_adjustment
        adjusted = max(1, min(7, adjusted))  # IMPORTANTE: Max 7, non 8!
        recommended_risks.append(adjusted)
    
    # Rimuovi duplicati e ordina
    recommended_risks = sorted(set(recommended_risks))
    
    # ============================================================================
    # ⚠️ CRITICAL FIX: HARD LIMITS BASATI SULLA TOLLERANZA AL RISCHIO
    # ============================================================================
    risk_tolerance_hard_caps = {
        "😰 Venderei immediatamente - Non sopporto le perdite": 2,
        "😟 Sarei molto preoccupato - Probabilmente venderei": 3,
        "😐 Sarei preoccupato ma manterrei - Capisco la volatilità": 5,
        "😊 Lo vedrei come opportunità - Comprerei di più se possibile": 7,
        "🚀 Sono tranquillo - È normale, compro ancora": 7
    }
    
    max_risk_allowed = risk_tolerance_hard_caps.get(risk_tolerance, 5)
    
    # APPLICA IL LIMITE INVALICABILE
    recommended_risks = [r for r in recommended_risks if r <= max_risk_allowed]
    
    # Se il filtro ha eliminato tutto, usa il massimo consentito e quello sotto
    if not recommended_risks:
        recommended_risks = [max(1, max_risk_allowed - 1), max_risk_allowed]
    
    # STEP 2: Determina preferenze di complessità
    
    # Capitale → influenza su single vs multi
    capital_preference = {
        "Meno di 5.000€": "single",
        "5.000€ - 20.000€": "flexible",
        "20.000€ - 50.000€": "flexible",
        "Più di 50.000€": "multi_ok"
    }
    
    capital_pref = capital_preference.get(initial_capital, "flexible")
    
    # Determina preferenza single/multi
    # FIX: Considera anche esperienza e complessità
    # Un utente esperto con capitale limitato può gestire 2-4 ETF
    single_only = (
        complexity == "Zero - Voglio investire e dimenticare (set & forget)" and
        capital_pref == "single"
    )
    
    # Se sei esperto o intermedio, anche con poco capitale, puoi gestire portafogli multi-ETF semplici
    if experience in ["Esperto - Investo regolarmente e comprendo i mercati", 
                      "Intermedio - Ho già investito in ETF o fondi"]:
        single_only = False
    
    prefer_single = (
        complexity in ["Zero - Voglio investire e dimenticare (set & forget)", 
                      "Minima - Al massimo un controllo annuale"] or
        (capital_pref == "single" and experience == "Principiante - È la mia prima volta con investimenti")
    )
    
    # STEP 3: Determina preferenza ESG
    
    esg_only = esg_preference == "Sì, voglio solo portafogli ESG - È una priorità"
    prefer_esg = esg_preference == "Mi interessa ma non è essenziale - Bonus se disponibile"
    
    # STEP 4: Determina complessità massima basata su esperienza
    
    max_components = {
        "Principiante - È la mia prima volta con investimenti": 1,
        "Base - Ho letto e studiato, ma poca pratica": 3,
        "Intermedio - Ho già investito in ETF o fondi": 6,
        "Esperto - Investo regolarmente e comprendo i mercati": 10
    }
    max_etfs = max_components.get(experience, 3)
    
    # STEP 5: Filtra e punteggia i portafogli
    
    # Raccogli tutti i portafogli
    all_portfolios = []
    for section in portfolios.values():
        all_portfolios.extend(section)
    
    # Filtra i portafogli
    candidates = []
    for portfolio in all_portfolios:
        # FILTRO CRITICO: Escludi sempre rischio 8
        if portfolio['risk_level'] == 8:
            continue
        
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
        
        # CALCOLA SCORE
        score = 0
        
        # Bonus per preferenza single
        if prefer_single and len(portfolio['components']) == 1:
            score += 12
        
        # Bonus per ESG
        if prefer_esg and portfolio['esg'] == 1:
            score += 6
        
        # Bonus forte per ESG only
        if esg_only and portfolio['esg'] == 1:
            score += 10
        
        # Bonus per nessun ribilanciamento
        if complexity in ["Zero - Voglio investire e dimenticare (set & forget)", 
                         "Minima - Al massimo un controllo annuale"]:
            if portfolio['rebalance'] == 'NO':
                score += 18
        
        # Bonus moderato per ribilanciamento annuale
        if complexity == "Moderata - Posso ribilanciare ogni 3-6 mesi se necessario":
            if portfolio['rebalance'] in ['NO', '1y']:
                score += 8
        
        # Bonus per portafogli semplici con poco capitale
        if capital_pref == "single" and len(portfolio['components']) == 1:
            score += 10
        
        # Penalità per portafogli troppo semplici con molto capitale
        if capital_pref == "multi_ok" and len(portfolio['components']) == 1:
            score -= 3
        
        # Bonus per match con obiettivo
        if investment_goal == "Preservazione capitale - Proteggere dall'inflazione":
            if portfolio['risk_level'] <= 3:
                score += 8
        
        if investment_goal == "Crescita patrimonio - Aumentare il capitale nel tempo":
            if portfolio['risk_level'] >= 5:
                score += 8
        
        # Vicinanza al rischio ideale
        ideal_risk = recommended_risks[len(recommended_risks)//2] if recommended_risks else 4
        risk_distance = abs(portfolio['risk_level'] - ideal_risk)
        score -= risk_distance * 3
        
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
            'age_range': age_range,
            'initial_capital': initial_capital,
            'time_horizon': time_horizon,
            'investment_goal': investment_goal,
            'portfolio_percentage': portfolio_percentage,
            'experience': experience,
            'risk_tolerance': risk_tolerance,
            'income_stability': income_stability,
            'esg_preference': esg_preference,
            'complexity': complexity,
            'single_only': single_only,
            'esg_only': esg_only,
            'max_etfs': max_etfs,
            'capital_pref': capital_pref
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
            **👤 Profilo Personale:**
            - Età: {criteria['age_range']}
            - Capitale: {criteria['initial_capital']}
            - Patrimonio: {criteria['portfolio_percentage']}
            
            **⏰ Profilo Temporale:**
            - Orizzonte: {criteria['time_horizon']}
            - Obiettivo: {criteria['investment_goal']}
            
            **⚖️ Profilo di Rischio:**
            - Tolleranza emotiva: {criteria['risk_tolerance']}
            - Stabilità reddito: {criteria['income_stability']}
            - **Livelli rischio suggeriti: {', '.join(map(str, results['recommended_risks']))}**
            """)
        
        with col2:
            st.markdown(f"""
            **📚 Esperienza e Preferenze:**
            - Livello: {criteria['experience']}
            - Max ETF per portafoglio: {criteria['max_etfs']}
            - Preferenza capitale: {criteria['capital_pref']}
            
            **🎯 Scelte Operative:**
            - ESG: {criteria['esg_preference']}
            - Tempo gestione: {criteria['complexity']}
            - Solo Single ETF: {'Sì' if criteria['single_only'] else 'No'}
            - Solo ESG: {'Sì' if criteria['esg_only'] else 'No'}
            """)
    
    st.divider()
    
    # Mostra portafogli raccomandati
    if results['portfolios']:
        st.subheader("🎯 I Tuoi Portafogli Consigliati")
        
        for idx, portfolio in enumerate(results['portfolios'], 1):
            # Emoji per il ranking
            if idx == 1:
                emoji = "🏆"
                medal = "Prima Scelta"
            elif idx == 2:
                emoji = "🥈"
                medal = "Alternativa Valida"
            else:
                emoji = "🥉"
                medal = "Opzione Aggiuntiva"
            
            st.markdown(f"### {emoji} {medal} - {portfolio['name']}")
            st.caption(f"ID Tecnico: {portfolio['id']}")
            
            # Spiega perché è stato raccomandato
            reasons = []
            
            if len(portfolio['components']) == 1:
                reasons.append("✅ **Semplicità massima** - Un solo ETF, gestione minima")
            
            if portfolio['esg'] == 1:
                reasons.append("🌱 **ESG compliant** - Investe secondo criteri sostenibili")
            
            if portfolio['rebalance'] == 'NO':
                reasons.append("⏰ **Zero manutenzione** - Non richiede ribilanciamento")
            elif portfolio['rebalance'] == '1y':
                reasons.append("📅 **Manutenzione annuale** - Ribilanciamento una volta l'anno")
            
            if portfolio['risk_level'] in results['recommended_risks']:
                risk_cat = get_risk_category(portfolio['risk_level'])
                reasons.append(f"⚖️ **Rischio appropriato** - Livello {portfolio['risk_level']} ({risk_cat}) adatto al tuo profilo")
            
            if len(portfolio['components']) <= 3:
                reasons.append("📊 **Facile da gestire** - Numero limitato di componenti")
            
            # Calcola TER medio
            if len(portfolio['components']) > 1:
                ter_medio = sum(
                    float(comp['ter']) * float(comp['percentage']) / 100
                    for comp in portfolio['components']
                )
                if ter_medio <= 0.15:
                    reasons.append(f"💰 **Costi bassi** - TER medio {ter_medio:.2f}%")
            else:
                ter_single = float(portfolio['components'][0]['ter'])
                if ter_single <= 0.15:
                    reasons.append(f"💰 **Costi bassi** - TER {ter_single}%")
            
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
        - Esplorare manualmente i portafogli disponibili usando "Esplora Liberamente"
        - Considerare portafogli con criteri leggermente diversi
        
        Ricorda: il rischio 8 (con leverage) è stato escluso per sicurezza.
        """)
    
    # Suggerimento finale personalizzato
    criteria = results['criteria']
    
    # Crea suggerimenti personalizzati
    tips = []
    
    if criteria['single_only']:
        tips.append("📌 **Single ETF:** Perfetto per iniziare. Quando avrai più esperienza potrai considerare portafogli multi-ETF.")
    
    if criteria['esg_only']:
        tips.append("🌱 **Focus ESG:** Ricorda di verificare i criteri ESG specifici di ogni ETF su JustETF.")
    
    if criteria['capital_pref'] == 'single':
        tips.append("💰 **Capitale Limitato:** Con il tuo capitale, un single ETF è la scelta più efficiente. Evita di frammentare troppo.")
    
    if criteria['experience'] == "Principiante - È la mia prima volta con investimenti":
        tips.append("📚 **Principiante:** Studia bene la sezione educativa dell'app e leggi i prospetti su JustETF prima di investire.")
    
    if "Pensione" in criteria['investment_goal']:
        tips.append("⏰ **Pensione:** Con un orizzonte lungo, puoi permetterti maggiore volatilità. Non farti influenzare dalle oscillazioni di breve termine.")
    
    if "Tutto o quasi tutto" in criteria['portfolio_percentage']:
        tips.append("⚠️ **Attenzione:** Questo rappresenta quasi tutto il tuo patrimonio. Assicurati di avere un fondo emergenza separato.")
    
    if tips:
        st.info("💡 **Suggerimenti Personalizzati:**\n\n" + "\n\n".join(tips))
    
    # Prossimi passi standard
    st.success("""
    ### 🚀 Prossimi Passi:
    
    1. **Studia** attentamente i portafogli raccomandati
    2. **Clicca** sui link JustETF per approfondire ogni ETF
    3. **Confronta** i costi (TER) e le caratteristiche
    4. **Verifica** l'allocazione geografica e settoriale
    5. **Leggi** i prospetti informativi completi
    6. **Consulta** un professionista prima di investire
    
    ⚠️ **Ricorda:** Questa è una guida educativa, non una raccomandazione personalizzata di investimento.
    """)


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
        'Alto': [],
        'Molto Alto': []  # NUOVA CATEGORIA PER RISCHIO 8
    }
    
    for portfolio in all_portfolios:
        category = get_risk_category(portfolio['risk_level'])
        risk_groups[category].append(portfolio)
    
    # Visualizza ogni gruppo
    for category in ['Basso', 'Medio', 'Alto', 'Molto Alto']:
        if risk_groups[category]:
            if category == 'Basso':
                icon = '🛡️'
                color = '#90EE90'
            elif category == 'Medio':
                icon = '⚖️'
                color = '#FFD700'
            elif category == 'Alto':
                icon = '🚀'
                color = '#FFA07A'
            else:  # Molto Alto
                icon = '⚡'
                color = '#8B0000'
            
            st.markdown(f"### {icon} Rischio {category}")
            st.markdown(f"<div style='background-color: {color}; padding: 0.5rem; border-radius: 0.5rem; margin-bottom: 1rem;'>Trovati {len(risk_groups[category])} portafogli</div>", unsafe_allow_html=True)
            
            # Warning speciale per categoria Molto Alto
            if category == 'Molto Alto':
                st.error("""
                ⚠️ **ATTENZIONE: PORTAFOGLI CON LEVERAGE**
                
                I portafogli in questa categoria utilizzano strumenti con leva finanziaria (2x) che amplificano 
                sia i guadagni che le perdite. Sono destinati SOLO ad investitori esperti che comprendono 
                completamente i rischi del leverage, compresi l'effetto decay e la necessità di ribilanciamento frequente.
                """)
            
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
        
        **🚀 Rischio Alto (6-7)**
        - Volatilità: 15-25% annua
        - Drawdown tipico: -30% / -50%
        - Ideale per: Orizzonti 15+ anni, alta tolleranza al rischio
        
        **⚡ Rischio Molto Alto (8) - LEVERAGE**
        - Volatilità: 30-50%+ annua
        - Drawdown tipico: -50% / -80%+
        - ⚠️ Utilizza leva finanziaria (2x)
        - ❌ NON adatto a principianti
        - ⚠️ Effetto "decay" in mercati laterali
        - ⚠️ Richiede ribilanciamento frequente (trimestrale)
        - Ideale per: SOLO investitori esperti con alta tolleranza al rischio e comprensione del leverage
        
        **⚠️ Il Vero Rischio è Vendere nel Momento Sbagliato**
        
        La maggior parte degli investitori perde denaro non a causa del mercato, ma perché 
        vende durante i ribassi trasformando perdite temporanee in perdite permanenti.
        
        **Nota sul Leverage (Rischio 8):**
        
        I portafogli con leverage amplificano i movimenti del mercato. Un ETF con leva 2x in teoria 
        dovrebbe raddoppiare i rendimenti giornalieri, ma a causa dell'effetto "compound decay", 
        le performance reali differiscono significativamente da quelle attese su periodi lunghi. 
        Questo rende il leverage inadatto per strategie buy-and-hold passive.
        """)
    
    with tab3:
        st.markdown("""
        ### 🎯 Come Scegliere il Portafoglio Giusto
        
        **1. Definisci il Tuo Orizzonte Temporale**
        - Meno di 3 anni → Rischio Basso
        - 3-10 anni → Rischio Basso/Medio
        - 10+ anni → Qualsiasi livello (eccetto 8 se non sei esperto)
        
        **2. Valuta la Tua Tolleranza Emotiva**
        
        Chiediti: "Se il mio portafoglio perdesse il 30% in un anno, riuscirei a non vendere?"
        - NO → Rischio Basso/Medio
        - SÌ, ma con difficoltà → Rischio Medio
        - SÌ, tranquillamente → Rischio Alto
        - SÌ, e comprerei di più → Forse Rischio Molto Alto (se esperto)
        
        **3. Considera la Complessità**
        - Principiante → Portafogli Single ETF (⭐)
        - Intermedio → Portafogli con 2-4 ETF (⭐⭐)
        - Avanzato → Portafogli multi-componente (⭐⭐⭐)
        - Esperto → Portafogli con leverage (⚡) - SOLO se comprendi i rischi
        
        **4. Ribilanciamento**
        - "NO" → Non richiede manutenzione
        - "1y" → Ribilanciamento annuale consigliato
        - "3M" → Ribilanciamento trimestrale (solo per esperti, tipicamente per leverage)
        
        **5. Attenzione al Leverage (Rischio 8)**
        
        I portafogli con leverage sono strumenti avanzati che richiedono:
        - Comprensione profonda dei mercati
        - Monitoraggio costante
        - Gestione attiva e ribilanciamento frequente
        - Tolleranza a perdite molto elevate
        - Esperienza con strumenti derivati
        
        Se non sei assolutamente certo di comprendere il leverage e l'effetto decay, 
        rimani sui livelli di rischio 1-7.
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
        
        **Leverage (Leva)**: Uso di debito o derivati per amplificare l'esposizione al mercato. 
        Un ETF con leva 2x mira a fornire il doppio del rendimento giornaliero dell'indice sottostante.
        
        **Decay (Decadimento)**: Effetto negativo sui rendimenti di lungo periodo degli ETF con leva 
        dovuto alla composizione giornaliera. In mercati laterali o volatili, il valore tende a diminuire 
        anche se l'indice sottostante rimane stabile.
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
    - I portafogli con leverage (Rischio 8) presentano rischi amplificati
    
    **Verifica sempre le informazioni più recenti sui siti ufficiali degli emittenti prima di investire.**
    """)
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p><strong>Portfolio ETF Explorer</strong> | Versione 4.0 (User-Friendly Edition) | Dicembre 2024</p>
        <p><small>Applicazione educativa - Non costituisce consulenza finanziaria</small></p>
        <p><small>✨ Nuova versione 4.0: Nomi descrittivi e spiegazioni strategiche per ogni portafoglio</small></p>
        <p><small>✅ PORT6a e PORT26 corretti a Rischio 6 (Alto) | Categoria separata "Molto Alto" per Rischio 8 (Leverage)</small></p>
    </div>
    """, unsafe_allow_html=True)


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
        - 🚀 Rischio Alto (6-7)
        - ⚡ Rischio Molto Alto (8 - Leverage)
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
        
        Rispondi a 10 domande approfondite per scoprire i portafogli più adatti a te.
        
        ⏱️ Richiede circa 3-4 minuti
        
        📊 Algoritmo avanzato che analizza:
        - Profilo personale e età
        - Capitale e patrimonio
        - Obiettivi e orizzonte
        - Esperienza e tolleranza
        - Preferenze ESG e gestione
        
        ⚠️ Il rischio 8 (leverage) è escluso automaticamente per sicurezza
        """)
        
        portfolio_wizard(portfolios)
    
    # Sezione educativa
    st.divider()
    display_educational_section()
    
    # Footer con disclaimer
    display_footer()


if __name__ == "__main__":
    main()
