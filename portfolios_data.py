"""
Database dei Portafogli ETF
Contiene tutti i portafogli modello organizzati per categoria
Versione 4.1 - Modifiche: PORT3, PORT5, PORT6a con oro invece di inflation-linked
"""

# ============================================================================
# PORTAFOGLI MULTI-ETF
# ============================================================================

MULTI_PORTFOLIOS = [
    {
        'id': 'PORT2a',
        'name': 'Conservatore Bilanciato',
        'risk_level': 2,
        'esg': 0,
        'min_duration': '5',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio prudente con minima esposizione azionaria (20%), forte presenza di obbligazioni breve termine e liquidità. Include oro per diversificazione. Ideale per chi cerca stabilità e protezione del capitale con un pizzico di crescita.',
        'components': [
            {'percentage': '10', 'name': 'SPDR MSCI World UCITS ETF', 'isin': 'IE00BFY0GT14', 'ter': '0.12'},
            {'percentage': '10', 'name': 'Xtrackers MSCI World Minimum Volatility UCITS ETF 1C', 'isin': 'IE00BL25JN58', 'ter': '0.25'},
            {'percentage': '10', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
            {'percentage': '20', 'name': 'Amundi Smart Overnight Return UCITS ETF Acc', 'isin': 'LU1190417599', 'ter': '0.10'},
            {'percentage': '30', 'name': 'iShares EUR Corporate Bond 0-3yr ESG SRI UCITS ETF EUR (Acc)', 'isin': 'IE000AK4O3W6', 'ter': '0.12'},
            {'percentage': '10', 'name': 'iShares Euro Inflation Linked Government Bond UCITS ETF', 'isin': 'IE00B0M62X26', 'ter': '0.09'},
            {'percentage': '10', 'name': 'iShares EUR Floating Rate Bond Advanced UCITS ETF EUR (Acc)', 'isin': 'IE000NVM56L3', 'ter': '0.10'},
        ],
        'note': ''
    },
    {
        'id': 'PORT2b',
        'name': 'Conservatore Quality',
        'risk_level': 2,
        'esg': 0,
        'min_duration': '7',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio conservativo con focus sulla qualità delle aziende (Quality factor) e bassa volatilità (Minimum Volatility). 30% azionario selezionato per stabilità, 70% obbligazionario/liquidità. Per chi vuole protezione ma con esposizione a società solide.',
        'components': [
            {'percentage': '15', 'name': 'Xtrackers MSCI World Minimum Volatility UCITS ETF 1C', 'isin': 'IE00BL25JN58', 'ter': '0.25'},
            {'percentage': '15', 'name': 'Xtrackers MSCI World Quality UCITS ETF 1C', 'isin': 'IE00BL25JL35', 'ter': '0.25'},
            {'percentage': '10', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
            {'percentage': '15', 'name': 'Amundi Smart Overnight Return UCITS ETF Acc', 'isin': 'LU1190417599', 'ter': '0.10'},
            {'percentage': '15', 'name': 'iShares EUR Corporate Bond 1-5yr UCITS ETF EUR (Acc)', 'isin': 'IE000F6G1DE0', 'ter': '0.20'},
            {'percentage': '15', 'name': 'iShares Euro Inflation Linked Government Bond UCITS ETF', 'isin': 'IE00B0M62X26', 'ter': '0.09'},
            {'percentage': '15', 'name': 'iShares EUR Floating Rate Bond Advanced UCITS ETF EUR (Acc)', 'isin': 'IE000NVM56L3', 'ter': '0.10'},
        ],
        'note': ''
    },
    {
        'id': 'PORT3',
        'name': 'Moderato Equilibrato',
        'risk_level': 3,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio bilanciato con 40% azionario (metà standard, metà Quality factor) e 60% obbligazionario diversificato. Include oro e obbligazioni inflation-linked. Equilibrio tra crescita e stabilità per orizzonti medio-lunghi.',
        'components': [
            {'percentage': '20', 'name': 'SPDR MSCI World UCITS ETF', 'isin': 'IE00BFY0GT14', 'ter': '0.12'},
            {'percentage': '20', 'name': 'Xtrackers MSCI World Quality UCITS ETF 1C', 'isin': 'IE00BL25JL35', 'ter': '0.25'},
            {'percentage': '10', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
            {'percentage': '10', 'name': 'iShares Euro Government Bond 3-5yr UCITS ETF', 'isin': 'IE00B1FZS681', 'ter': '0.15'},
            {'percentage': '15', 'name': 'iShares EUR Corporate Bond 1-5yr UCITS ETF EUR (Acc)', 'isin': 'IE000F6G1DE0', 'ter': '0.20'},
            {'percentage': '10', 'name': 'iShares Euro Inflation Linked Government Bond UCITS ETF', 'isin': 'IE00B0M62X26', 'ter': '0.09'},
            {'percentage': '15', 'name': 'iShares EUR Floating Rate Bond Advanced UCITS ETF EUR (Acc)', 'isin': 'IE000NVM56L3', 'ter': '0.10'},
        ],
        'note': ''
    },
    {
        'id': 'PORT5',
        'name': 'Dinamico 60/40',
        'risk_level': 5,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio dinamico con 60% azionario globale (All-World), 30% obbligazionario e 10% oro fisico. L\'oro sostituisce le obbligazioni inflation-linked per protezione dall\'inflazione. Buon compromesso tra potenziale di crescita e controllo del rischio. Adatto per orizzonti lunghi con tolleranza media alla volatilità.',
        'components': [
            {'percentage': '60', 'name': 'Vanguard FTSE All-World UCITS ETF (USD) Accumulating', 'isin': 'IE00BK5BQT80', 'ter': '0.19'},
            {'percentage': '10', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
            {'percentage': '10', 'name': 'iShares EUR Floating Rate Bond Advanced UCITS ETF EUR (Acc)', 'isin': 'IE000NVM56L3', 'ter': '0.10'},
            {'percentage': '20', 'name': 'iShares Euro Government Bond 3-5yr UCITS ETF', 'isin': 'IE00B1FZS681', 'ter': '0.15'},
        ],
        'note': ''
    },
    {
        'id': 'PORT6a',
        'name': 'Aggressivo Globale con Oro',
        'risk_level': 6,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio ad alta esposizione azionaria (80%) con diversificazione globale MSCI World, protezione valutaria parziale (10% EUR hedged) e oro (10%). Minima componente obbligazionaria (10%). Per chi cerca crescita con un pizzico di protezione.',
        'components': [
            {'percentage': '70', 'name': 'SPDR MSCI World UCITS ETF', 'isin': 'IE00BFY0GT14', 'ter': '0.12'},
            {'percentage': '10', 'name': 'Xtrackers MSCI World UCITS ETF 2C - EUR Hedged', 'isin': 'IE000ONQ3X90', 'ter': '0.17'},
            {'percentage': '10', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
            {'percentage': '10', 'name': 'iShares EUR Corporate Bond 1-5yr UCITS ETF EUR (Acc)', 'isin': 'IE000F6G1DE0', 'ter': '0.20'},
        ],
        'note': ''
    },
    {
        'id': 'PORT6b',
        'name': 'Aggressivo Emerging + Oro',
        'risk_level': 6,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio molto aggressivo con 85% azionario (80% globale + 5% mercati emergenti extra) e 15% oro. Nessuna componente obbligazionaria. Massima crescita con oro come unica protezione. Solo per orizzonti molto lunghi.',
        'components': [
            {'percentage': '80', 'name': 'Amundi Prime All Country World UCITS', 'isin': 'IE0003XJA0J9', 'ter': '0.07'},
            {'percentage': '5', 'name': 'iShares Core MSCI Emerging Markets IMI UCITS ETF (Acc)', 'isin': 'IE00BKM4GZ66', 'ter': '0.18'},
            {'percentage': '15', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
        ],
        'note': ''
    },
    {
        'id': 'PORT7a',
        'name': 'Factor Investing: Momentum + Value',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio 100% azionario basato su Factor Investing: 60% core market + 20% Momentum + 20% Value. Punta a sovraperformare il mercato nel lungo periodo attraverso fattori scientificamente provati. Per investitori esperti che credono nei fattori.',
        'components': [
            {'percentage': '60', 'name': 'SPDR MSCI World UCITS ETF', 'isin': 'IE00BFY0GT14', 'ter': '0.12'},
            {'percentage': '20', 'name': 'iShares Edge MSCI World Momentum Factor UCITS ETF (Acc)', 'isin': 'IE00BP3QZ825', 'ter': '0.25'},
            {'percentage': '20', 'name': 'iShares Edge MSCI World Value Factor UCITS ETF', 'isin': 'IE00BP3QZB59', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT7b',
        'name': 'Globale Ottimizzato USA + Mondo',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio 100% azionario con allocazione ottimizzata: 40% USA (S&P 500), 45% resto del mondo sviluppato, 15% mercati emergenti. Maggiore controllo sulla distribuzione geografica rispetto a un All-World standard. Per chi vuole personalizzare l\'esposizione.',
        'components': [
            {'percentage': '40', 'name': 'Vanguard S&P 500 UCITS ETF (USD) Accumulating', 'isin': 'IE00BFMXXD54', 'ter': '0.07'},
            {'percentage': '45', 'name': 'Xtrackers MSCI World ex USA UCITS ETF 1C', 'isin': 'IE0006WW1TQ4', 'ter': '0.15'},
            {'percentage': '15', 'name': 'iShares Core MSCI Emerging Markets IMI UCITS ETF (Acc)', 'isin': 'IE00BKM4GZ66', 'ter': '0.18'},
        ],
        'note': ''
    },
    {
        'id': 'PORT8',
        'name': 'Turbo Leverage 2x (Solo Esperti)',
        'risk_level': 8,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '3M',
        'strategy_description': '⚠️ Portafoglio ESTREMO con leverage 2x: 50% azionario standard + 50% azionario con leva 2x. Amplifica sia guadagni che perdite. Soggetto a "decay" in mercati laterali. Ribilanciamento trimestrale obbligatorio. SOLO per trader esperti che comprendono appieno i rischi del leverage.',
        'components': [
            {'percentage': '50', 'name': 'SPDR MSCI World UCITS ETF', 'isin': 'IE00BFY0GT14', 'ter': '0.12'},
            {'percentage': '50', 'name': 'Amundi MSCI World (2x) Leveraged UCITS ETF Acc', 'isin': 'FR0014010HV4', 'ter': '0.60'},
        ],
        'note': '⚠️ Portafoglio con LEVERAGE (2x) - Solo per investitori esperti che comprendono i rischi amplificati'
    },
]

# ============================================================================
# PORTAFOGLI SINGLE ETF
# ============================================================================

SINGLE_PORTFOLIOS = [
    {
        'id': 'PORT11a',
        'name': 'Liquidità Sicura',
        'risk_level': 1,
        'esg': 0,
        'min_duration': '1..xx',
        'rebalance': 'NO',
        'strategy_description': 'Portafoglio ultra-sicuro con rendimenti legati ai tassi overnight. Perfetto per fondi emergenza o capitale da investire a breve. Zero rischio di mercato, rendimenti in linea con i tassi BCE. Liquidabile in qualsiasi momento.',
        'components': [
            {'percentage': '100', 'name': 'Amundi Smart Overnight Return UCITS ETF Acc', 'isin': 'LU1190417599', 'ter': '0.10'},
        ],
        'note': ''
    },
    {
        'id': 'PORT11b',
        'name': 'Bond Ladder con Scadenza',
        'risk_level': 1,
        'esg': 1,
        'min_duration': '1...9',
        'rebalance': 'NO',
        'strategy_description': 'Strategia "bond ladder" con ETF corporate a scadenza. Scegli l\'ETF con scadenza allineata al tuo obiettivo. A scadenza ricevi il capitale (salvo default). Ideale per obiettivi con data precisa (es. acquisto casa tra 5 anni). Minimo rischio di tasso.',
        'components': [
            {'percentage': '100', 'name': 'iShares iBonds Dec 2034 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000UY6XF65', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2033 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000ZBGZQM8', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2032 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000I660ZF8', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2031 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000D9WMGF0', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2030 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000Y2BJVK9', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2029 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000SNLFDR7', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2028 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE0008UEVOE0', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2027 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000ZOI8OK5', 'ter': '0.12'},
            {'percentage': '100', 'name': 'iShares iBonds Dec 2026 Term EUR Corporate UCITS ETF EUR (Acc)', 'isin': 'IE000WA6L436', 'ter': '0.12'},
        ],
        'note': '(Scegli UNO solo di questi ETF in base alla scadenza desiderata)'
    },
    {
        'id': 'PORT13',
        'name': 'Vanguard LifeStrategy 40% Equity',
        'risk_level': 3,
        'esg': 0,
        'min_duration': '7',
        'rebalance': 'NO',
        'strategy_description': 'Soluzione all-in-one di Vanguard: 40% azionario globale + 60% obbligazionario globale. Ribilanciamento automatico incluso. Semplicità massima, costi bassi. Ideale per chi vuole un portafoglio moderato senza pensieri. Set & forget.',
        'components': [
            {'percentage': '100', 'name': 'Vanguard LifeStrategy 40% Equity UCITS ETF Accumulating', 'isin': 'IE00BMVB5M21', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT15',
        'name': 'Vanguard LifeStrategy 60% Equity',
        'risk_level': 5,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
        'strategy_description': 'Soluzione all-in-one di Vanguard: 60% azionario globale + 40% obbligazionario globale. Allocazione bilanciata con leggera prevalenza azionaria. Ribilanciamento automatico. Perfetto per investitori con orizzonte 10+ anni. Set & forget.',
        'components': [
            {'percentage': '100', 'name': 'Vanguard LifeStrategy 60% Equity UCITS ETF Accumulating', 'isin': 'IE00BMVB5P51', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT16',
        'name': 'Vanguard LifeStrategy 80% Equity',
        'risk_level': 6,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
        'strategy_description': 'Soluzione all-in-one di Vanguard: 80% azionario globale + 20% obbligazionario globale. Approccio aggressivo con minima stabilizzazione obbligazionaria. Ribilanciamento automatico. Per chi vuole massima crescita ma un minimo di protezione. Set & forget.',
        'components': [
            {'percentage': '100', 'name': 'Vanguard LifeStrategy 80% Equity UCITS ETF Accumulating', 'isin': 'IE00BMVB5R75', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT17a',
        'name': 'All Country World - Ultra Low Cost',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
        'strategy_description': 'Portafoglio 100% azionario globale (paesi sviluppati + emergenti) con il TER più basso sul mercato (0.07%). Massima diversificazione, costi minimi. La scelta del purista che crede nel mercato globale nel lungo termine. Set & forget definitivo.',
        'components': [
            {'percentage': '100', 'name': 'Amundi Prime All Country World UCITS', 'isin': 'IE0003XJA0J9', 'ter': '0.07'},
        ],
        'note': ''
    },
    {
        'id': 'PORT17b',
        'name': 'MSCI World Classico',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
        'strategy_description': 'Portafoglio 100% azionario sui mercati sviluppati (MSCI World). Esclude mercati emergenti. Approccio tradizionale, storico e testato. Ideale per chi preferisce focus sui paesi sviluppati evitando l\'extra volatilità degli emergenti. Set & forget.',
        'components': [
            {'percentage': '100', 'name': 'SPDR MSCI World UCITS ETF', 'isin': 'IE00BFY0GT14', 'ter': '0.12'},
        ],
        'note': ''
    },
]

# ============================================================================
# PORTAFOGLI ESG
# ============================================================================

ESG_PORTFOLIOS = [
    {
        'id': 'PORT21a',
        'name': 'ESG Floating Rate Sicuro',
        'risk_level': 1,
        'esg': 1,
        'min_duration': '1..xx',
        'rebalance': 'NO',
        'strategy_description': 'Obbligazioni corporate ESG a tasso variabile. Protezione dall\'inflazione e rialzo tassi. Rischio contenuto, solo società con buone pratiche ESG. Ideale per liquidità di medio termine con valori sostenibili. Nessuna esposizione azionaria.',
        'components': [
            {'percentage': '100', 'name': 'Amundi Floating Rate Euro Corporate ESG UCITS ETF EUR (C)', 'isin': 'LU1829219390', 'ter': '0.18'},
        ],
        'note': ''
    },
    {
        'id': 'PORT22a',
        'name': 'ESG Conservatore',
        'risk_level': 2,
        'esg': 1,
        'min_duration': '7',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio conservativo ESG: 30% azionario sostenibile + 70% obbligazionario ESG (mix corporate breve termine e floating rate). Tutti i componenti rispettano criteri ambientali e sociali. Per investitori prudenti con valori sostenibili.',
        'components': [
            {'percentage': '30', 'name': 'iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc)', 'isin': 'IE00B8KGV557', 'ter': '0.20'},
            {'percentage': '10', 'name': 'PIMCO Euro Short Maturity UCITS ETF Acc', 'isin': 'IE00BVZ6SP04', 'ter': '0.19'},
            {'percentage': '30', 'name': 'Amundi Index Euro Corporate SRI 0-3 Y UCITS ETF DR (C)', 'isin': 'LU1437017350', 'ter': '0.12'},
            {'percentage': '40', 'name': 'Amundi Floating Rate Euro Corporate ESG UCITS ETF EUR (C)', 'isin': 'LU1829219390', 'ter': '0.18'},
        ],
        'note': ''
    },
    {
        'id': 'PORT23a',
        'name': 'ESG Moderato',
        'risk_level': 3,
        'esg': 1,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio moderato ESG: 40% azionario sostenibile + 60% obbligazionario ESG (mix corporate breve termine, floating rate e governativi 3-5 anni). Equilibrio tra crescita sostenibile e stabilità. Per investitori bilanciati con focus ESG.',
        'components': [
            {'percentage': '40', 'name': 'iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc)', 'isin': 'IE00B8KGV557', 'ter': '0.20'},
            {'percentage': '20', 'name': 'Amundi Index Euro Corporate SRI 0-3 Y UCITS ETF DR (C)', 'isin': 'LU1437017350', 'ter': '0.12'},
            {'percentage': '20', 'name': 'Amundi Floating Rate Euro Corporate ESG UCITS ETF EUR (C)', 'isin': 'LU1829219390', 'ter': '0.18'},
            {'percentage': '20', 'name': 'BNP Paribas Easy JPM ESG EMU Government Bond IG 3-5Y UCITS ETF', 'isin': 'LU2244387457', 'ter': '0.15'},
        ],
        'note': ''
    },
    {
        'id': 'PORT25a',
        'name': 'ESG Dinamico',
        'risk_level': 5,
        'esg': 1,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio dinamico ESG: 60% azionario sostenibile + 40% obbligazionario ESG diversificato. Buon potenziale di crescita mantenendo criteri ambientali e sociali rigorosi. Per chi vuole performance con impatto positivo.',
        'components': [
            {'percentage': '60', 'name': 'iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc)', 'isin': 'IE00B8KGV557', 'ter': '0.20'},
            {'percentage': '10', 'name': 'Amundi Index Euro Corporate SRI 0-3 Y UCITS ETF DR (C)', 'isin': 'LU1437017350', 'ter': '0.12'},
            {'percentage': '10', 'name': 'Amundi Floating Rate Euro Corporate ESG UCITS ETF EUR (C)', 'isin': 'LU1829219390', 'ter': '0.18'},
            {'percentage': '20', 'name': 'BNP Paribas Easy JPM ESG EMU Government Bond IG 3-5Y UCITS ETF', 'isin': 'LU2244387457', 'ter': '0.15'},
        ],
        'note': ''
    },
    {
        'id': 'PORT26',
        'name': 'ESG Aggressivo',
        'risk_level': 6,
        'esg': 1,
        'min_duration': '10',
        'rebalance': '1y',
        'strategy_description': 'Portafoglio aggressivo ESG: 80% azionario sostenibile + 20% obbligazionario ESG breve termine. Massima esposizione alla crescita delle aziende sostenibili con minima protezione obbligazionaria. Per investitori convinti dell\'ESG con orizzonte lungo.',
        'components': [
            {'percentage': '80', 'name': 'iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc)', 'isin': 'IE00B8KGV557', 'ter': '0.20'},
            {'percentage': '10', 'name': 'Amundi Index Euro Corporate SRI 0-3 Y UCITS ETF DR (C)', 'isin': 'LU1437017350', 'ter': '0.12'},
            {'percentage': '10', 'name': 'Amundi Floating Rate Euro Corporate ESG UCITS ETF EUR (C)', 'isin': 'LU1829219390', 'ter': '0.18'},
        ],
        'note': ''
    },
    {
        'id': 'PORT27',
        'name': 'ESG World 100% - Enhanced CTB',
        'risk_level': 7,
        'esg': 1,
        'min_duration': '10',
        'rebalance': 'NO',
        'strategy_description': 'Portafoglio 100% azionario ESG con approccio Enhanced + Climate Transition Benchmark. Esclude combustibili fossili e punta su aziende allineate agli obiettivi climatici. Per puristi ESG che vogliono massimo impatto e crescita. Set & forget sostenibile.',
        'components': [
            {'percentage': '100', 'name': 'iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc)', 'isin': 'IE00B8KGV557', 'ter': '0.20'},
        ],
        'note': ''
    },
    {
        'id': 'PORT27b',
        'name': 'ESG Global All Cap - Vanguard',
        'risk_level': 7,
        'esg': 1,
        'min_duration': '10',
        'rebalance': 'NO',
        'strategy_description': 'Portafoglio 100% azionario ESG globale con approccio Vanguard. Include tutte le capitalizzazioni (large, mid, small cap) con screening ESG. Massima diversificazione sostenibile. Per chi vuole il massimo della crescita ESG con qualità Vanguard. Set & forget.',
        'components': [
            {'percentage': '100', 'name': 'Vanguard ESG Global All Cap UCITS ETF (USD) Accumulating', 'isin': 'IE00BNG8L278', 'ter': '0.24'},
        ],
        'note': ''
    },
]

# ============================================================================
# FUNZIONI HELPER
# ============================================================================

def get_all_portfolios():
    """Restituisce tutti i portafogli organizzati per categoria"""
    return {
        'multi': MULTI_PORTFOLIOS,
        'single': SINGLE_PORTFOLIOS,
        'esg': ESG_PORTFOLIOS
    }

def get_portfolio_by_id(portfolio_id):
    """Cerca un portafoglio specifico per ID"""
    all_portfolios = MULTI_PORTFOLIOS + SINGLE_PORTFOLIOS + ESG_PORTFOLIOS
    for portfolio in all_portfolios:
        if portfolio['id'] == portfolio_id:
            return portfolio
    return None

def get_portfolios_by_risk(risk_level):
    """Filtra i portafogli per livello di rischio"""
    all_portfolios = MULTI_PORTFOLIOS + SINGLE_PORTFOLIOS + ESG_PORTFOLIOS
    return [p for p in all_portfolios if p['risk_level'] == risk_level]

def get_portfolios_by_esg(esg_only=True):
    """Filtra i portafogli per criterio ESG"""
    all_portfolios = MULTI_PORTFOLIOS + SINGLE_PORTFOLIOS + ESG_PORTFOLIOS
    if esg_only:
        return [p for p in all_portfolios if p['esg'] == 1]
    else:
        return [p for p in all_portfolios if p['esg'] == 0]

def get_statistics():
    """Restituisce statistiche sui portafogli disponibili"""
    all_portfolios = MULTI_PORTFOLIOS + SINGLE_PORTFOLIOS + ESG_PORTFOLIOS
    return {
        'total_portfolios': len(all_portfolios),
        'multi_portfolios': len(MULTI_PORTFOLIOS),
        'single_portfolios': len(SINGLE_PORTFOLIOS),
        'esg_portfolios': len(ESG_PORTFOLIOS),
        'risk_levels': sorted(set(p['risk_level'] for p in all_portfolios)),
        'unique_etfs': len(set(
            comp['isin'] 
            for p in all_portfolios 
            for comp in p['components']
        ))
    }
