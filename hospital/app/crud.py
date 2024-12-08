from sqlalchemy.orm import Session
from datetime import date
from app import models, schemas


# Create Patient
def create_patient(db: Session, patient: schemas.PatientCreate):
    db_patient = models.Patient(
        name=patient.name,
        age=patient.age,
        address=patient.address
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient

# Read All Patients
def get_patients(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Patient).offset(skip).limit(limit).all()

# Read Single Patient
def get_patient(db: Session, patient_id: int):
    return db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()

# Update Patient
def update_patient(db: Session, patient_id: int, updated_data: schemas.PatientCreate):
    db_patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if db_patient:
        db_patient.name = updated_data.name
        db_patient.age = updated_data.age
        db_patient.address = updated_data.address
        db.commit()
        db.refresh(db_patient)
    return db_patient

# Delete Patient
def delete_patient(db: Session, patient_id: int):
    db_patient = db.query(models.Patient).filter(models.Patient.patient_id == patient_id).first()
    if db_patient:
        db.delete(db_patient)
        db.commit()
    return db_patient


# Create Doctor
def create_doctor(db: Session, doctor: schemas.DoctorCreate):
    db_doctor = models.Doctor(
        name=doctor.name,
        specialization=doctor.specialization,
    )
    db.add(db_doctor)
    db.commit()
    db.refresh(db_doctor)
    return db_doctor

# Read All Doctors
def get_doctors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Doctor).offset(skip).limit(limit).all()

# Read Single Doctor
def get_doctor(db: Session, doctor_id: int):
    return db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).first()

# Update Doctor
def update_doctor(db: Session, doctor_id: int, updated_data: schemas.DoctorCreate):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).first()
    if db_doctor:
        db_doctor.name = updated_data.name
        db_doctor.specialization = updated_data.specialization
        db.commit()
        db.refresh(db_doctor)
    return db_doctor

# Delete Doctor
def delete_doctor(db: Session, doctor_id: int):
    db_doctor = db.query(models.Doctor).filter(models.Doctor.doctor_id == doctor_id).first()
    if db_doctor:
        db.delete(db_doctor)
        db.commit()
    return db_doctor



# Create Appointment
def create_appointment(db: Session, appointment: schemas.AppointmentCreate):
    db_appointment = models.Appointment(
        patient_id=appointment.patient_id,
        doctor_id=appointment.doctor_id,
        date=appointment.date,
        description=appointment.description
    )
    db.add(db_appointment)
    db.commit()
    db.refresh(db_appointment)
    return db_appointment

# Read All Appointments
def get_appointments(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Appointment).offset(skip).limit(limit).all()

# Read Single Appointment
def get_appointment(db: Session, appointment_id: int):
    return db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()

# Update Appointment
def update_appointment(db: Session, appointment_id: int, updated_data: schemas.AppointmentCreate):
    db_appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
    if db_appointment:
        db_appointment.patient_id = updated_data.patient_id
        db_appointment.doctor_id = updated_data.doctor_id
        db_appointment.date = updated_data.date
        db_appointment.description = updated_data.description
        db.commit()
        db.refresh(db_appointment)
    return db_appointment

# Delete Appointment
def delete_appointment(db: Session, appointment_id: int):
    db_appointment = db.query(models.Appointment).filter(models.Appointment.appointment_id == appointment_id).first()
    if db_appointment:
        db.delete(db_appointment)
        db.commit()
    return db_appointment

# Create a new disease record
# def create_disease(db: Session, disease: schemas.DiseaseCreate):
#     db_disease = models.Disease(
#         name=disease.name,
#         description=disease.description,
#         symptoms=disease.symptoms,
#         treatment=disease.treatment,
#         contagious=disease.contagious,
#         severity=disease.severity,
#         common_in=disease.common_in,
#         causes=disease.causes,
#     )
#     db.add(db_disease)
#     db.commit()
#     db.refresh(db_disease)
#     return db_disease

# def get_diseases(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Disease).offset(skip).limit(limit).all()

# def get_disease(db: Session, disease_id: int):
#     return db.query(models.Disease).filter(models.Disease.disease_id == disease_id).first()

# def update_disease(db: Session, disease_id: int, updated_data: schemas.DiseaseCreate):
#     db_disease = db.query(models.Disease).filter(models.Disease.disease_id == disease_id).first()
#     if db_disease:
#         db_disease.name = updated_data.name
#         db_disease.description = updated_data.description
#         db_disease.symptoms = updated_data.symptoms
#         db_disease.treatment = updated_data.treatment
#         db_disease.contagious = updated_data.contagious
#         db_disease.severity = updated_data.severity
#         db_disease.common_in = updated_data.common_in
#         db_disease.causes = updated_data.causes
#         db.commit()
#         db.refresh(db_disease)
#     return db_disease

# def delete_disease(db: Session, disease_id: int):
#     db_disease = db.query(models.Disease).filter(models.Disease.disease_id == disease_id).first()
#     if db_disease:
#         db.delete(db_disease)
#         db.commit()
#     return db_disease

