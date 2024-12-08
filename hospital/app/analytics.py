import pandas as pd
import numpy as np
from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Dict, Any, List
from . import models

class HospitalAnalytics:
    def __init__(self, db: Session):
        self.db = db
        self.patients_df = self._get_patients_df()
        self.doctors_df = self._get_doctors_df()
        self.appointments_df = self._get_appointments_df()

    def _get_patients_df(self) -> pd.DataFrame:
        try:
            patients_query = self.db.query(models.Patient).all()
            if not patients_query:
                return pd.DataFrame(columns=['id','name', 'age', 'address',])
            
            return pd.DataFrame([{
                'id': patient.id,
                'name': patient.name,
                'age': patient.age,
                'address': patient.address,
                # 'guider_ids': [g.id for g in animal.guiders]
            } for patient in patients_query])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting patients data: {str(e)}")

    def _get_doctors_df(self) -> pd.DataFrame:
        try:
            doctors_query = self.db.query(models.Doctor).all()
            if not doctors_query:
                return pd.DataFrame(columns=['id', 'name', 'specialization'])
            
            return pd.DataFrame([{
                'id': doctor.id,
                'name': doctor.name,
                'specialization': doctor.specialization,
                # 'guider_ids': [g.id for g in guest.guiders]
            } for doctor in doctors_query])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting doctors data: {str(e)}")

    def _get_appointments_df(self) -> pd.DataFrame:
        try:
            appointments_query = self.db.query(models.Appointment).all()
            if not appointments_query:
                return pd.DataFrame(columns=['id', 'patient_id', 'doctor_id', 'date', 'description'])
            
            return pd.DataFrame([{
                'id': appointment.id,
                'patient_id': appointment.patient_id,
                'doctor_id': appointment.doctor_id,
                'date': appointment.date,
                'description': appointment.description
            } for appointment in appointments_query])
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error getting appointments data: {str(e)}")

    def get_basic_stats(self) -> Dict[str, Any]:
        try:
            if self.animals_df.empty or self.guiders_df.empty:
                return {
                    'patients_stats': {},
                    'animals_stats': {},
                    'total_patients': 0,
                    'total_doctors': 0
                    
                }
            
            return {
                'patients_stats': self.patients_df['age'].describe().to_dict() if not self.patients_df.empty else {},
                'doctors_stats': self.doctors_df['specialization'].describe().to_dict() if not self.doctors_df.empty else {},
                'total_patients': len(self.patients_df),
                'total_doctors': len(self.doctors_df),
                'total_appointments': len(self.appointments_df)
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error calculating basic stats: {str(e)}")

    # def get_patient_distribution(self) -> Dict[str, Any]:
    #     try:
    #         if self.patients_df.empty:
    #             return {
    #                 'native_vs_imported': {},
    #                 'species_distribution': {}
    #             }
            
    #         return {
    #             'native_vs_imported': self.patients_df['is_native'].value_counts().to_dict(),
    #             'species_distribution': self.patients_df['species'].value_counts().to_dict()
    #         }
    #     except Exception as e:
    #         raise HTTPException(status_code=500, detail=f"Error analyzing animal distribution: {str(e)}")

    def get_doctors_analysis(self) -> Dict[str, Any]:
        try:
            if self.doctors_df.empty:
                return {
                    'adult_child_ratio': {},
                    'visits_by_month': {}
                }
            
            return {
                'adult_child_ratio': self.guests_df['is_adult'].value_counts(normalize=True).to_dict(),
                'visits_by_month': pd.to_datetime(self.guests_df['visit_date']).dt.month.value_counts().sort_index().to_dict()
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error analyzing guest data: {str(e)}")

    def get_guider_analysis(self) -> Dict[str, Any]:
        try:
            if self.guiders_df.empty:
                return {
                    'gender_distribution': {},
                    'avg_service_hours_by_gender': {}
                }
            
            return {
                'gender_distribution': self.guiders_df['gender'].value_counts().to_dict(),
                'avg_service_hours_by_gender': self.guiders_df.groupby('gender')['service_hours'].mean().to_dict()
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error analyzing guider data: {str(e)}")

    def get_complex_analysis(self) -> Dict[str, Any]:
        try:
            if self.animals_df.empty or self.guests_df.empty or self.guiders_df.empty:
                return {
                    'guider_workload': {
                        'animals_per_guider': {},
                        'guests_per_guider': {}
                    },
                    'guest_animal_interactions': {
                        'native_animals_adult_guests': 0,
                        'native_animals_child_guests': 0
                    },
                    'guider_performance': {
                        'avg_animals_by_gender': {},
                        'avg_guests_by_gender': {}
                    }
                }

            animal_guider = self.animals_df.explode('guider_ids')
            guest_guider = self.guests_df.explode('guider_ids')
            
            animal_full = animal_guider.merge(
                self.guiders_df,
                left_on='guider_ids',
                right_on='id',
                suffixes=('_animal', '_guider')
            )
            
            guest_full = guest_guider.merge(
                self.guiders_df,
                left_on='guider_ids',
                right_on='id',
                suffixes=('_guest', '_guider')
            )
            
            return {
                'guider_workload': {
                    'animals_per_guider': animal_guider['guider_ids'].value_counts().describe().to_dict(),
                    'guests_per_guider': guest_guider['guider_ids'].value_counts().describe().to_dict()
                },
                'guest_animal_interactions': {
                    'native_animals_adult_guests': len(animal_full[animal_full['is_native'] & guest_full['is_adult']]),
                    'native_animals_child_guests': len(animal_full[animal_full['is_native'] & ~guest_full['is_adult']])
                },
                'guider_performance': {
                    'avg_animals_by_gender': animal_full.groupby('gender')['id_animal'].nunique().to_dict(),
                    'avg_guests_by_gender': guest_full.groupby('gender')['id_guest'].nunique().to_dict()
                }
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error in complex analysis: {str(e)}")