import streamlit as st

# Diagnostic Knowledge Base
DIAGNOSTIC_RULES = {
    "Fish / Aquaculture": {
        "Gasping at water surface": {
            "condition": "Acute Dissolved Oxygen (DO) Depletion",
            "urgency": "CRITICAL",
            "action": "Turn on aerators immediately. Stop feeding and exchange 20-30% of pond volume with fresh, oxygenated water."
        },
        "Erratic swimming / flashing against pond walls": {
            "condition": "Ectoparasitic Infestation (e.g., Trichodina, Costia)",
            "urgency": "HIGH",
            "action": "Check water pH and ammonia levels. Isolate affected fish and prepare a supervised salt bath treatment."
        },
        "Sudden loss of feed response": {
            "condition": "Water Quality Stress or Early Bacterial Infection",
            "urgency": "MODERATE",
            "action": "Halt feeding for 24 hours. Run an immediate ammonia/nitrite test and check bottom sediment buildup."
        }
    },
    "Poultry / Livestock": {
        "Bloody droppings with ruffled feathers": {
            "condition": "Suspected Coccidiosis Outbreak",
            "urgency": "CRITICAL",
            "action": "Administer veterinary-approved anticoccidial (e.g., Amprolium) in drinking water. Replace damp bedding."
        },
        "Huddling under heat lamps / drooping wings": {
            "condition": "Severe Brooder Chilling / Hypothermia or Gumboro",
            "urgency": "HIGH",
            "action": "Inspect brooder heating units, eliminate cold drafts, and provide supportive electrolyte solution."
        }
    }
}

st.set_page_config(page_title="AgroVoice AI Diagnostic", page_icon="🐟", layout="centered")

st.title("🐟 AgroVoice Diagnostic Engine")
st.markdown("Automated condition assessment and triage advisory for aquaculture ponds and livestock pens.")

category = st.selectbox("Select Domain:", list(DIAGNOSTIC_RULES.keys()))

options = list(DIAGNOSTIC_RULES[category].keys())
selected_symptom = st.selectbox("Observed Behavior / Symptom:", options)

custom_symptom = st.text_input("Or enter specific field observation:")

if st.button("Run Diagnostic Assessment", type="primary"):
    match_key = None
    target_text = custom_symptom.lower().strip() if custom_symptom.strip() else selected_symptom.lower().strip()
    
    for key in DIAGNOSTIC_RULES[category]:
        if key.lower() in target_text or target_text in key.lower():
            match_key = key
            break
            
    if match_key:
        result = DIAGNOSTIC_RULES[category][match_key]
        st.subheader("Diagnostic Results")
        if result["urgency"] == "CRITICAL":
            st.error(f"⚠️ **Urgency Level: {result['urgency']}**")
        else:
            st.warning(f"⚠️ **Urgency Level: {result['urgency']}**")
            
        st.write(f"**Identified Condition:** {result['condition']}")
        st.info(f"**Recommended Action:** {result['action']}")
    else:
        st.info("Observation inconclusive against emergency triage rules. Please contact an extension officer or local veterinarian.")
          
