from flask import Flask, render_template, request, redirect, url_for
from patient_info import (upsert_patient, upsert_medical_history, upsert_symptoms,
                          upsert_lifestyle, upsert_physical_examination,
                          upsert_lab_tests)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        # Get data from the form
        patient_id = None  # Use None to auto-generate patient ID
        name = request.form['name']
        age = int(request.form['age'])
        gender = request.form['gender']
        contact_info = request.form['contact_info']
        address = request.form['address']

        # Upsert patient data
        upsert_patient(patient_id, name, age, gender, contact_info, address)

        # Get the newly inserted patient_id for further use
        patient_id = request.form['patient_id']

        # Get medical history data
        past_conditions = request.form['past_conditions']
        family_history = request.form['family_history']
        current_medications = request.form['current_medications']
        allergies = request.form['allergies']
        immunization_history = request.form['immunization_history']
        upsert_medical_history(patient_id, past_conditions, family_history, current_medications, allergies, immunization_history)

        # Get symptoms data
        onset = request.form['onset']
        nature = request.form['nature']
        severity = request.form['severity']
        duration = request.form['duration']
        frequency = request.form['frequency']
        upsert_symptoms(patient_id, onset, nature, severity, duration, frequency)

        # Get lifestyle data
        diet = request.form['diet']
        exercise = request.form['exercise']
        sleep_patterns = request.form['sleep_patterns']
        substance_use = request.form['substance_use']
        occupational_exposures = request.form['occupational_exposures']
        upsert_lifestyle(patient_id, diet, exercise, sleep_patterns, substance_use, occupational_exposures)

        # Get physical examination data
        vital_signs = request.form['vital_signs']
        general_appearance = request.form['general_appearance']
        specific_findings = request.form['specific_findings']
        upsert_physical_examination(patient_id, vital_signs, general_appearance, specific_findings)

        # Get lab tests data
        test_type = request.form['test_type']
        test_results = request.form['test_results']
        upsert_lab_tests(patient_id, test_type, test_results)

        return redirect(url_for('index'))

    return render_template('add_patient.html')

if __namae__ == '__main__':
    app.run(debug=True)