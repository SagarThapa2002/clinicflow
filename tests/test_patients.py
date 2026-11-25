import pytest
from clinicflow.patients import add_patient, parse_age


@pytest.mark.parametrize("raw, expected", [
    ("25", 25),
    (" 40 ", 40),   #spaces are stripped
    ("0", 0),       #lower edge
    ("130", 130),   #upper edge
])
def test_parse_age_valid(raw, expected):
    assert parse_age(raw) == expected

@pytest.mark.parametrize("raw", ["abc","","12.5","twenty"])
def test_parse_age_not_a_number(raw):
    with pytest.raises(ValueError, match="Age must be a number"):
        parse_age(raw)

    
@pytest.mark.parametrize("raw", ["-1", "131", "200"])
def test_parse_age_out_of_range(raw):
    with pytest.raises(ValueError, match="Age must be 0-130"):
        parse_age(raw)


def test_add_patient_success():
    patients ={}
    result = add_patient(patients, "A1", "Josh", 29)
    assert result == {"A1": {"name": "Josh", "age": 29}}
    assert result is patients


def test_add_patient_duplicate_id():
    patients = {"A1": {"name": "Josh", "age": 29}}
    with pytest.raises(ValueError, match="already exits"):
        add_patient(patients, "A1", "Max", 38)

def test_add_patient_empty_name():
    with pytest.raises(ValueError, match="Name cannot be empty"):
        add_patient({}, "p3", " ", 30)


def test_add_patient_strips_name():
    patients = add_patient({}, "P3", " Matt ", 39)
    assert patients["P3"]["name"] == "Matt"