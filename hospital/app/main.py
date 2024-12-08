from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.database import SessionLocal, engine

# Initialize FastAPI app
app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Patients Endpoints
@app.post("/patients/", response_model=schemas.Patient)
def create_patient(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    return crud.create_patient(db, patient)

@app.get("/patients/", response_model=list[schemas.Patient])
def get_patients(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_patients(db, skip=skip, limit=limit)

@app.get("/patients/{patient_id}", response_model=schemas.Patient)
def get_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.get_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.put("/patients/{patient_id}", response_model=schemas.Patient)
def update_patient(patient_id: int, updated_patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    patient = crud.update_patient(db, patient_id, updated_patient)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int, db: Session = Depends(get_db)):
    patient = crud.delete_patient(db, patient_id)
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return {"message": "Patient deleted successfully"}

# Doctors Endpoints
@app.post("/doctors/", response_model=schemas.Doctor)
def create_doctor(doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    return crud.create_doctor(db, doctor)

@app.get("/doctors/", response_model=list[schemas.Doctor])
def get_doctors(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_doctors(db, skip=skip, limit=limit)

@app.get("/doctors/{doctor_id}", response_model=schemas.Doctor)
def get_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.get_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.put("/doctors/{doctor_id}", response_model=schemas.Doctor)
def update_doctor(doctor_id: int, updated_doctor: schemas.DoctorCreate, db: Session = Depends(get_db)):
    doctor = crud.update_doctor(db, doctor_id, updated_doctor)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor

@app.delete("/doctors/{doctor_id}")
def delete_doctor(doctor_id: int, db: Session = Depends(get_db)):
    doctor = crud.delete_doctor(db, doctor_id)
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor deleted successfully"}

# Appointments Endpoints
@app.post("/appointments/", response_model=schemas.Appointment)
def create_appointment(appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    return crud.create_appointment(db, appointment)

@app.get("/appointments/", response_model=list[schemas.Appointment])
def get_appointments(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_appointments(db, skip=skip, limit=limit)

@app.get("/appointments/{appointment_id}", response_model=schemas.Appointment)
def get_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = crud.get_appointment(db, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@app.put("/appointments/{appointment_id}", response_model=schemas.Appointment)
def update_appointment(appointment_id: int, updated_appointment: schemas.AppointmentCreate, db: Session = Depends(get_db)):
    appointment = crud.update_appointment(db, appointment_id, updated_appointment)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return appointment

@app.delete("/appointments/{appointment_id}")
def delete_appointment(appointment_id: int, db: Session = Depends(get_db)):
    appointment = crud.delete_appointment(db, appointment_id)
    if not appointment:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted successfully"}

# Diseases end points

# @app.post("/diseases/", response_model=schemas.Disease)
# def create_disease(disease: schemas.DiseaseCreate, db: Session = Depends(get_db)):
#     return crud.create_disease(db, disease)

# @app.get("/diseases/", response_model=list[schemas.Disease])
# def get_diseases(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     return crud.get_diseases(db, skip=skip, limit=limit)

# @app.get("/diseases/{disease_id}", response_model=schemas.Disease)
# def get_disease(disease_id: int, db: Session = Depends(get_db)):
#     disease = crud.get_disease(db, disease_id)
#     if not disease:
#         raise HTTPException(status_code=404, detail="Disease not found")
#     return disease

# @app.put("/diseases/{disease_id}", response_model=schemas.Disease)
# def update_disease(disease_id: int, updated_disease: schemas.DiseaseCreate, db: Session = Depends(get_db)):
#     disease = crud.update_disease(db, disease_id, updated_disease)
#     if not disease:
#         raise HTTPException(status_code=404, detail="Disease not found")
#     return disease

# @app.delete("/diseases/{disease_id}")
# def delete_disease(disease_id: int, db: Session = Depends(get_db)):
#     disease = crud.delete_disease(db, disease_id)
#     if not disease:
#         raise HTTPException(status_code=404, detail="Disease not found")
#     return {"message": "Disease deleted successfully"}
