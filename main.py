def estimate_max_hr(age_years: int, sex: str) -> int:
    """
    Schätzt die maximale Herzfrequenz basierend auf Alter und Geschlecht.
    """
    if sex == "male":
        max_hr_bpm = 223 - 0.9 * age_years
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 * age_years
    else:
        max_hr_bpm = int(input("Geben Sie die maximale Herzfrequenz ein: "))
    return max_hr_bpm

def build_person(first_name, last_name, sex, age) -> dict:
    """
    Erstellt ein Dictionary mit Informationen über eine Person (Supervisor oder Subject).
    """
    person_dict = {
        "first_name": first_name,
        "last_name": last_name,
        "age": age,
        "estimate_max_hr": estimate_max_hr(age, sex)
    }
    return person_dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """
    Erstellt ein Dictionary mit Informationen über ein Experiment.
    """
    experiment_dict = {
        "experiment_name": experiment_name,
        "date": date,
        "supervisor": supervisor,
        "subject": subject
    }
    return experiment_dict
