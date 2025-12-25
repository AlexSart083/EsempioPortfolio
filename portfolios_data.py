"""
Database dei Portafogli ETF
Contiene tutti i portafogli modello organizzati per categoria
"""

# ============================================================================
# PORTAFOGLI MULTI-ETF
# ============================================================================

MULTI_PORTFOLIOS = [
    {
        'id': 'PORT2a',
        'risk_level': 2,
        'esg': 0,
        'min_duration': '5',
        'rebalance': '1y',
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
        'risk_level': 2,
        'esg': 0,
        'min_duration': '7',
        'rebalance': '1y',
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
        'risk_level': 3,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
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
        'risk_level': 5,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'components': [
            {'percentage': '60', 'name': 'Vanguard FTSE All-World UCITS ETF (USD) Accumulating', 'isin': 'IE00BK5BQT80', 'ter': '0.19'},
            {'percentage': '10', 'name': 'iShares Euro Inflation Linked Government Bond UCITS ETF', 'isin': 'IE00B0M62X26', 'ter': '0.09'},
            {'percentage': '10', 'name': 'iShares EUR Floating Rate Bond Advanced UCITS ETF EUR (Acc)', 'isin': 'IE000NVM56L3', 'ter': '0.10'},
            {'percentage': '20', 'name': 'iShares Euro Government Bond 3-5yr UCITS ETF', 'isin': 'IE00B1FZS681', 'ter': '0.15'},
        ],
        'note': ''
    },
    {
        'id': 'PORT6a',
        'risk_level': 6,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'components': [
            {'percentage': '70', 'name': 'Amundi Prime All Country World UCITS', 'isin': 'IE0003XJA0J9', 'ter': '0.07'},
            {'percentage': '10', 'name': 'Xtrackers MSCI World UCITS ETF 2C - EUR Hedged', 'isin': 'IE000ONQ3X90', 'ter': '0.17'},
            {'percentage': '10', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
            {'percentage': '10', 'name': 'iShares EUR Corporate Bond 1-5yr UCITS ETF EUR (Acc)', 'isin': 'IE000F6G1DE0', 'ter': '0.20'},
        ],
        'note': ''
    },
    {
        'id': 'PORT6b',
        'risk_level': 6,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'components': [
            {'percentage': '80', 'name': 'Amundi Prime All Country World UCITS', 'isin': 'IE0003XJA0J9', 'ter': '0.07'},
            {'percentage': '5', 'name': 'iShares Core MSCI Emerging Markets IMI UCITS ETF (Acc)', 'isin': 'IE00BKM4GZ66', 'ter': '0.18'},
            {'percentage': '15', 'name': 'WisdomTree Core Physical Gold', 'isin': 'JE00BN2CJ301', 'ter': '0.12'},
        ],
        'note': ''
    },
    {
        'id': 'PORT7a',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'components': [
            {'percentage': '60', 'name': 'SPDR MSCI World UCITS ETF', 'isin': 'IE00BFY0GT14', 'ter': '0.12'},
            {'percentage': '20', 'name': 'iShares Edge MSCI World Momentum Factor UCITS ETF (Acc)', 'isin': 'IE00BP3QZ825', 'ter': '0.25'},
            {'percentage': '20', 'name': 'iShares Edge MSCI World Value Factor UCITS ETF', 'isin': 'IE00BP3QZB59', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT7b',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '1y',
        'components': [
            {'percentage': '40', 'name': 'Vanguard S&P 500 UCITS ETF (USD) Accumulating', 'isin': 'IE00BFMXXD54', 'ter': '0.07'},
            {'percentage': '45', 'name': 'Xtrackers MSCI World ex USA UCITS ETF 1C', 'isin': 'IE0006WW1TQ4', 'ter': '0.15'},
            {'percentage': '15', 'name': 'iShares Core MSCI Emerging Markets IMI UCITS ETF (Acc)', 'isin': 'IE00BKM4GZ66', 'ter': '0.18'},
        ],
        'note': ''
    },
    {
        'id': 'PORT8',
        'risk_level': 8,
        'esg': 0,
        'min_duration': '10',
        'rebalance': '3M',
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
        'risk_level': 1,
        'esg': 0,
        'min_duration': '1..xx',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'Amundi Smart Overnight Return UCITS ETF Acc', 'isin': 'LU1190417599', 'ter': '0.10'},
        ],
        'note': ''
    },
    {
        'id': 'PORT11b',
        'risk_level': 1,
        'esg': 1,
        'min_duration': '1...9',
        'rebalance': 'NO',
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
        'note': '(Only one of the following ETF depend on user needs)'
    },
    {
        'id': 'PORT13',
        'risk_level': 3,
        'esg': 0,
        'min_duration': '7',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'Vanguard LifeStrategy 40% Equity UCITS ETF Accumulating', 'isin': 'IE00BMVB5M21', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT15',
        'risk_level': 5,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'Vanguard LifeStrategy 60% Equity UCITS ETF Accumulating', 'isin': 'IE00BMVB5P51', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT16',
        'risk_level': 6,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'Vanguard LifeStrategy 80% Equity UCITS ETF Accumulating', 'isin': 'IE00BMVB5R75', 'ter': '0.25'},
        ],
        'note': ''
    },
    {
        'id': 'PORT17a',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'Amundi Prime All Country World UCITS', 'isin': 'IE0003XJA0J9', 'ter': '0.07'},
        ],
        'note': ''
    },
    {
        'id': 'PORT17b',
        'risk_level': 7,
        'esg': 0,
        'min_duration': '10',
        'rebalance': 'NO',
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
        'risk_level': 1,
        'esg': 1,
        'min_duration': '1..xx',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'Amundi Floating Rate Euro Corporate ESG UCITS ETF EUR (C)', 'isin': 'LU1829219390', 'ter': '0.18'},
        ],
        'note': ''
    },
    {
        'id': 'PORT22a',
        'risk_level': 2,
        'esg': 1,
        'min_duration': '7',
        'rebalance': '1y',
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
        'risk_level': 3,
        'esg': 1,
        'min_duration': '10',
        'rebalance': '1y',
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
        'risk_level': 5,
        'esg': 1,
        'min_duration': '10',
        'rebalance': '1y',
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
        'risk_level': 6,
        'esg': 1,
        'min_duration': '10',
        'rebalance': '1y',
        'components': [
            {'percentage': '80', 'name': 'iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc)', 'isin': 'IE00B8KGV557', 'ter': '0.20'},
            {'percentage': '10', 'name': 'Amundi Index Euro Corporate SRI 0-3 Y UCITS ETF DR (C)', 'isin': 'LU1437017350', 'ter': '0.12'},
            {'percentage': '10', 'name': 'Amundi Floating Rate Euro Corporate ESG UCITS ETF EUR (C)', 'isin': 'LU1829219390', 'ter': '0.18'},
        ],
        'note': ''
    },
    {
        'id': 'PORT27',
        'risk_level': 7,
        'esg': 1,
        'min_duration': '10',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'iShares MSCI World ESG Enhanced CTB UCITS ETF USD (Acc)', 'isin': 'IE00B8KGV557', 'ter': '0.20'},
        ],
        'note': ''
    },
    {
        'id': 'PORT27b',
        'risk_level': 7,
        'esg': 1,
        'min_duration': '10',
        'rebalance': 'NO',
        'components': [
            {'percentage': '100', 'name': 'Vanguard ESG Global All Cap UCITS ETF (USD) Accumulating', 'isin': 'IE00BNG8L278', 'ter': '0.24'},
        ],
        'note': ''
    },
]

