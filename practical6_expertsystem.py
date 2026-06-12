

knowledge_base = {
    "cold":      ["fever", "cough", "cold"],
    "malaria":   ["fever", "headache", "sweating", "vomiting"],
    "dengue":    ["fever", "rash", "joint pain", "headache"],
    "pneumonia": ["fever", "chest pain", "breathing difficulty"],
    "diabetes":  ["frequent urination", "excessive thirst", "fatigue"],
    "typhoid":   ["fever", "stomach pain", "vomiting", "headache"],
}

advice = {
    "cold":      "Take rest, drink warm fluids, consult doctor if not better.",
    "malaria":   "Get blood test done immediately. Take antimalarial drugs.",
    "dengue":    "Rush to hospital. Get platelet count checked.",
    "pneumonia": "Visit hospital immediately. Serious condition.",
    "diabetes":  "Consult doctor. Avoid sugar. Exercise regularly.",
    "typhoid":   "Take prescribed antibiotics. Drink boiled water only.",
}

def diagnose(symptoms):
    print("\n--- Diagnosis Report ---")
    found = False
    for disease, required in knowledge_base.items():
        matched = [s for s in symptoms if s in required]
        if len(matched) >= 2:
            confidence = int(len(matched) / len(required) * 100)
            print(f"Disease    : {disease.upper()}")
            print(f"Confidence : {confidence}%")
            print(f"Advice     : {advice[disease]}")
            print()
            found = True
    if not found:
        print("No disease matched. Please consult a doctor.")

def main():
    print("=== Medical Expert System ===")
    print("Enter symptoms one by one. Type 'done' when finished.\n")
    symptoms = []
    while True:
        s = input("Enter symptom: ").strip().lower()
        if s == "done":
            break
        symptoms.append(s)
    print(f"\nSymptoms entered: {symptoms}")
    diagnose(symptoms)

main()