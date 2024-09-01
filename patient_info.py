import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('patient_info.db')
c = conn.cursor()

# TABLE DEFINITIONS

# Create a table for storing patient information
c.execute('''
CREATE TABLE IF NOT EXISTS patients (
    patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    gender TEXT NOT NULL,
    contact_info TEXT NOT NULL,
    address TEXT NOT NULL
)
''')

# Create a table for storing medical history
c.execute('''
CREATE TABLE IF NOT EXISTS medical_history (
    patient_id INTEGER PRIMARY KEY,
    past_conditions TEXT,
    family_history TEXT,
    current_medications TEXT,
    allergies TEXT,
    immunization_history TEXT
)
''')

# Create a table for storing symptoms
c.execute('''
CREATE TABLE IF NOT EXISTS symptoms (
    patient_id INTEGER PRIMARY KEY,
    onset TEXT,
    nature TEXT,
    severity TEXT,
    duration TEXT,
    frequency TEXT
)
''')

# Create a table for storing lifestyle information
c.execute('''
CREATE TABLE IF NOT EXISTS lifestyle (
    patient_id INTEGER PRIMARY KEY,
    diet TEXT,
    exercise TEXT,
    sleep_patterns TEXT,
    substance_use TEXT,
    occupational_exposures TEXT
)
''')

# Create a table for storing physical examination findings
c.execute('''
CREATE TABLE IF NOT EXISTS physical_examination (
    patient_id INTEGER PRIMARY KEY,
    vital_signs TEXT,
    general_appearance TEXT,
    specific_findings TEXT
)
''')

# Create a table for storing laboratory and diagnostic test results
c.execute('''
CREATE TABLE IF NOT EXISTS lab_tests (
    patient_id INTEGER PRIMARY KEY,
    test_type TEXT,
    test_results TEXT
)
''')

# Upsert functions for each table

# Upsert for patients table
def upsert_patient(patient_id, name, age, gender, contact_info, address):
    with conn:
        c.execute('''
    INSERT INTO patients (patient_id, name, age, gender, contact_info, address)
    VALUES (:patient_id, :name, :age, :gender, :contact_info, :address)
    ON CONFLICT(patient_id) DO UPDATE SET
    name = excluded.name,
    age = excluded.age,
    gender = excluded.gender,
    contact_info = excluded.contact_info,
    address = excluded.address
    ''', {'patient_id':patient_id, 'name':name, 'age':age, 'gender':gender, 'contact_info':contact_info, 'address':address})

# Upsert for medical_history table
def upsert_medical_history(patient_id, past_conditions, family_history, current_medications, allergies, immunization_history):
    with conn:
        c.execute('''
    INSERT INTO medical_history (patient_id, past_conditions, family_history, current_medications, allergies, immunization_history)
        VALUES (:patient_id, :past_conditions, :family_history, :current_medications, :allergies, :immunization_history)
    ON CONFLICT(patient_id) DO UPDATE SET
    past_conditions = excluded.past_conditions,
    family_history = excluded.family_history,
    current_medications = excluded.current_medications,
    allergies = excluded.allergies,
    immunization_history = excluded.immunization_history
    ''', {'patient_id':patient_id, 'past_conditions':past_conditions, 
              'family_history':family_history, 'current_medications':current_medications,
                'allergies':allergies, 'immunization_history':immunization_history})

# Upsert for symptoms table
def upsert_symptoms(patient_id, onset, nature, severity, duration, frequency):
    with conn:
        c.execute('''
    INSERT INTO symptoms (patient_id, onset, nature, severity, duration, frequency)
        VALUES (:patient_id, :onset, :nature, :severity, :duration, :frequency)
    ON CONFLICT(patient_id) DO UPDATE SET
    onset = excluded.onset,
    nature = excluded.nature,
    severity = excluded.severity,
    duration = excluded.duration,
    frequency = excluded.frequency
    ''', {'patient_id':patient_id, 'onset':onset, 'nature':nature, 'severity':severity, 'duration':duration, 'frequency':frequency})

# Upsert for lifestyle table
def upsert_lifestyle(patient_id, diet, exercise, sleep_patterns, substance_use, occupational_exposures):
    with conn:
        c.execute('''
    INSERT INTO lifestyle (patient_id, diet, exercise, sleep_patterns, substance_use, occupational_exposures)
        VALUES (:patient_id, :diet, :exercise, :sleep_patterns, :substance_use, :occupational_exposures)
    ON CONFLICT(patient_id) DO UPDATE SET
    diet = excluded.diet,
    exercise = excluded.exercise,
    sleep_patterns = excluded.sleep_patterns,
    substance_use = excluded.substance_use,
    occupational_exposures = excluded.occupational_exposures
    ''', {'patient_id':patient_id, 'diet':diet, 'exercise':exercise, 'sleep_patterns':sleep_patterns, 'substance_use':substance_use, 'occupational_exposures':occupational_exposures})


# Upsert for physical_examination table
def upsert_physical_examination(patient_id, vital_signs, general_appearance, specific_findings):
    with conn:
        c.execute('''
    INSERT INTO physical_examination (patient_id, vital_signs, general_appearance, specific_findings)
    VALUES (:patient_id, :vital_signs, :general_appearance, :specific_findings)
    ON CONFLICT(patient_id) DO UPDATE SET
    vital_signs = excluded.vital_signs,
    general_appearance = excluded.general_appearance,
    specific_findings = excluded.specific_findings
    ''', {'patient_id':patient_id, 'vital_signs':vital_signs, 'general_appearance':general_appearance, 'specific_findings':specific_findings})

# Upsert for lab_tests table
def upsert_lab_tests(patient_id, test_type, test_results):
    with conn:
        c.execute('''
    INSERT INTO lab_tests (patient_id, test_type, test_results)
    VALUES (:patient_id, :test_type, :test_results)
    ON CONFLICT(patient_id) DO UPDATE SET
    test_type = excluded.test_type,
    test_results = excluded.test_results
    ''', {'patient_id':patient_id, 'test_type':test_type, 'test_results':test_results})

# Commit changes
conn.commit()