# ============================================================================
# FUNZIONE PER OTTENERE TUTTI I PORTAFOGLI
# ============================================================================

def get_all_portfolios():
    """
    Restituisce tutti i portafogli organizzati per categoria
    
    Returns:
        dict: Dizionario con chiavi 'multi', 'single', 'esg'
    """
    return {
        'multi': MULTI_PORTFOLIOS,
        'single': SINGLE_PORTFOLIOS,
        'esg': ESG_PORTFOLIOS
    }


def get_portfolio_by_id(portfolio_id):
    """
    Cerca un portafoglio specifico per ID
    
    Args:
        portfolio_id (str): ID del portafoglio (es. 'PORT5')
        
    Returns:
        dict or None: Il portafoglio se trovato, altrimenti None
    """
    all_portfolios = MULTI_PORTFOLIOS + SINGLE_PORTFOLIOS + ESG_PORTFOLIOS
    
    for portfolio in all_portfolios:
        if portfolio['id'] == portfolio_id:
            return portfolio
    
    return None


def get_portfolios_by_risk(risk_level):
    """
    Filtra i portafogli per livello di rischio
    
    Args:
        risk_level (int): Livello di rischio da 1 a 8
        
    Returns:
        list: Lista di portafogli con il livello di rischio specificato
    """
    all_portfolios = MULTI_PORTFOLIOS + SINGLE_PORTFOLIOS + ESG_PORTFOLIOS
    
    return [p for p in all_portfolios if p['risk_level'] == risk_level]


def get_portfolios_by_esg(esg_only=True):
    """
    Filtra i portafogli per criterio ESG
    
    Args:
        esg_only (bool): Se True, restituisce solo portafogli ESG
        
    Returns:
        list: Lista di portafogli filtrati
    """
    all_portfolios = MULTI_PORTFOLIOS + SINGLE_PORTFOLIOS + ESG_PORTFOLIOS
    
    if esg_only:
        return [p for p in all_portfolios if p['esg'] == 1]
    else:
        return [p for p in all_portfolios if p['esg'] == 0]


# ============================================================================
# STATISTICHE
# ============================================================================

def get_statistics():
    """
    Restituisce statistiche sui portafogli disponibili
    
    Returns:
        dict: Dizionario con varie statistiche
    """
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


if __name__ == "__main__":
    # Test del modulo
    stats = get_statistics()
    print("📊 Statistiche Database Portafogli:")
    print(f"  - Portafogli totali: {stats['total_portfolios']}")
    print(f"  - Multi-ETF: {stats['multi_portfolios']}")
    print(f"  - Single ETF: {stats['single_portfolios']}")
    print(f"  - ESG: {stats['esg_portfolios']}")
    print(f"  - Livelli di rischio: {stats['risk_levels']}")
    print(f"  - ETF unici: {stats['unique_etfs']}")
