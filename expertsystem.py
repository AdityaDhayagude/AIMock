class MedicalDiagnosisSystem:
    def __init__(self):
        self.symptom_mapping = {
            "cough": ["cold", "flu"],
            "fever": ["flu", "COVID-19"],
            "headache": ["migraine", "tension headache"],
            "fatigue": ["anemia", "chronic fatigue syndrome"]
        }

    def diagnose(self, symptoms):
        possible_diseases = set()

        for symptom in symptoms:
            if symptom in self.symptom_mapping:
                possible_diseases.update(self.symptom_mapping[symptom])

        if possible_diseases:
            return possible_diseases
        else:
            return "No diagnosis could be made based on the given symptoms."

# Example usage
diagnosis_system = MedicalDiagnosisSystem()

while True:
    user_input = input("Please enter your symptoms (comma-separated) (or 'q' to quit): ")
    if user_input == "q":
        break

    symptoms = user_input.split(",")
    diagnosis = diagnosis_system.diagnose(symptoms)
    print(diagnosis)
