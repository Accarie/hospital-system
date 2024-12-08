import pandas as pd
import random
import requests
from datetime import datetime, timedelta

# Step 1: Generate dataset for patients
def generate_patients_dataset(rows=500000):
    data = {
        "id": [num for num in range(1, rows + 1)],
        "name": [f"Patient {num}" for num in range(1, rows + 1)],
        "age": [random.randint(1, 100) for _ in range(rows)],
        "address": [f"Address {num}" for num in range(1, rows + 1)],
    }
    return pd.DataFrame(data)

# Step 1.1: Post patients data to FastAPI
def post_patients_to_api(df):
    api_url = "http://127.0.0.1:8000/patients/"
    for _, row in df.iterrows():
        patient_data = row.to_dict()
        try:
            response = requests.post(api_url, json=patient_data)
            response.raise_for_status()
            print(f"Successfully uploaded patient: {patient_data['name']}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to upload patient: {patient_data['name']}\nError: {e}")
            continue
print (pd.shape)
# Step 2: Describe the dataset
def describe_dataset(df):
    return df.describe(include="all")

# Step 3: Handle null values
def handle_null_values(df, column):
    # Randomly introduce null values for demonstration
    df.loc[random.sample(range(len(df)), 5), column] = None
    print(f"\nMissing Values in '{column}' Before Handling:")
    print(df.isnull().sum())
    df[column] = df[column].ffill()
    print(f"\nMissing Values in '{column}' After Handling:")
    print(df.isnull().sum())
    return df

# Step 4: Perform basic data processing
def process_data(df, column):
    non_null_records = df[df[column].notnull()]
    return df, non_null_records

# Step 5: Create new features
def create_new_features(df):
    # Feature 1: Age Category (Child, Adult, Senior)
    df["age_category"] = df["age"].apply(
        lambda age: "Child" if age < 18 else "Adult" if age <= 65 else "Senior"
    )
    # Feature 2: Is Active (Patients with an age less than 90 are considered active)
    df["is_active"] = df["age"] < 90
    return df

# Main execution
if __name__ == "__main__":
    print("Generating patients dataset...")
    df_patients = generate_patients_dataset(rows=500000)
    print("Dataset Shape:", df_patients.shape)
    
    print("\nPatients Dataset Description:")
    print(describe_dataset(df_patients))
    
    print("\nHandling Null Values in Address...")
    df_patients = handle_null_values(df_patients, column="address", fill_value="Unknown Address")
    
    print("\nProcessing Data...")
    df_patients, active_patients = process_data(df_patients, column="address")
    print(f"\nActive Patients: {len(active_patients)}")
    
    print("\nCreating New Features...")
    df_patients = create_new_features(df_patients)
    
    print("\nSaving Processed Dataset to 'patients_dataset.csv'...")
    df_patients.to_csv("patients_dataset.csv", index=False)
    print("Dataset saved successfully.")
    
    print("\nPosting Patients Data to API...")
    post_patients_to_api(df_patients)
    
    print("\nData processing completed!")
