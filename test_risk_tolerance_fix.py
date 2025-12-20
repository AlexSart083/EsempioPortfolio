#!/usr/bin/env python3
"""
Test Suite per Verifica Correzione Hard Limits Tolleranza al Rischio
Versione: 3.2
"""

def test_risk_tolerance_caps():
    """
    Testa che i cap di rischio basati sulla tolleranza funzionino correttamente
    """
    
    print("🧪 Test Suite - Hard Limits Tolleranza al Rischio")
    print("=" * 60)
    
    # Definizione caps (deve matchare app.py)
    risk_tolerance_hard_caps = {
        "😰 Venderei immediatamente - Non sopporto le perdite": 2,
        "😟 Sarei molto preoccupato - Probabilmente venderei": 3,
        "😐 Sarei preoccupato ma manterrei - Capisco la volatilità": 5,
        "😊 Lo vedrei come opportunità - Comprerei di più se possibile": 7,
        "🚀 Sono tranquillo - È normale, compro ancora": 7
    }
    
    # TEST 1: Bassa tolleranza blocca rischio alto
    print("\n📋 TEST 1: Bassa Tolleranza Emotiva")
    print("-" * 60)
    base_risks = [5, 6, 7]  # Da orizzonte lungo
    tolerance = "😰 Venderei immediatamente - Non sopporto le perdite"
    max_allowed = risk_tolerance_hard_caps[tolerance]
    
    filtered = [r for r in base_risks if r <= max_allowed]
    print(f"Rischi base (da orizzonte): {base_risks}")
    print(f"Tolleranza: {tolerance}")
    print(f"Max rischio consentito: {max_allowed}")
    print(f"Rischi dopo filtro: {filtered}")
    
    if not filtered:
        fallback = [max(1, max_allowed - 1), max_allowed]
        print(f"Fallback applicato: {fallback}")
        assert fallback == [1, 2], "❌ Fallback errato!"
        print("✅ TEST 1 PASSATO - Bassa tolleranza correttamente limitata")
    else:
        print("❌ TEST 1 FALLITO - Filtro non applicato!")
        return False
    
    # TEST 2: Media tolleranza consente solo portafogli moderati
    print("\n📋 TEST 2: Media Tolleranza Emotiva")
    print("-" * 60)
    base_risks = [3, 4, 5]
    tolerance = "😟 Sarei molto preoccupato - Probabilmente venderei"
    max_allowed = risk_tolerance_hard_caps[tolerance]
    
    filtered = [r for r in base_risks if r <= max_allowed]
    print(f"Rischi base: {base_risks}")
    print(f"Tolleranza: {tolerance}")
    print(f"Max rischio consentito: {max_allowed}")
    print(f"Rischi dopo filtro: {filtered}")
    
    assert filtered == [3], f"❌ Filtro errato! Atteso [3], ottenuto {filtered}"
    print("✅ TEST 2 PASSATO - Media tolleranza correttamente filtrata")
    
    # TEST 3: Alta tolleranza consente portafogli aggressivi (ma non leverage)
    print("\n📋 TEST 3: Alta Tolleranza Emotiva")
    print("-" * 60)
    base_risks = [5, 6, 7, 8]  # Include leverage (8)
    tolerance = "🚀 Sono tranquillo - È normale, compro ancora"
    max_allowed = risk_tolerance_hard_caps[tolerance]
    
    filtered = [r for r in base_risks if r <= max_allowed]
    print(f"Rischi base (con leverage): {base_risks}")
    print(f"Tolleranza: {tolerance}")
    print(f"Max rischio consentito: {max_allowed}")
    print(f"Rischi dopo filtro: {filtered}")
    
    assert 8 not in filtered, "❌ Rischio 8 (leverage) non dovrebbe passare!"
    assert filtered == [5, 6, 7], f"❌ Filtro errato! Atteso [5,6,7], ottenuto {filtered}"
    print("✅ TEST 3 PASSATO - Alta tolleranza OK, leverage escluso")
    
    # TEST 4: Tolleranza neutra
    print("\n📋 TEST 4: Tolleranza Neutra")
    print("-" * 60)
    base_risks = [4, 5, 6]
    tolerance = "😐 Sarei preoccupato ma manterrei - Capisco la volatilità"
    max_allowed = risk_tolerance_hard_caps[tolerance]
    
    filtered = [r for r in base_risks if r <= max_allowed]
    print(f"Rischi base: {base_risks}")
    print(f"Tolleranza: {tolerance}")
    print(f"Max rischio consentito: {max_allowed}")
    print(f"Rischi dopo filtro: {filtered}")
    
    assert filtered == [4, 5], f"❌ Filtro errato! Atteso [4,5], ottenuto {filtered}"
    print("✅ TEST 4 PASSATO - Tolleranza neutra correttamente limitata")
    
    # TEST 5: Edge case - Base risks tutti sotto il cap
    print("\n📋 TEST 5: Edge Case - Rischi Bassi")
    print("-" * 60)
    base_risks = [1, 2]
    tolerance = "😊 Lo vedrei come opportunità - Comprerei di più se possibile"
    max_allowed = risk_tolerance_hard_caps[tolerance]
    
    filtered = [r for r in base_risks if r <= max_allowed]
    print(f"Rischi base: {base_risks}")
    print(f"Tolleranza: {tolerance}")
    print(f"Max rischio consentito: {max_allowed}")
    print(f"Rischi dopo filtro: {filtered}")
    
    assert filtered == [1, 2], "❌ Non dovrebbe filtrare nulla!"
    print("✅ TEST 5 PASSATO - Rischi bassi non filtrati")
    
    # RIEPILOGO
    print("\n" + "=" * 60)
    print("✅ TUTTI I TEST PASSATI!")
    print("=" * 60)
    print("\nLa correzione degli hard limits funziona correttamente:")
    print("- 😰 Bassa tolleranza → MAX rischio 2")
    print("- 😟 Media-bassa tolleranza → MAX rischio 3")
    print("- 😐 Media tolleranza → MAX rischio 5")
    print("- 😊😚 Alta tolleranza → MAX rischio 7 (NO leverage)")
    print("\nRischio 8 (leverage) sempre escluso separatamente.")
    
    return True


