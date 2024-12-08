from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# Patient Schemas
class PatientBase(BaseModel):
    name: str
    # email: str
    # gender: Optional[str]
    # date_of_birth: date
    age: int
    address: Optional[str]

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    patient_id: int
    age: int

    class Config:
         from_attributes = True
# Diseases         
# class DiseaseBase(BaseModel):
#     name: str
#     description: str
#     symptoms: List[str]
#     treatment: List[str]
#     contagious: bool
#     severity: str
#     common_in: str
#     causes: List[str]

# class DiseaseCreate(DiseaseBase):
#     pass

# class Disease(DiseaseBase):
#     disease_id: int

#     class Config:
#         from_attributes = True

# Doctor Schemas
class DoctorBase(BaseModel):
    name: str
    specialization: str

class DoctorCreate(DoctorBase):
    pass

class Doctor(DoctorBase):
    doctor_id: int
    
    class Config:
         from_attributes = True

# Appointment Schemas
class AppointmentBase(BaseModel):
    patient_id: int
    doctor_id: int
    date: date
    description: Optional[str]

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    appointment_id: int
   

    class Config:
         from_attributes = True  