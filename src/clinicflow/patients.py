def parse_age(raw: str) -> int:
    """Turn user input into an age. Raie ValueError if invlaid"""

    try:
        age = int(raw.strip())

    except ValueError as e:
        raise ValueError("Age must be a number") from e

    if not 0 <= age <= 130:
        raise ValueError("Age must be 0-130")

    return age

def add_patient(patients: dict, patient_id: str, name: str, age: int) -> dict:

    """Add a patient to the dict and return it. Raise ValueError if invalid. """

    if patient_id in patients:
        raise ValueError(f"Patient Id {patient_id} already exits. ")

    if not name.strip():
        raise ValueError("Name cannot be empty")

    patients[patient_id] = {"name": name.strip(), "age": age}
    return patients