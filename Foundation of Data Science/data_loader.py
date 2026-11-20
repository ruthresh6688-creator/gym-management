"""
Foundation of Data Science - Data Ingestion and Preprocessing Pipeline
Course: 25ITC31 - Foundations of Data Science (Units 2, 3, & 4)
Department of Information Technology, Velalar College of Engineering and Technology
"""

import os
import sqlite3
import pandas as pd
import numpy as np

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_DIR)
DB_PATH = os.path.join(PROJECT_ROOT, "gym_management.db")
DATA_DIR = os.path.join(BASE_DIR, "data")

def get_connection():
    # 1. Try MySQL Connection if available
    try:
        import mysql.connector
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="gym_management"
        )
        return conn
    except Exception:
        # 2. Seamlessly connect to bundled SQLite database
        if not os.path.exists(DB_PATH):
            raise FileNotFoundError(f"Database not found at: {DB_PATH}")
        return sqlite3.connect(DB_PATH)

def load_and_preprocess_data():
    """
    Connects to database, retrieves raw tables, performs cleaning,
    data type conversion, feature engineering, and exports clean datasets.
    """
    os.makedirs(DATA_DIR, exist_ok=True)
    conn = get_connection()

    # 1. Retrieve Raw DataFrames (Unit 2 & 3)
    members_df = pd.read_sql_query("SELECT * FROM members", conn)
    plans_df = pd.read_sql_query("SELECT * FROM membership_plans", conn)
    memberships_df = pd.read_sql_query("SELECT * FROM memberships", conn)
    trainers_df = pd.read_sql_query("SELECT * FROM trainers", conn)
    assignments_df = pd.read_sql_query("SELECT * FROM trainer_assignments", conn)
    attendance_df = pd.read_sql_query("SELECT * FROM attendance", conn)
    conn.close()

    # 2. Data Cleaning & Type Conversion (Unit 4: Data Quality & Pre-processing)
    # Datetime conversions
    members_df['registration_date'] = pd.to_datetime(members_df['registration_date'])
    memberships_df['start_date'] = pd.to_datetime(memberships_df['start_date'])
    memberships_df['expiry_date'] = pd.to_datetime(memberships_df['expiry_date'])
    assignments_df['assignment_date'] = pd.to_datetime(assignments_df['assignment_date'])
    attendance_df['attendance_date'] = pd.to_datetime(attendance_df['attendance_date'])

    # Handle missing / null values (Unit 4)
    members_df['email'] = members_df['email'].fillna('Unspecified')
    trainers_df['email'] = trainers_df['email'].fillna('Unspecified')
    attendance_df['duration_minutes'] = attendance_df['duration_minutes'].fillna(0).astype(int)

    # Remove duplicates if any
    members_df.drop_duplicates(subset=['member_id'], inplace=True)
    attendance_df.drop_duplicates(subset=['attendance_id'], inplace=True)

    # 3. Feature Engineering & Derived Variables
    # Parse check-in hour for peak-hour analysis
    attendance_df['check_in_hour'] = attendance_df['check_in_time'].apply(
        lambda t: int(str(t).split(':')[0]) if pd.notnull(t) else 6
    )
    attendance_df['workout_month'] = attendance_df['attendance_date'].dt.to_period('M').astype(str)
    attendance_df['workout_day_of_week'] = attendance_df['attendance_date'].dt.day_name()

    # Join memberships with plan names and fees
    enriched_memberships = memberships_df.merge(
        plans_df[['plan_id', 'plan_name', 'duration', 'fee']], 
        on='plan_id', 
        how='left'
    )

    # Join attendance with member names
    enriched_attendance = attendance_df.merge(
        members_df[['member_id', 'name', 'age']], 
        on='member_id', 
        how='left'
    )

    # 4. Save Cleaned Datasets to CSV (Unit 2: File Handling)
    members_df.to_csv(os.path.join(DATA_DIR, "clean_members.csv"), index=False)
    plans_df.to_csv(os.path.join(DATA_DIR, "clean_plans.csv"), index=False)
    enriched_memberships.to_csv(os.path.join(DATA_DIR, "clean_memberships.csv"), index=False)
    trainers_df.to_csv(os.path.join(DATA_DIR, "clean_trainers.csv"), index=False)
    assignments_df.to_csv(os.path.join(DATA_DIR, "clean_assignments.csv"), index=False)
    enriched_attendance.to_csv(os.path.join(DATA_DIR, "clean_attendance.csv"), index=False)

    return {
        "members": members_df,
        "plans": plans_df,
        "memberships": enriched_memberships,
        "trainers": trainers_df,
        "assignments": assignments_df,
        "attendance": enriched_attendance
    }

if __name__ == "__main__":
    data = load_and_preprocess_data()
    print("[SUCCESS] Data extracted, preprocessed, and saved to CSV files in data/ directory.")
    for name, df in data.items():
        print(f" - {name.capitalize()}: {len(df)} records, {len(df.columns)} columns")