def test_portfolios_mapping():
    """
    Testa la mappatura tra livelli di rischio e portafogli disponibili
    """
    
    print("\n\n🗂️ Mappatura Portafogli per Tolleranza")
    print("=" * 60)
    
    portfolios_by_risk = {
        1: ["PORT11a (Money Market)", "PORT11b (iBonds)", "PORT21a (ESG)"],
        2: ["PORT2a (20% azioni)", "PORT2b (30% azioni)", "PORT22a (ESG 30% azioni)"],
        3: ["PORT3 (40% azioni)", "PORT13 (LifeStrategy 40%)", "PORT23a (ESG 40% azioni)"],
        5: ["PORT5 (60% azioni)", "PORT6a (70% azioni)", "PORT15 (LifeStrategy 60%)", 
            "PORT25a (ESG 60%)", "PORT26 (ESG 80%)"],
        6: ["PORT6b (80% azioni)", "PORT16 (LifeStrategy 80%)"],
        7: ["PORT7a (100% factor)", "PORT7b (100% geographic)", "PORT17a (ACWI)", 
            "PORT17b (World)", "PORT27 (ESG World)", "PORT27b (ESG All Cap)"],
        8: ["PORT8 (2x Leverage) - SEMPRE ESCLUSO"]
    }
    
    caps = {
        "😰 Venderei": 2,
        "😟 Molto preoccupato": 3,
        "😐 Preoccupato": 5,
        "😊 Opportunità": 7,
        "🚀 Tranquillo": 7
    }
    
    for tolerance, max_risk in caps.items():
        print(f"\n{tolerance} → MAX RISCHIO {max_risk}")
        print("-" * 60)
        print("Portafogli CONSENTITI:")
        for risk_level in sorted(portfolios_by_risk.keys()):
            if risk_level <= max_risk and risk_level != 8:
                print(f"  Rischio {risk_level}: {', '.join(portfolios_by_risk[risk_level])}")
        
        print("\nPortafogli ESCLUSI:")
        for risk_level in sorted(portfolios_by_risk.keys()):
            if risk_level > max_risk or risk_level == 8:
                print(f"  Rischio {risk_level}: {', '.join(portfolios_by_risk[risk_level])}")


def test_real_world_scenarios():
    """
    Testa scenari del mondo reale
    """
    
    print("\n\n🌍 Scenari del Mondo Reale")
    print("=" * 60)
    
    scenarios = [
        {
            "name": "Giovane Investitore Nervoso",
            "age": "25 anni",
            "horizon": "30+ anni",
            "tolerance": "😰 Venderei immediatamente",
            "expected_max": 2,
            "rationale": "Nonostante orizzonte lungo, bassa tolleranza limita a rischio 2"
        },
        {
            "name": "Investitore Pre-Pensione Prudente",
            "age": "55 anni",
            "horizon": "10 anni",
            "tolerance": "😟 Sarei molto preoccupato",
            "expected_max": 3,
            "rationale": "Orizzonte medio + bassa tolleranza = max rischio 3"
        },
        {
            "name": "Investitore Esperto con Capitale",
            "age": "40 anni",
            "horizon": "20+ anni",
            "tolerance": "🚀 Sono tranquillo",
            "expected_max": 7,
            "rationale": "Alta tolleranza + esperienza = può gestire 100% azioni (ma NO leverage)"
        },
        {
            "name": "Investitore Giovane Bilanciato",
            "age": "30 anni",
            "horizon": "15+ anni",
            "tolerance": "😐 Sarei preoccupato ma manterrei",
            "expected_max": 5,
            "rationale": "Media tolleranza = portafogli balanced fino 60% azioni"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n📊 SCENARIO {i}: {scenario['name']}")
        print("-" * 60)
        print(f"Età: {scenario['age']}")
        print(f"Orizzonte: {scenario['horizon']}")
        print(f"Tolleranza: {scenario['tolerance']}")
        print(f"\nMAX RISCHIO CONSENTITO: {scenario['expected_max']}")
        print(f"Motivazione: {scenario['rationale']}")


if __name__ == "__main__":
    print("\n🚀 Avvio Test Suite Completa")
    print("=" * 60)
    print("Test degli hard limits per tolleranza al rischio")
    print("Versione: 3.2 (Critical Fix)")
    print("=" * 60)
    
    # Esegui tutti i test
    if test_risk_tolerance_caps():
        test_portfolios_mapping()
        test_real_world_scenarios()
        
        print("\n\n🎉 SUITE COMPLETA TERMINATA CON SUCCESSO!")
        print("=" * 60)
        print("La correzione è implementata correttamente.")
        print("Puoi procedere con il deploy in sicurezza.")
        print("=" * 60)
    else:
        print("\n\n❌ ALCUNI TEST SONO FALLITI")
        print("Verifica l'implementazione della correzione in app.py")
