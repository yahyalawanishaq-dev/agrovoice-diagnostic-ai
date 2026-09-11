import sys

# Knowledge base for fish and poultry symptoms
DIAGNOSTIC_RULES = {
    "fish": {
        "gasping at surface": {
            "condition": "Severe Dissolved Oxygen (DO) depletion",
            "action": "Turn on aerators immediately, pause feeding, and flush 20-30% of pond water with aerated water."
        },
        "rubbing against pond walls": {
            "condition": "Potential ectoparasitic infestation (e.g., Trichodina)",
            "action": "Test water pH and ammonia, isolate sample fish, and prepare a recommended salt bath treatment."
        },
        "loss of appetite": {
            "condition": "Water quality stress or early bacterial infection",
            "action": "Check ammonia/nitrite levels right away. Cut feeding volume by 50% until water stabilizes."
        }
    },
    "poultry": {
        "bloody droppings": {
            "condition": "Likely Coccidiosis outbreak",
            "action": "Administer approved anticoccidial treatment in drinking water and replace damp litter immediately."
        },
        "drooping wings and huddling": {
            "condition": "Hypothermia, severe stress, or systemic infection",
            "action": "Check brooder heat source, inspect ventilation, and provide clean electrolyte water."
        }
    }
}

def analyze_symptom(category: str, symptom: str) -> dict:
    """Matches farmer observations against diagnostic advisory rules."""
    cat = category.lower().strip()
    sym = symptom.lower().strip()

    if cat not in DIAGNOSTIC_RULES:
        return {"status": "error", "message": f"Category '{cat}' not found. Use 'fish' or 'poultry'."}

    for known_symptom, advice in DIAGNOSTIC_RULES[cat].items():
        if known_symptom in sym or sym in known_symptom:
            return {
                "status": "success",
                "category": cat,
                "symptom_matched": known_symptom,
                "diagnosis": advice["condition"],
                "recommended_action": advice["action"]
            }

    return {
        "status": "inconclusive",
        "message": "Symptoms do not match high-risk automated rules. Contact a local extension officer or vet."
    }

if __name__ == "__main__":
    test_cat = "fish"
    test_obs = "gasping at surface"
    
    print(f"--- AgroVoice Diagnostic Test ---")
    res = analyze_symptom(test_cat, test_obs)
    print(f"Target: {test_cat}")
    print(f"Observation: {test_obs}")
    print(f"Diagnosis: {res.get('diagnosis')}")
    print(f"Action: {res.get('recommended_action')}")
  
