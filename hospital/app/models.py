from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

# Patient Model
class Patient(Base):
    __tablename__ = "patients"
    patient_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    # gender = Column(String, nullable= True)
    age = Column(Integer, nullable=False)
    address = Column(String, nullable=True)

    # Relationship
    appointments = relationship("Appointment", back_populates="patient")

# Disease Model

# class Disease(Base):
#     __tablename__ = 'diseases'

#     disease_id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     description = Column(Text, nullable=False)
#     symptoms = Column(JSON, nullable=False) 
#     treatment = Column(JSON, nullable=False)  
#     contagious = Column(Boolean, default=False)
#     severity = Column(String, nullable=True)
#     common_in = Column(String, nullable=True)
#     causes = Column(JSON, nullable=True) 

# Doctor Model
class Doctor(Base):
    __tablename__ = "doctors"
    doctor_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    specialization = Column(String, nullable=False)
    # Relationship
    appointments = relationship("Appointment", back_populates="doctor")

# Appointment Model
class Appointment(Base):
    __tablename__ = "appointments"
    appointment_id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.patient_id"), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.doctor_id"), nullable=False)
    date = Column(Date, nullable=False)
    description = Column(String, nullable=True)

    # Relationships
    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctor", back_populates="appointments")